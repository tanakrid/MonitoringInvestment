# from project import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)


from sqlalchemy import create_engine

# Replace 'mysecretpassword' with the password you set in Step 3


db_host = 'localhost'
db_port = '5432'
db_name = 'postgres'
db_user = 'postgres'
db_password = 'lwpjtylla6EhcZ8r5Gmu'
db_endpoint = 'sit-pfm-db.cyrgkvmfx5v1.ap-southeast-1.rds.amazonaws.com'

# Create the database URL for SQLAlchemy
db_url = f'postgresql://{db_user}:{db_password}@{db_endpoint}:{db_port}/{db_name}'
print(db_url)

# Create the SQLAlchemy engine
engine = create_engine(db_url)

# Test the connection
connection = engine.connect()
result = connection.execute('SELECT 1')
for row in result:
    print(row[0])

# Close the connection
connection.close()
