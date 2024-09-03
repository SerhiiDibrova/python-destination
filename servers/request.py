from settings.settings import ALLOWED_HOSTS


def split_domain(allowed_hosts: list[str]) -> str:
    if not allowed_hosts:
        raise ValueError("allowed_hosts cannot be an empty list")

    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        return host


def get_host() -> str:
    try:
        allowed_hosts = ALLOWED_HOSTS
        if not allowed_hosts or allowed_hosts == "":
            raise ValueError("ALLOWED_HOSTS cannot be empty")

        domain = split_domain(allowed_hosts)

        return domain
    except AttributeError as e:
        print(f"An error occurred: {e}")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""