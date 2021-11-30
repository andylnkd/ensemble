from fastapi import FastAPI
from .core.config import ALLOWED_HOSTS, API_V1_STR, PROJECT_NAME
from fastapi.middleware.cors import CORSMiddleware
# from .api.api_v1.api import router as api_router
from .db.mongodb_utils import connect_to_mongo, close_mongo_connection

app = FastAPI()

if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.add_event_handler("startup", connect_to_mongo)


@app.on_event("startup")
async def startup():
    connect = await connect_to_mongo()


# app.add_event_handler("shutdown", close_mongo_connection)


@app.on_event("shutdown")
async def shutdown():
    disconnect = await close_mongo_connection()


@app.get("/")
async def read_root():
    return {"Hello": "Root"}

# app.include_router(api_router, prefix=API_V1_STR)