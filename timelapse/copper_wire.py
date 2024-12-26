# third party
from requests import request
from requests.models import Response

# local
from .environment import env


__all__ = ("get", "mkcol", "propfind", "put")


def get(url: str, **kwargs) -> Response:
    headers = {"Authorization": env.AUTHORIZATION.get_secret_value() or ""} | kwargs.pop("headers", {})
    return request("get", url, headers=headers, **kwargs)


def mkcol(url: str, **kwargs) -> Response:
    headers = {"Authorization": env.AUTHORIZATION.get_secret_value() or ""} | kwargs.pop("headers", {})
    return request("mkcol", url, headers=headers, **kwargs)


def propfind(url: str, **kwargs) -> Response:
    headers = {"Authorization": env.AUTHORIZATION.get_secret_value() or ""} | kwargs.pop("headers", {})
    return request("propfind", url, headers=headers, **kwargs)


def put(url: str, data: ... = None, **kwargs) -> Response:
    headers = {"Authorization": env.AUTHORIZATION.get_secret_value() or ""} | kwargs.pop("headers", {})
    return request("put", url, data=data, headers=headers, **kwargs)
