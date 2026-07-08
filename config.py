import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

GETHUB_ORG = os.getenv("GITHUB_ORGS").split(',')

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT"))

PER_PAGE = int(os.getenv("PER_PAGE"))

SCHEDULE_HOURE = int(os.getenv("SCHEDULE_HOURE"))
SCHEDULE_MINUTE = int(os.getenv("SCHEDULE_MINUTE"))
TIME_ZONE = os.getenv("TIME_ZONE")


# the varibale of connection with smpt server
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")