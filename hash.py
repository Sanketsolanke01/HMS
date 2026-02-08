from passlib.context import CryptContext

ph=CryptContext(schemes=["argon2"],deprecated="auto")

# To be used in Register API
def generate_hash_password(password:str)->str:
    return ph.hash(password)

#To be used in Login API
def verify_password(plain_password:str,hash_password:str)->bool:
    return ph.verify(plain_password,hash_password)
