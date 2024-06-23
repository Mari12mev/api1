import hashlib 
from virus_total_apis import publicapi

api_key = 'plural'
api = publicapi(api_key)

with open ("biblioteca.txt","rb") as file
    file_hash - hashlib.md5(file.read()).hexdigest()