"""Helper class for version an API"""

def mount_api_version(base_app, versioned_app):
    """Helper class for version an API"""
    base_app.mount(versioned_app.openapi_prefix, versioned_app)
