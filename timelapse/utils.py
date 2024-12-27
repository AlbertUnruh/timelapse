# standard library
from datetime import UTC, datetime
from pathlib import Path

# local
from .camera import capture
from .video import convert_to_mp4
from .webdav import download_session, save_image, save_video


__all__ = ("capture_and_save", "generate_new_session", "generate_video_and_save")


def capture_and_save(session: str) -> None:
    save_image(session, capture())


def generate_new_session() -> str:
    return datetime.now(UTC).isoformat(" ", "seconds")


def generate_video_and_save(session: str) -> Path:
    path = convert_to_mp4(download_session(session))
    save_video(session, path.read_bytes())
    return path
