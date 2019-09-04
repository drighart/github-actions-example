"""Helper class for technical monitoring with Prometheus"""
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette_prometheus import PrometheusMiddleware, metrics


def initialize_prometheus_middleware(app, endpoint='/metrics'):
    """Add middleware to the webserver"""
    app.add_middleware(PrometheusMiddleware)
    app.add_route(endpoint, metrics)


def initialize_health_route(app, endpoint='/health'):
    """Add health endpoint"""
    app.add_route(endpoint, health)


def health(request: Request) -> JSONResponse: #pylint: disable=W0613
    """Handles health endpoint"""
    content = {"status": "OK"}
    return JSONResponse(content=content)
