import httpx

from jobox.constants import BASE_URL
from jobox.struct import ConfigChannel


def parse_channels(channels_str: str) -> list[ConfigChannel]:
    channels_split = channels_str.strip().split(",")
    channels = []

    for ch in channels_split:
        channels.append(ConfigChannel.from_channel_id(ch))

    return channels


def get_channel_uploads_playlist(
    api_key: str, *, handle: str | None = None, channel_id: str | None = None
) -> str:
    """Get channel uploads playlist id.
    Provide either `handle` or `channel_id`. `handle` is priotised.
    Return the playlist ID.
    """
    params = dict(
        part="contentDetails",
        key=api_key,
        maxResults=50,
    )
    if handle:
        params["forHandle"] = handle
    elif channel_id:
        params["id"] = channel_id
    else:
        raise ValueError("Must provide `handle` or `channel_id`.")

    response = httpx.get(
        httpx.URL(
            BASE_URL.join(f"channels"),
            params=params,
        )
    )
    if response.status_code != 200:
        raise ValueError(
            f"Could not fetch uploads for channel handle/id: {repr(handle or channel_id)}"
        )

    rj = response.json()

    return rj["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_playlist_videos(api_key: str, playlist_id: str):
    params = dict(
        part="snippet,contentDetails",
        playlistId=playlist_id,
        key=api_key,
        maxResults=50,
    )
    response = httpx.get(
        httpx.URL(
            BASE_URL.join(f"playlistItems"),
            params=params,
        )
    )

    if response.status_code != 200:
        raise ValueError(f"Could not fetch videos for playlist id: {playlist_id}")

    rj = response.json()

    return rj
