DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'keeplearning'
DB_USER = 'root'
DB_PASSWORD = 'keep1234'
DB_ECHO_MODE = True

# 'sqlite:///mydatabase.db' 
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'