# ========== User Model ==========
# import all packages
from pydantic import BaseModel

class User(BaseModel) :
	name: str
	email: str 
	password: str 