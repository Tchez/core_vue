from decouple import config

APP_ID = "core_vue"

ELASTIC_APM = {
    "SERVICE_NAME": "core_vue",
    "SERVER_URL": config("ELASTIC_APM_SERVER_URL"),
    "DEBUG": config("DEBUG", default=False, cast=bool),
    "ENVIRONMENT": config("ENVIRONMENT", default="desenvolvimento"),
}