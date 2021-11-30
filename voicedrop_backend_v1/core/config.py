import os

from starlette.datastructures import Secret, CommaSeparatedStrings

API_V1_STR = "/api"
JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
# SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))
SECRET_KEY = "ensemble"

PROJECT_NAME = os.getenv("PROJECT_NAME", "VoiceDrop")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")

