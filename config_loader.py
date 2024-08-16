import configparser

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    return {section: dict(config.items(section)) for section in config.sections()}

def read_identity_string_or_domain_name(source):
    config = load_config(source)
    identity_string_or_domain_name = None
    if 'identity' in config:
        identity_string_or_domain_name = config['identity'].get('string', config['identity'].get('domain_name'))
    return identity_string_or_domain_name