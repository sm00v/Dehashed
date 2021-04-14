# Dehashed Query and Crack
1: <b>dehashed.py</b> is a  <a href="https://dehashed.com">dehashed.com</a> query tool which only queries 'domain' as of now. It will output the gathered cleartext passwords and hashes to a file.

2: <b>hash_crack.py</b> will send all the specified hashes to <a href="https://hashes.com">hashes.com</a> in attempt to crack the hash. It will then return all cracked passwords.

## 1: dehashed.py usage:
   usage: dehashed.py [-h] [-a [API_KEY]] [-u [USERNAME]] [-d DOMAIN] [-f DEHASHED_DATA_FILE] [-o [DEHASHED_FILE]] [--version]

    optional arguments:
      -h, --help            show this help message and exit
      -a [API_KEY]          Use your dehashed.com API key to query domain.
      -u [USERNAME]         Use your dehashed.com username to auth to API.
      -d DOMAIN             Target domain to search dehashed.com for.
      -f DEHASHED_DATA_FILE
                            Read json data from previously saved API query.
      -o [DEHASHED_FILE]    Stores all hashes and cracked passwords in files. [dehashed_*.txt]
      --version             show program's version number and exit

   dehashed.py usage [parse saved query in json format]:
   
    python3 dehashed.py -f previous_query.json
    
   dehashed.py usage [hardcoded dehashed email and api key]:
   
    python3 dehashed.py -d domain.com -o output_file.txt
    
   dehashed.py usage [non-hardcoded dehashed credentials]:
   
    python3 dehashed.py -o -d domain.com -a API-KEY -u user@domain.com

   Example Output of dehashed.py:
   
    $ python3 dehashed.py -d domain.com -o
    [+] Querying Dehashed for all entries under domain: domain.com...
    [+] Cleartext Passwords {email:password}
    brady@domain.com:password1
    copper@domain.com:summer1999

    [+] Hashed Passwords {email:hash}
    sam@domain.com:$2a$08$K2YzRKMF7sVlHwIwuGsqUuJ5B1Q0CG3RZzO1pectKlytIbVmKra4q
    tom@domain.com:22c212f0d123a3a031aa063f85800be2

    [+] Raw Hashes to Copy/Paste then crack >:)
    $2a$08$K2YzRKMF7sVlHwIwuGsqUuJ5B1Q0CG3RZzO1pectKlytIbVmKra4q
    22c212f0d123a3a031aa063f85800be2

    [+] Cracked passwords written to dehashed_cracked.txt
    [+] Hashes written to dehashed_hashes.txt

## 2: hash_crack.py usage:
```
usage: hash_crack.py [-h] [-f [HASHES]]

optional arguments:
  -h, --help   show this help message and exit
  -f [HASHES]  Input any hash file separated by newline in format {email:hash}.
```
   No file specified will search for direct output from dehashed.py {dehashed_hashes.txt}:

    python3 hash_crack.py -f
   Injest any hash file in format {email:hash}:

    python3 hash_crack.py -f hash_file.txt
    
   Example Output of hash_crack.py:
   
    $python3 hash_crack.py -f
    [+] Restarting TOR...
    [+] Done! New IP: 185.220.101.197
    [+] Sending 8 hashes...
    [-] Blocked by captcha, retrying...
    [+] Restarting TOR...
    [+] Done! New IP: 51.158.111.157
    [-] Blocked by captcha, retrying...
    [+] Restarting TOR...
    [+] Done! New IP: 104.244.72.36
    [-] Blocked by captcha, retrying...
    [+] Restarting TOR...
    [+] Done! New IP: 89.234.157.254
    [-] Blocked by captcha, retrying...
    [+] Restarting TOR...
    [+] Done! New IP: 91.203.146.126
    [+] Success! Returned 8 passwords!
    [+] Cracked 8 hashes:
    29be83ff7eedd5ecf5807b6729ef69d237faaf3e:910299329
    3bdd449dc37efc759e40729c1a071f8084a3d047:ramazo
    3eae40ad01eeb72d23f64c60e255bc567b2ee837:kek22
    47eab33b590d3df5b378c1ab3eba83cae44201c4:whoami
    7f1d3f91b56b396073d893d8fe2c78c0f0ee95ba:fake@@#
    c19c95e405b41f88889bf9810c81a5b39fbdb905:asdff
    e3e0fc2183c4313a89ddd5355d96770e90b61e7c:10291
    22c212f0d123a3a031aa063f85800be2:panda2993
