# standard library
from io import BytesIO
from xml.etree.ElementTree import ElementTree

# local
from .copper_wire import mkcol, propfind
from .environment import env


__all__ = ("download_session", "find_sessions", "send")


def send() -> bool:
    pass


def find_sessions(*, is_retry_after_404: bool = False) -> list[str]:
    response = propfind(env.sessions_url)
    if response.status_code == 404:  # noqa: PLR2004
        if is_retry_after_404:  # does the folder not exist?
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
            sessions.append(t[:-1])

    return sessions


def download_session(session: str) -> list[...]:
    raise NotImplementedError
