#!/usr/bin/python3

import os
import sys
import requests

API_URL = 'https://sm.ms/api/v2'
TOKEN_URL = f'{API_URL}/token'
PROFILE_URL = f'{API_URL}/profile'
CLEAR_URL = f'{API_URL}/clear'
HISTORY_URL = f'{API_URL}/history'
DELETE_URL = f'{API_URL}/delete'
UPLOAD_HISTORY_URL = f'{API_URL}/upload_history'
UPLOAD_URL = f'{API_URL}/upload'

ALBUMS = f'{API_URL}/albums'

__HEADERS = {'user-agent': 'smms/0.0.1'}


def f_token(username, password):
    resp = requests.post(TOKEN_URL, headers=__HEADERS, data={
                         'username': username, 'password': password})
    result = resp.json()
    print(result)
    return result


def f_profile(token):
    resp = requests.post(PROFILE_URL, headers={
                         **__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_clear():
    resp = requests.get(CLEAR_URL, headers=__HEADERS)
    result = resp.json()
    print(result)
    return result


def f_history():
    resp = requests.get(HISTORY_URL, headers=__HEADERS)
    result = resp.json()
    print(result)
    return result


def f_delete(token, hash):
    resp = requests.get(f'{DELETE_URL}/{hash}',
                        headers={**__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_upload_history(token):
    resp = requests.get(UPLOAD_HISTORY_URL, headers={
                        **__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_upload(token, file):
    with open(file, 'rb') as f:
        resp = requests.post(UPLOAD_URL, headers={
                             **__HEADERS, 'Authorization': token}, files={'smfile': f})
        f.close()
        result = resp.json()
        print(result)
        return result


def f_albums_create(token, album_name, album_description):
    resp = requests.post(ALBUMS, headers={**__HEADERS, 'Authorization': token}, data={
                         'album_name': album_name, 'album_description': album_description})
    result = resp.json()
    print(result)
    return result


def f_albums_delete(token, album_id):
    resp = requests.get(f'{ALBUMS}/{album_id}/delete',
                        headers={**__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_albums_add_item(token, album_id, hash):
    resp = requests.get(f'{ALBUMS}/{album_id}/item', headers={**
                                                              __HEADERS, 'Authorization': token}, params={'add': hash})
    result = resp.json()
    print(result)
    return result


def f_albums_remove_item(token, album_id, hash):
    resp = requests.get(f'{ALBUMS}/{album_id}/item', headers={**
                                                              __HEADERS, 'Authorization': token}, params={'remove': hash})
    result = resp.json()
    print(result)
    return result


def f_albums_items(token, album_id):
    resp = requests.get(f'{ALBUMS}/{album_id}',
                        headers={**__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_albums(token):
    resp = requests.get(f'{ALBUMS}', headers={
                        **__HEADERS, 'Authorization': token})
    result = resp.json()
    print(result)
    return result


def f_upload_ext(token, files):
    results = []
    for file in files:
        real_file = file
        result = f_upload(token, real_file)
        results.append(result)

    print('upload images url list:')
    for result in results:
        if result['success']:
            print(result['data']['url'])
        if result['code'] == 'image_repeated':
            print(result['images'])


def main(argv):
    if(len(argv) < 1):
        print('smms command [token] [params]')
        sys.exit(1)
    command = argv[0]
    if command == 'upload':
        f_upload_ext(argv[1], files=argv[2:])
    elif command == 'token':
        f_token(argv[1], argv[2])
    elif command == 'profile':
        f_profile(argv[1])
    elif command == 'clear':
        f_clear()
    elif command == 'history':
        f_history()
    elif command == 'delete':
        f_delete(argv[1], argv[2])
    elif command == 'upload_history':
        f_upload_history(argv[1])
    elif command == 'albums_create':
        f_albums_create(argv[1], argv[2], argv[3])
    elif command == 'albums_delete':
        f_albums_delete(argv[1], argv[2])
    elif command == 'albums_add_item':
        f_albums_add_item(argv[1], argv[2], argv[3])
    elif command == 'albums_remove_item':
        f_albums_remove_item(argv[1], argv[2], argv[3])
    elif command == 'albums_items':
        f_albums_items(argv[1], argv[2])
    elif command == 'albums':
        f_albums(argv[1])
    else:
        print('not supported command %s' % command)


if __name__ == '__main__':
    main(sys.argv[1:])
