## app/main.py
## importing libraries
from fastapi import FastAPI
#from api_routes.base import api_router
from app.core.config import settings
from app.db.session import engine 
from db.base_class import Base 

from app.apis.base import api_router

## adding our api routes 
def include_router(app):
    app.include_router(api_router)

## adding the functionality of creating all tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# @app.get("/")
# def hello_api():
#     return {"msg": "Hello API"}

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app 

app = start_application()

