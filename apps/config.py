DB = 'mysql'
DRIVER = 'pymysql'
NAME = 'root'
PWD = '123'
HOST = 'localhost'
PORT = 3306
DB_NAME = 'flask_demo'
CHARSET = 'utf8'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(DB, DRIVER, NAME, PWD, HOST, PORT, DB_NAME,
                                                                     CHARSET)
SQLALCHEMY_TRACK_MODIFICATIONS = False
