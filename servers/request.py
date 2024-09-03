from settings.settings import ALLOWED_HOSTS


def split_domain(allowed_hosts: list[str]) -> str:
    if not allowed_hosts or all(host == "*" for host in allowed_hosts):
        raise ValueError("No valid hosts found")
    
    for host in allowed_hosts:
        if host != "*":
            return host

    return "0.0.0.0"


def get_host() -> str:
    try:
        allowed_hosts = ALLOWED_HOSTS
        if allowed_hosts is None:
            allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

        domain = split_domain(allowed_hosts)

        return domain

    except ValueError as e:
        print(f"An error occurred: {e}")
        return None