import json

def byte_to_object(data_byte):
    data_str = data_byte.decode('utf-8')  # Decode the bytes to a string
    data_obj = json.loads(data_str) 
    return data_obj