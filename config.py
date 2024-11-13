# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28174664"))
API_HASH = getenv("API_HASH", "f504bf34ad7dbc597c8802db2f46453c")
BOT_TOKEN = getenv("BOT_TOKEN", "7609001774:AAEOlC4qbdmf0gRp5KCj28SIOJ6z2NT4rKg")
OWNER_ID = int(getenv("OWNER_ID", "219249035"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://Sachinsir:SSRAssra@cluster0.c3xqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1004516055574"))
FORCESUB = getenv("FORCESUB", "testdirrest")
