# third party
from requests import request
from requests.models import Response


__all__ = (
    "get",
    "mkcol",
    "propfind",
    "put",
)


def get(url: str, **kwargs) -> Response:
    return request("get", url, **kwargs)


def mkcol(url: str, **kwargs) -> Response:
    return request("mkcol", url, **kwargs)


def propfind(url: str, **kwargs) -> Response:

    return request("propfind", url, **kwargs)


def put(url: str, data: ... = None, **kwargs) -> Response:
    return request("put", url, data=data, **kwargs)
