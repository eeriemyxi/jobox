from jobox.constants import SCRIPT_DIR
from jobox.struct import ConfigChannel


def load_startup_schema(conn, cur):
    with open(SCRIPT_DIR / "schema.sql") as schema:
        schema = schema.read()
        cur.executescript(schema)
        conn.commit()


def sync_configuration(conn, cur, config_channels: list[ConfigChannel]):
    cur.execute("SELECT * FROM videos")
    db_channels = cur.fetchall()

    for id, _ in db_channels:
        if not any(ch.id == id for ch in config_channels):
            cur.execute(f"DELETE FROM Videos WHERE id = ?", id)
            break
    for ch in config_channels:
        if not any(ch.id == row[0] for row in db_channels):
            cur.execute(
                "INSERT INTO Videos VALUE (?, ?)", ch.id, ch.channel_type.name.lower()
            )
            break
    conn.commit()
