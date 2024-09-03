from settings.settings import ALLOWED_HOSTS


def split_domain(allowed_hosts: list[str]) -> str:
    """
    Splits host from a list and returns the first matching host.

    Args:
        allowed_hosts (list): A list of allowed hosts.

    Returns:
        str: The first matching host or "0.0.0.0" if the host is "*".
    Raises:
        ValueError: If allowed_hosts is an empty list.
    """
    if not allowed_hosts:
        raise ValueError("allowed_hosts cannot be empty")

    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        return host


def get_host() -> str:
    """
    Returns the first matching host from ALLOWED_HOSTS.

    If ALLOWED_HOSTS is empty, returns 'localhost'.

    Raises:
        ValueError: If an error occurs while getting the host.
    """
    try:
        # Allow variants of localhost if ALLOWED_HOSTS is empty then send default host and port
        allowed_hosts = ALLOWED_HOSTS
        if not allowed_hosts:
            allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

        domain = split_domain(allowed_hosts)

        return domain

    except ValueError as e:
        raise Exception(f"An error occurred: {e}")