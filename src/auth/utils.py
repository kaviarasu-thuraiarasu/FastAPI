from passlib.context import CryptContext
import jwt
from datetime import datetime,timedelta
import uuid
import logging

password_hash = CryptContext(schemes=['bcrypt'])

def generate_hash_password(password:str)->str:
    hash = password_hash.hash(password)
    return hash

def verify_password(password:str,hashPassword:str)->bool:
    return password_hash.verify(password,hashPassword)

def create_jwt_token(user_data:dict,expiry:timedelta=30000,refrest_token:bool=False):
    payload = {}
    payload['user'] = user_data 
    payload['exp'] = datetime.now() + expiry 
    payload['jti'] = str(uuid.uuid4())
    payload['refrest_token'] = refrest_token

    token = jwt.encode(payload=payload,algorithm='HS256',key='This is an Highly Confidential details')
    return token


def decode_token(token:str)->dict:
    # token may expired or failed to decode the token, so we are using try , except block
    try:
        token_data = jwt.decode(
            jwt=token,
            algorithms=['HS256'],
            key='This is an Highly Confidential details'
        )
        return token_data
    except jwt.PyJWTError as e:
        logging.exception(e) 
        return None