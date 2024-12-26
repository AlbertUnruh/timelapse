# standard library
from datetime import UTC, datetime

# local
from .camera import capture
from .webdav import save_image


__all__ = ("capture_and_save", "generate_new_session")


def capture_and_save(session: str) -> None:
    save_image(session, capture())


def generate_new_session() -> str:
    return datetime.now(UTC).isoformat(" ", "seconds")
