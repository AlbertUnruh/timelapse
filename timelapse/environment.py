# standard library
from functools import cached_property
from pathlib import Path

# third party
from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


__all__ = ("env",)


class Environment(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        extra="ignore",
        env_file=((__env := Path(__file__).parents[1].joinpath(".env")), __env.with_suffix(".prod")),
        # .env-files are located in the same directory as the python package, not inside it
        env_file_encoding="utf-8",
    )

    URL: HttpUrl
    """The webdav-url (including credentials)."""
    CAMERA: int
    """The camera to capture from."""
    SPAN: float = 1.0
    """The total span to cover with the timelapse. (in days)"""
    FPS: int = 20
    """How many frames the timelapse should have per second."""
    DURATION: int = 60
    """How long the final timelapse should be. (in seconds)"""

    @cached_property
    def sessions_url(self) -> str:
        return str(self.URL).rstrip("/") + "/sessions/"

    def session_url(self, session: str) -> str:
        return f"{self.sessions_url}{session}/"

    @cached_property
    def saves_url(self) -> str:
        return str(self.URL).rstrip("/") + "/saves/"


env = Environment()
