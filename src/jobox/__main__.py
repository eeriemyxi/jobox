import logging
import sqlite3

from jobox import sql, yt
from jobox.constants import API_KEY, CHANNELS, SCRIPT_DIR
from jobox.struct import ConfigChannelType

logging.basicConfig(level="INFO")
log = logging.getLogger(__name__)

conn = sqlite3.connect(SCRIPT_DIR / "videos.db")
cur = conn.cursor()


def main() -> int:
    sql.load_startup_schema(conn, cur)

    parsed_channels = yt.parse_channels(CHANNELS)

    sql.sync_configuration(conn, cur, parsed_channels)
    # TODO: sync videos
    # NOTE: make sure to check for latest uploads
    for ch in parsed_channels:
        is_id = ch.channel_type == ConfigChannelType.HANDLE
        uploads = yt.get_channel_uploads_playlist(
            API_KEY, **{"handle" if is_id else "channel_id": ch.id}
        )

        if uploads:
            vids = yt.get_playlist_videos(API_KEY, playlist_id=uploads)
            log.info(
                "Fetched videos for channel handle/id %s: %s",
                ch.id,
                vids,
            )

    return 0


if __name__ == "__main__":
    exit(main())
