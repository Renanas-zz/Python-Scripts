from passlib.hash import pbkdf2_sha256 as cryp

class Password:
    
    def __init__(self, id, senha, falhas):
        self.__id = id
        self.__senha = cryp.hash(senha, round=20000, salt_size=16)
        self.__senha = falhas