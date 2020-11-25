#!/usr/bin/python3

import os,sys
import requests

API_URL = 'https://sm.ms/api/v2/'
UPLOAD_URL = f'{API_URL}upload'

def upload(token, files):
    headers = {'user-agent': 'smms/0.0.1', 'Authorization': token}
    for file in files:
        real_file = file
        with open(real_file, 'rb') as f:
            resp = requests.post(UPLOAD_URL, headers=headers, files={'smfile': f})
            f.close()
            result = resp.json()
            
            # print(result)
            if result['success']:
                print(result['data']['url'])
                return
            if result['code'] == 'image_repeated':
                print(result['images'])

def main(argv):
    if(len(argv) < 2):
        print('smms command token [files]')
        sys.exit()
    command = argv[0]
    token = argv[1]
    if command == 'upload':
        upload(token, files = argv[2:])
    else:
        print('not supported command %s' % command)

if __name__ == '__main__':
    main(sys.argv[1:])