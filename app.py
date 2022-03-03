from dotenv import load_dotenv
from dotenv import dotenv_values
import os
load_dotenv()  # take environment variables from .env.

EMAIL_ADD = os.getenv("EMAIL_ADD") # get enviroment variable from .env
PASSWORD = os.getenv("PASSWORD")
MYNAME = os.getenv("MYNAME")

print(EMAIL_ADD,PASSWORD,MYNAME) # MYNAME = VIET

# Load configuration without altering the environment
config = dotenv_values(".env")
print(type(config)) # an orderdict contain content in env.

'''Use load_dotenv(override = True) to override the enviroment 
variable by the value in .env file'''
load_dotenv(override=True)

EMAIL_ADD = os.getenv("EMAIL_ADD") # get enviroment variable from .env
PASSWORD = os.getenv("PASSWORD")
MYNAME = os.getenv("MYNAME")
print(EMAIL_ADD,PASSWORD,MYNAME) # MYNAME = PATRICE_WOLFGANG



