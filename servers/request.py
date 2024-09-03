from settings.settings import ALLOWED_HOSTS
from typing import List


def split_domain(allowed_hosts: List[str]) -> str:
    """
    Splits host from a list and returns the first matching host.

    Args:
        allowed_hosts (List[str]): A list of allowed hosts.

    Returns:
        str: The first matching host or "0.0.0.0" if the host is "*".
    Raises:
        ValueError: If allowed_hosts is an empty list.
    """
    if not allowed_hosts:
        raise ValueError("allowed_hosts cannot be an empty list")

    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        return host


def get_host() -> str:
    try:
        allowed_hosts = ALLOWED_HOSTS
        if not isinstance(allowed_hosts, list) or not all(isinstance(host, str) for host in allowed_hosts):
            raise ValueError("ALLOWED_HOSTS must be a list of strings")

        if not allowed_hosts:
            allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

        domain = split_domain(allowed_hosts)

        return domain
    except Exception as e:
        # Handle potential exceptions that may occur when accessing the ALLOWED_HOSTS variable
        raise