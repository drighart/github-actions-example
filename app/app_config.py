"""Contains the application configurations for various deployment scenarios."""

import os


class Config: # pylint: disable=R0903
    """Class met configuratie."""
    try:
        CURRENT_NAMESPACE = os.environ.get('CURRENT_NAMESPACE')
    except KeyError:
        CURRENT_NAMESPACE = 'dnb-got-tst'


def get_setting(key: str):
    """Return value set for key.
    Args:
        key (str): key of configuration setting
    Returns:
        value if key exists, None otherwise
    """
    return getattr(Config, key, None)
