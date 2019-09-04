"""Main class"""
import uvicorn
from fastapi import FastAPI

from app.core.initializers.monitoring import initialize_prometheus_middleware
from app.core.initializers.monitoring import initialize_health_route
from app.core.initializers.mounting import mount_api_version
from app.versions.v1 import app as v1

# Create new application instance
app = FastAPI() # pylint: disable=C0103

# Activate enabled API versions
mount_api_version(app, v1)

# Add middleware
initialize_prometheus_middleware(app)
initialize_health_route(app)

if __name__ == '__main__':
    # Run the application locally
    uvicorn.run(app, host='127.0.0.1', port=8000)
