# ScrubEncoder
dehashed.py is a  <a href="https://dehashed.com">dehashed.com</a> query tool which only queries 'domain' as of now. It will output the gathered cleartext passwords and hashes to a file.
hash_crack.py will send all the specified hashes to <a href="https://hashes.com">hashes.com</a> in attempt to crack the hash. It will then return all cracked passwords.

dehashed.py usage:
```
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
```

Example Output of dehashed.py:
```
python3 dehashed.py -d domain.com -o
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
```
