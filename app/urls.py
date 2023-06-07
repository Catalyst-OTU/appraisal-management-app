from sys import prefix
from fastapi import APIRouter , WebSocket, Depends

from routers.users.account.main import *
#from app.main import app
import config as cfg

api_router = APIRouter()



api_router.include_router(router, prefix="", tags=['User'])
api_router.include_router(router, tags=['User & Adminstrator Accounts'], prefix='/accounts')