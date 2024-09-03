import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26718902"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0c21902b496c8b8828fa5fd2b6720649")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority")
