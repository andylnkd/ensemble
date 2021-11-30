import os

from starlette.datastructures import Secret, CommaSeparatedStrings

API_V1_STR = "/api"
JWT_TOKEN_PREFIX = "Token"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week

MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
# SECRET_KEY = Secret(os.getenv("SECRET_KEY", "secret key for project"))
SECRET_KEY = "rajshirolkar"

PROJECT_NAME = os.getenv("PROJECT_NAME", "Mental Health app")
ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
# MONGODB_URL = "mongodb+srv://FirstSuperUser:FSU#01@cluster0.0zilq.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE&retryWrites=true&w=majority"

database_name = "freelance"
article_collection_name = "articles"
favorites_collection_name = "favorites"
tags_collection_name = "tags"
users_collection_name = "users"
comments_collection_name = "commentaries"
followers_collection_name = "followers"
community_collection_name = "communities"
community_member_collection_name = "community_requests"
