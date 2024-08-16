import argparse
import configparser
import re

def read_identity_string_or_domain_name(source):
    if source.startswith('--'):
        parser = argparse.ArgumentParser()
        parser.add_argument('--identity', type=str, help='Identity string or domain name')
        args = parser.parse_args()
        identity_string_or_domain_name = args.identity
    else:
        config = configparser.ConfigParser()
        config.read(source)
        identity_string_or_domain_name = config.get('DEFAULT', 'identity')

    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(identity_string_or_domain_name):
        raise ValueError("Invalid identity string or domain name")

    return identity_string_or_domain_name