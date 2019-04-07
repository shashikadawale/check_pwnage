
import requests
from hashlib import sha1
import sys

# Checking user password with the password data fetched from the haveibeenpwned api
def check_password(user_pass):
    user_pass = user_pass
    pass_hash = sha1(user_pass.encode()).hexdigest()
    pass_first_five = pass_hash[:5]
    url = f'https://api.pwnedpasswords.com/range/{pass_first_five}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            pass_data = response.content.decode()

            for line in pass_data.split('\r\n'):
                password, count = line.split(':')
                if pass_hash[5:] == password.lower():
                    print(f'Warning: Your password has been seen {count} times in data breaches.')
                    break
            else:
                print('Your password is safe.')

        else:
            print('Cannot connect to the {url}')
    except Exception as exp:
        print(exp)


if __name__ == '__main__':
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print('usage:\n\npython check_pwned.py <your_password>')
        sys.exit()
    check_password(sys.argv[1])
