import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.ingredient import ingredient_route
from api.main_page import main_route
from api.recipe import recipe_route
from core.config import settings
from core.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_route)
main_app.include_router(recipe_route)
main_app.include_router(ingredient_route)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
