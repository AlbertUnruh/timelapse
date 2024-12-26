# standard library
from collections.abc import Iterable
from datetime import UTC, datetime
from io import BytesIO
from urllib.parse import unquote
from xml.etree.ElementTree import ElementTree

# local
from .copper_wire import get, mkcol, propfind, put
from .environment import env


__all__ = ("download_session", "find_sessions", "save_image", "save_video")


def save_image(session: str, image: bytes, *, is_retry_after_409: bool = False) -> bool:
    response = put(f"{env.session_url(session).rstrip("/")}/{datetime.now(UTC).isoformat(" ", "seconds")}.png", image)
    if response.status_code == 409 and not is_retry_after_409:  # is the session's folder missing?  # noqa: PLR2004
        mkcol(env.sessions_url)  # try to create parent the folder (may already be present, but I don't care tbh ^^)
        mkcol(env.session_url(session))  # try to create the folder
        return save_image(session, image, is_retry_after_409=True)
    return response.status_code == 201  # noqa: PLR2004


def save_video(session: str, video: bytes, *, is_retry_after_409: bool = False) -> bool:
    response = put(f"{env.saves_url.rstrip("/")}/{session}.mp4", video)
    if response.status_code == 409 and not is_retry_after_409:  # is the save's folder missing?  # noqa: PLR2004
        mkcol(env.saves_url)  # try to create the folder
        return save_image(session, video, is_retry_after_409=True)
    return response.status_code == 201  # noqa: PLR2004


def find_sessions(*, is_retry_after_404: bool = False) -> list[str]:
    response = propfind(env.sessions_url)
    if response.status_code == 404:  # noqa: PLR2004
        if not is_retry_after_404:  # does the folder not exist?
            mkcol(env.sessions_url)  # try to create the folder
            return find_sessions(is_retry_after_404=True)
        raise NotADirectoryError(f"Unable to find {response.request.path_url}")  # noqa: TRY003, EM102

    xml_io = BytesIO(response.content)
    data = ElementTree().parse(xml_io)

    sessions = []
    _l = len(response.request.path_url)
    for d in filter(lambda _: _.text is not None, data.iterfind("*/")):
        t = d.text[_l:]
        if t.endswith("/"):
            sessions.append(unquote(t[:-1]))

    return sessions


def download_session(session: str) -> Iterable[bytes]:
    response = propfind(env.session_url(session))
    host = f"{env.URL.scheme}://{env.URL.host}:{env.URL.port}"

    xml_io = BytesIO(response.content)
    data = ElementTree().parse(xml_io)

    for d in filter(lambda _: _.text is not None, data.iterfind("*/")):
        t = d.text
        if not t.endswith("/") and (response := get(host + t)).status_code == 200:  # noqa: PLR2004
            yield response.content
