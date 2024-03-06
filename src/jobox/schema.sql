CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,
    channel_id TEXT NOT NULL,
    channel_name TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    upload_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS channels (
    id TEXT PRIMARY KEY,
    type TEXT NOT NULL,
    latest_video_date TEXT NOT NULL,
    next_page_token TEXT NULL
);
