import os
from base64 import b64decode

def main():
    key = os.environ.get('SERVICE_ACCOUNT_KEY')
    with open('path.json','w') as json_file:
        json_file.write(b64decode(key).decode())
    print(os.path.realpath('path.json'))

if __name__ == '__main__':
    main()