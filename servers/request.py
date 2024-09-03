from settings.settings import ALLOWED_HOSTS
from typing import List, Union


def split_domain(allowed_hosts: List[str]) -> Union[List[str], str]:
    result = []
    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        result.append(host)
    return result


def get_host() -> Union[str, None]:
    try:
        allowed_hosts = ALLOWED_HOSTS
    except AttributeError as e:
        raise ValueError("ALLOWED_HOSTS is not defined") from e

    if not isinstance(allowed_hosts, list):
        raise ValueError("ALLOWED_HOSTS must be a list")

    if not allowed_hosts:
        allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

    domain = split_domain(allowed_hosts)

    if isinstance(domain, str):
        return domain
    elif len(domain) > 0:
        return domain[0]
    else:
        return None