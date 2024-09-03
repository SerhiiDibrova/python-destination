from settings.settings import ALLOWED_HOSTS
from typing import List, Union


def split_domain(allowed_hosts: List[Union[str, None]]) -> str:
    """
    Returns a single host from the allowed hosts.

    Args:
        allowed_hosts (List[Union[str, None]]): A list of allowed hosts.

    Returns:
        str: A single host or "0.0.0.0" if the only host is "*".
    """
    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        elif host is not None:
            return host
    return ""


def get_host() -> str:
    try:
        allowed_hosts = ALLOWED_HOSTS
    except AttributeError as e:
        print(f"An error occurred: {e}")
        return ""

    if not isinstance(allowed_hosts, list):
        allowed_hosts = []

    if not allowed_hosts:
        allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

    domain = split_domain(allowed_hosts)

    return domain