# standard library
from functools import cached_property
from pathlib import Path
from typing import Annotated

# third party
from annotated_types import Ge, Gt
from pydantic import HttpUrl, SecretStr
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
    """The webdav-url."""
    AUTHORIZATION: SecretStr = None
    """The authorization header."""
    CAMERA: int = 0
    """The camera to capture from."""
    SPAN: Annotated[float, Gt(gt=0)] = 1.0
    """The total span to cover with the timelapse. (in days)"""
    FPS: Annotated[int, Ge(ge=1)] = 20
    """How many frames the timelapse should have per second."""
    DURATION: Annotated[int, Ge(ge=1)] = 60
    """How long the final timelapse should be. (in seconds)"""
    PRE_CAPTURES: Annotated[int, Ge(ge=0)] = 5
    """How many captures should be taken before they are used."""

    @cached_property
    def sessions_url(self) -> str:
        return str(self.URL).rstrip("/") + "/sessions/"

    def session_url(self, session: str) -> str:
        return f"{self.sessions_url}{session}/"

    @cached_property
    def saves_url(self) -> str:
        return str(self.URL).rstrip("/") + "/saves/"


env = Environment()
