import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from time import sleep
from stem import Signal
from stem.control import Controller
import os
import sys

def init_useragent():
    return UserAgent()

def init_hash_list():
    hash_file = open('/Users/omega/Documents/work/vda/texas_bank/dehashed/hashes.txt', 'r')
    file = hash_file.readlines()
    numbers = [line.strip() for line in file]
    hash_chunks = [numbers[i:i + 25] for i in range(0, len(numbers), 25)]
    return hash_chunks
    # hash_file = open(sys.argv[1], 'r')

def create_session(ua):
    session = requests.session()
    session.proxies = {}
    session.proxies['http'] = 'socks5://127.0.0.1:9050'
    session.proxies['https'] = 'socks5://127.0.0.1:9050'
    headers = {"Connection": "close", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
               "Origin": "https://hashes.com", "Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": ua.random,
               # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               # "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
               # "Sec-Fetch-Dest": "document", "Referer": "https://hashes.com/en/decrypt/hash",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}
    session.cookies.clear()
    return session, headers

def make_request(session, raw_hashes, headers):
    data = {"hashes": raw_hashes, "vyd": "64", "submitted": "true"}
    data_raw = session.post(hashes_com_url, headers=headers, data=data)
    data = data_raw.content
    return data

def reset_session(raw_hashes):
    switchIP()
    session, headers = create_session(init_useragent())
    data = make_request(session, raw_hashes, headers)
    filter_hashes(data, raw_hashes)

def filter_hashes(data, raw_hashes):
    soup = BeautifulSoup(data, 'html.parser')
    mydivs = soup.findAll("div", {"class": "py-1"})
    if 'Invalid captcha.' in data.decode('utf-8'):
        print('[-] Blocked by captcha, retrying...')
        reset_session(raw_hashes)
    else:
        for hash in mydivs:
            hash = str(hash)
            combo = hash.split('>')[1].split('<')[0]
            all_cracked.append(combo)
        print('[+] Success! Returned ' + str(len(mydivs)) + ' passwords!')

def switchIP():
    print('[+] Restarting TOR...')
    os.system('brew services restart tor > /dev/null')
    sleep(10)
    proxies = {
        'http': 'socks5://localhost:9050',
        'https': 'socks5://localhost:9050'}
    url = 'https://api.ipify.org'
    ip = requests.get(url, proxies=proxies).text
    print('[+] Done! New IP: ' + ip)

def send_hashes():
    ua = init_useragent()
    hash_chunks = init_hash_list()
    for hash_list in hash_chunks:
        switchIP()
        print('[+] Sending ' + str(len(hash_list)) + ' hashes...')
        session, headers = create_session(ua)
        raw_hashes = "\r\n".join(hash_list)
        data = make_request(session, raw_hashes, headers)
        filter_hashes(data, raw_hashes)

def display_hashes():
    print('[+] Cracked ' + str(len(all_cracked)) + ' hashes:')
    for combo in all_cracked:
        print(combo)

if __name__ == '__main__':
    all_cracked = []
    hashes_com_url = "https://hashes.com:443/en/decrypt/hash"
    send_hashes()
    display_hashes()