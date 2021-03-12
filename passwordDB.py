import os
import sys
import shelve
import pyperclip
import Password_chk

if not os.path.exists('D:\\Documents\\Passwords'):
    os.mkdir('D:\\Documents\\Passwords')
os.chdir('D:\\Documents\\Passwords')
db_pass = shelve.open('db')
password_chk = pyperclip.paste()

req_for_chk = input("Do you want to check your password\n-:")
if req_for_chk.lower() == 'yes':

    Password_chk.check_password(password_chk)
    a = input('Press Enter for continue, or print "Exit" for stop app and change your password')
    if a.lower() == 'exit':
        sys.exit()

print("You should use only:\n-save\n-copy\n-show\n for actions with your password\n---")


def ask_for_pass():
    app_attr = input('Print action(key)')
    x = app_attr.split()
    if x[0].lower() == 'exit':
        print('Bye')
        sys.exit()
    return x


def get_data(l):
    if l[0] == 'save':
        db_pass[l[1]] = password_chk
    elif l[0] == 'show':
        for k, i in enumerate(list(db_pass.keys())):
            print(str(k + 1) + ') ' + i)
    elif l[0] == 'copy':

        if l[1] not in db_pass.keys():
            print('Use another key or "show"')
        pyperclip.copy(db_pass[l[1]])
    else:
        raise Exception('''You should use only:
                   -save
                   -copy
                   -show''')

    return get_data(ask_for_pass())


try:

    get_data(ask_for_pass())
except Exception as err:
    print(err)
finally:
    get_data(ask_for_pass())

db_pass.close()
