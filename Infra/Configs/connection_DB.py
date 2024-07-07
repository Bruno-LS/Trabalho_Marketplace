from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def carrega_Env():
    load_dotenv()
    USER_NAME = os.getenv('USER_NAME')
    BD_NAME = os.getenv('BD_NAME')
    DRIVER_NAME = os.getenv('DRIVER_NAME')

    connection_string = "mssql+pyodbc://{}/{}?driver={}".format(USER_NAME, BD_NAME, DRIVER_NAME)

    return connection_string


# noinspection PyStatementEffect
class DBconnection:

    def __init__(self):
        self.__connection_string = carrega_Env()
        self.__engine = self.__create_database_engine()
        self.session = self.__create_session()


    def __create_database_engine(self):
        engine = create_engine(self.__connection_string, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    def __create_session(self):
        session_make = sessionmaker(bind=self.__engine)
        session = session_make()
        return session

    def __enter__(self):
        if self.session is None:
            self.session = self.__create_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
