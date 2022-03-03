# STUDY PYTHON-DOTENV

## Load enviroment variable from .env file
1. Install pakage
```
pip install python-dotenv
conda install -c conda-forge python-dotenv
```
2. Load enviroment variable
```
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.

EMAIL_ADD = os.getenv("EMAIL_ADD") # get enviroment variable from .env
PASSWORD = os.getenv("PASSWORD")
```
* note: remember to ignore the .env with gitignore before pushing, otherwise your secret development setting will be reveal

3. Overwrite enviroment variable by value in .env 
* set  enviroment variable MYNAME = VIET
```
conda env config vars set MYNAME=VIET
```
* In .env file, MYNAME = PATRICE_WOLFGANG
* If use default
```
load_dotenv()
EMAIL_ADD = os.getenv("EMAIL_ADD")
PASSWORD = os.getenv("PASSWORD")
MYNAME = os.getenv("MYNAME) (MYNAME = VIET)
```
* If use overwrite
```
load_dotenv(override=True)
EMAIL_ADD = os.getenv("EMAIL_ADD")
PASSWORD = os.getenv("PASSWORD")
MYNAME = os.getenv("MYNAME) (MYNAME = PATRICE_WOLFGANG)
```
