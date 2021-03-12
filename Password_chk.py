import requests
import hashlib


# App allows you to find if your password was hacked

# Send 5 first symbols and request from pwnedpassword
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    return res


# Split response for tail and number how often your password is meet
def read_res(hashes, hash_to_chk):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_chk:
            return count
    return 0


# Hashing your password and take 5 first symbols to transmit
def password_for_request(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_char, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first_char)
    return read_res(response, tail)


def check_password(*args):
    for password in args:
        count = password_for_request(password)
        if count:
            print(f'{password} was found {count} times.\nYou should change it')
        else:
            print(f"{password} wasn't found.")


if __name__ == '__main__':
    check_password('12345678')
