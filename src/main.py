import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from  src.api.main_page import main_route
from  src.api.recipes import recipe_route
from  src.core.config import settings
from  src.core.models.db_helper import db_helper



@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(main_route)
main_app.include_router(recipe_route)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )