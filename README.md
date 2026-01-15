# YouTube Video Downloader (yt-dlp)

**A small utility for downloading videos and playlists using yt-dlp.**

---

## Why use yt-dlp (not another library)

- **Actively maintained fork** of youtube-dl with frequent fixes and updates — this matters for site changes and format extraction reliability.
- **Broader site support** and more extractors (works with many more platforms and edge cases).
- **Better feature set**: faster format selection, native support for playlists, subtitles, chapters, and best-quality selection.
- **Flexible CLI + Python API**: usable as a command-line tool or embedded programmatically via `yt_dlp` Python module.
- **Community & stability**: widely used with better maintenance, which reduces breakage risk compared to smaller or unmaintained libraries.

---

## Quick start (macOS / Linux / Windows)

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.\.venv\Scripts\activate  # Windows (PowerShell/CMD)
```

2. Install the package:

```bash
pip install -U yt-dlp
```

3. Usage examples:

- From the command line (download best quality):

```bash
yt-dlp "https://www.youtube.com/watch?v=VIDEO_ID"
```

- Download a playlist:

```bash
yt-dlp -i --yes-playlist "PLAYLIST_URL"
```

- Using in Python (basic example):

```python
from yt_dlp import YoutubeDL

def download(url, outtmpl='%(title)s.%(ext)s'):
    opts = {'outtmpl': outtmpl}
    with YoutubeDL(opts) as ydl:
        ydl.download([url])
```

> Tip: The local script `youtube.py` in this repo demonstrates a simple wrapper around `yt-dlp`.

---

## Configuration & Best Practices

- Use a virtual environment and pin `yt-dlp` in `requirements.txt` if the project will be deployed or reused.
- For private or age-restricted content, pass cookies or credentials via `--cookies` or `--username/--password`.
- Prefer using `yt_dlp` Python API for tighter integration (progress hooks, metadata handling, retries).

---

## Possible future enhancements

- Add a small GUI (Tkinter / Electron / Tauri) for non-technical users.
- Add concurrency to download multiple videos in parallel (async or thread pool).
- Add format presets and automatic post-processing (transcoding, embedding metadata).
- Support for scheduled downloads, database-backed job queue, and resume/retry logic.
- Add unit and integration tests, CI workflows, and package the tool (pip or Homebrew formula).

