def to_str(s):
    return s and chr(int(s[:2], base=16)) + to_str(s[2:]) or ''


# xor two strings with different lengths
def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def show_msgs(str_cipher, str_chg_cipher):
    chg_msg = 'Hackers should be judged by their acting, not bogus criteria.'
    xor_key = strxor(str_chg_cipher, chg_msg)
    for i in str_cipher:
        print(strxor(i, xor_key))
    print(chg_msg)


if __name__ == '__main__':
    # read cipher text
    cipher_text = []
    with open('msg', 'r') as f:
        for line in f:
            temp = ''.join(line.split())
            cipher_text.append(temp)

    # read challenge cipher text
    chg_cipher_text = open('msg_challenge', 'r').read()
    chg_cipher_text = ''.join(chg_cipher_text.split())

    # turn text from ascii hex to string
    str_cipher_text = []
    for i in cipher_text:
        str_cipher_text.append(to_str(i))
        # str_cipher_text.append(bytearray.fromhex(i).decode())
    str_chg_cipher_text = to_str(chg_cipher_text)
