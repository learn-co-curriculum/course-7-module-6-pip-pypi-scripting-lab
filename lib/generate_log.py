from datetime import datetime
import requests
import os

def generate_log(data: list):
    if type(data) != list:
        raise ValueError()
    else: 
        file_name = f'log_{datetime.now().strftime('%Y%m%d')}.txt'
        
        with open(file_name, 'w') as file:
            for entry in data:
                file.write(f'{entry}\n')
        
        print(f'File written to {file_name}')

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
    post_data = post.get('body', 'No body found')
    list_data = post_data.split('\n')
    generate_log(list_data)