
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "24620300" # integer value, dont use ""
    API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"
    TOKEN = "7628114935:AAEclzS7e_9yZ2WZdYEZUDGFniDta9NzboI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 7765692814 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "Elina_Roxbot_support"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/aa231f7d02e55a1c9dde5-9cf8b00afc3a5b8aa4.jpg"
    EVENT_LOGS = (-1002318902811)  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://Valentina:Valentina@valentina.pkv2i2s.mongodb.net/?retryWrites=true&w=majority&appName=valentina"
    # RECOMMENDED
    BOT_USERNAME = "Elina_Roxbot"
    DATABASE_URL = "postgres://wsnioboi:Fkf1ef7qRJVP1CvP_gKYqhdxk6LXBbQE@balarama.db.elephantsql.com/wsnioboi"
    CASH_API_KEY = (
        "XWHWZAMUD5BWUW6F"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "NGAA314JQZXB"
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [7186437295]  # User id of sudo users
    DEV_USERS = [6848223695]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
