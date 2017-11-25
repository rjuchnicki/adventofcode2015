import re
import string

alph = string.ascii_lowercase

def is_valid(password):
    if len(re.findall(r'(\w)\1', password)) < 2:
        return False
    if any(c in 'iol' for c in password):
        return False
    has_straight = False
    for i in range(0, len(password)-3):
        if password[i:i+3] in alph:
            has_straight = True
            break

    return has_straight

assert not is_valid('hijklmmn')
assert not is_valid('abbceffg')
assert not is_valid('abbcegjk')
assert is_valid('abcdffaa')
assert is_valid('ghjaabcc')

def inc_pass(password):
    mod = ord('z')
    new_pass = password
    for i in range(len(new_pass)-1, -1, -1):
        if ord(new_pass[i])%mod == 0:
            new_pass = new_pass[0:i] + 'a' + new_pass[i+1:]
        else:
            new_pass = new_pass[0:i] + chr(ord(new_pass[i])+1) + new_pass[i+1:]
            break
    return new_pass

def next_valid(password):
    while not is_valid(password):
        password = inc_pass(password)
    return password

password = 'cqjxjnds'
password = next_valid(password)
print(password)

# Find the following valid password
password = inc_pass(password)
print(next_valid(password))
