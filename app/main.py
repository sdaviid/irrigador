from fastapi import(
    Depends,
    FastAPI,
    HTTPException,
    Response,
    status
)
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse


from app.core.database import(
    SessionLocal,
    engine,
    Base
)

from app.api.base import api_router


Base.metadata.create_all(bind=engine)

description = """
This API was developed for a scenario where exists a sprinkler that can communicate with an external system to obtain information on when to water a plant.
Some information like description are also available for a possible front-end to distinguish the items.
"""

tags_metadata = [
    {
        "name": "sprinkler",
        "description": "Register information about a sprinkler.",
    },
    {
        "name": "plant",
        "description": "Information about a plant.",
    },
    {
        "name": "waterday",
        "description": "Operations on when to water a plant.",
    },
    {
        "name": "log",
        "description": "Access to logs about actions made by a sprinkler."
    }
]



app = FastAPI(
    title="IrrigadorAPI",
    description=description,
    version="0.0.1",
    contact={
        "name": "David Souza",
        "url": "https://davidsouza.site",
        "email": "email@davidsouza.site"
    },
    openapi_tags=tags_metadata
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)



app.include_router(api_router)



