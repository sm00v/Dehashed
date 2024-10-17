#!/usr/bin/env python3

import json
import requests
import argparse
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from time import sleep
import os
import sys

dehashed_api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' #Hardcode API key if you so choose
dehashed_username = 'XXXXXXXXXXXXXXXXXXX' #Hardcode email if you so choose
dehashed_default = 'dehashed'

parser = argparse.ArgumentParser()
parser.add_argument('-a', dest='api_key', nargs='?', default=dehashed_api_key, const=dehashed_api_key,
                    help='Use your dehashed.com API key to query domain.')
parser.add_argument('-u', action='store', nargs='?', dest='username', default=dehashed_username, const=dehashed_username,
                    help='Use your dehashed.com username to auth to API.')
parser.add_argument('-d', action='store', dest='domain',
                    help='Target domain to search dehashed.com for.')
parser.add_argument('-f', action='store', dest='dehashed_data_file',
                    help='Read json data from previously saved API query.')
parser.add_argument('-o', action='store', dest='dehashed_file', nargs='?', const=dehashed_default,
                    help='Stores all hashes and cracked passwords in files. [dehashed_*.txt]')
parser.add_argument('--version', action='version', version='%(prog)s 1337.1')
args = parser.parse_args()

def check_api_auth_success(dehashed_json_raw):
    check_success = json.loads(dehashed_json_raw)
    if check_success.get('success') == False:
        sys.exit('[-] API Authentication Failure.')
    else:
        pass

def query_dehashed_domain():
    headers = {'Accept': 'application/json',}
    params = (('query', 'domain:' + args.domain),)
    dehashed_json_raw = requests.get('https://api.dehashed.com/search',
                            headers=headers,
                            params=params,
                            auth=(args.username, args.api_key)).text
    check_api_auth_success(dehashed_json_raw)
    dehashed_json = jsonify_data(dehashed_json_raw)
    return dehashed_json

def jsonify_data(json_raw_data):
    json_data = json.loads(json_raw_data)
    entries = json_data['entries']
    return entries

def filter_entries():
    for entry in entries:
        email = entry['email']
        # username = entry['username']
        password = entry['password']
        hash = entry['hashed_password']
        if len(password) >= 1:
            combo = email,password
            password_combos.append(combo)
        elif len(hash) >= 1:
            combo = email,hash
            hash_combos.append(combo)
        else:
            pass

def output():
    print('[+] Cleartext Passwords {email:password}')
    bool = False
    try:
        cracked=open(args.dehashed_file + '_cracked.txt', 'a') #These are set to false by default in case user does not want to save output to file
        hashes=open(args.dehashed_file + '_hashes.txt', 'a')
        bool = True
    except Exception as e:
        print('[-] Did not save.')
    for combo in password_combos:
        combo_raw = combo[0] + ':' + combo[1]
        print(combo_raw)
        try:
            cracked.write(combo_raw)
            cracked.write('\n')
        except Exception as e:
            pass
    print('\n\n[+] Hashed Passwords {email:hash}')
    for combo in hash_combos:
        combo_raw = combo[0] + ':' + combo[1]
        try:
            hashes.write(combo_raw)
            hashes.write('\n')
        except Exception as e:
            pass
        print(combo_raw)
    print('\n\n[+] Raw Hashes to Copy/Paste then crack >:)')
    for combo in hash_combos:
        print(combo[1])
    if bool:
        print('\n[+] Cracked passwords written to ' + args.dehashed_file + '_cracked.txt')
        print('[+] Hashes written to ' + args.dehashed_file + '_hashes.txt')
    else:
        print('[+] Done!')

def check_data_returned(entries):
    try:
        for x in entries:
            pass
    except TypeError:
        sys.exit('[-] No data returned. Probably error in syntax.')

def control_flow():
    if args.dehashed_data_file:
        try:
            print('[+] Parsing Dehashed output file...')
            json_raw_data = open(args.dehashed_data_file, 'r')
            json_data = json.loads(json_raw_data.read())
            entries = json_data['entries']
            check_data_returned(entries)
            return entries
        except json.decoder.JSONDecodeError:
            sys.exit('[-] Failed to import JSON file.')
    elif args.api_key and args.domain and args.username:
        print('[+] Querying Dehashed for all entries under domain: ' + args.domain + '...')
        entries = query_dehashed_domain()
        return entries
    else:
        sys.exit('[-] Missing argument, exiting.')

if __name__ == '__main__':
    entries = control_flow()
    hash_combos = []
    password_combos = []
    filter_entries()
    output()
