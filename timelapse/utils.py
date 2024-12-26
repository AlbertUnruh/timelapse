# standard library
from datetime import UTC, datetime


__all__ = ("generate_new_session",)


def generate_new_session() -> str:
    return datetime.now(UTC).isoformat(" ", "seconds")
