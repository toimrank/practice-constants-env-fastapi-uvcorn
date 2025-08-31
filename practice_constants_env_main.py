import constants
from group_constants import Database, Server
from status import Status

''' START - Constants '''
# From constants.py
print("From constants - ", constants.DB_PASSWORD)

# From group_constants.py
print("Group constants Database - ", Database.PASSWORD)
print("Group constants Server - ", Server.DNS)

print("Enum - ", Status.ACTIVE)
print("Enum Value - ", Status.ACTIVE.value)
''' END - Constants '''


''' START - Environment Variables '''
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# .env files having url, username and password 
db_url = os.getenv("DB_URL")
user_name = os.getenv("USER_NAME")
user_password = os.getenv("USER_PASSWORD")

# environment variables from OS 
java_home = os.getenv("JAVA_HOME")

# Print environment variables value
print("DB URL:", db_url)
print("User Name:", user_name)
print("User Password:", user_password)
print("JAVA HOME:", java_home)
''' END - Environment Variables '''




