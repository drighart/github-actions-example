"""Helper class for API documentation"""

def prepare_example_response(example_response, content_type: str = 'application/json') -> dict:
    """Helper class for API documentation"""
    return {'content': {content_type: {'example': example_response}}}
