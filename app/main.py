from fastapi import FastAPI
from app.api.routes import router
from app.core.logger import setup_logging, get_logger
from app.core.config import settings


def create_app() -> FastAPI:
    setup_logging()

    app = FastAPI(title=settings.service_name)

    logger = get_logger(settings.service_name)
    logger.info("service_initializing", environment=settings.environment)

    app.include_router(router)

    return app


app = create_app()