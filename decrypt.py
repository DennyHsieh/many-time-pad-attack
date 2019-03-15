def to_str(s):
    return s and chr(int(s[:2], base=16)) + to_str(s[2:]) or ''


# xor two strings with different lengths
# Note: a XOR b in python: chr(ord(a) ^ ord(b))
def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def show_msgs(str_ciphers, str_chg_cipher):
    chg_msg = 'Hackers should be judged by their acting, not bogus criteria.'
    xor_key = strxor(str_chg_cipher, chg_msg)
    for str_cipher in str_ciphers:
        print(strxor(str_cipher, xor_key))
    print(chg_msg)


if __name__ == '__main__':
    # read cipher text in array []
    cipher_text = []
    with open('msg', 'r') as f:
        for line in f:
            temp = ''.join(line.split())
            cipher_text.append(temp)

    # read challenge cipher text in string (hex) ''
    chg_cipher_text = open('msg_challenge', 'r').read()
    chg_cipher_text = ''.join(chg_cipher_text.split())

    # turn text from ASCII hex to string
    str_cipher_text = []
    for text in cipher_text:
        str_cipher_text.append(to_str(text))
        # str_cipher_text.append(bytearray.fromhex(text).decode())
    str_chg_cipher_text = to_str(chg_cipher_text)

    # try each possible alphabetic in challenge cipher string by XOR cipher strings
    results = []
    for i in range(len(str_chg_cipher_text)):
        chars = []
        for j in range(len(str_cipher_text)):
            len_cipher_j = len(str_cipher_text[j])
            # jump out the loop if ith alphabetic of challenge cipher is longer than cipher string
            if i >= len_cipher_j:
                continue

            '''
            XOR challenge cipher text with other cipher text. If lower alphabetic from challenge cipher text meets space 
            from other cipher text, it will be showed in same upper alphabetic. Also, The upper alphabetic will be 
            showed in same lower alphabetic.
            '''
            char = (chr(ord(str_cipher_text[j][i:i + 1]) ^ ord(str_chg_cipher_text[i:i + 1])))

            # if ASCII HEX is from A to z, XOR with space to get the real alphabetic
            if 'A' <= char <= 'z':
                new_char = chr(ord(char) ^ ord(' '))
                if new_char not in chars:
                    chars.append(new_char)

        results.append(chars)

    '''
    If the array is empty [], that is, neither msg_1 nor msg_2 has space, any alphabetic is possible.
    If the array appears above 5 alphabetic, the challenge cipher text is space or other symbols in this part.
    '''
    # print all possible alphabetic
    for chg_char in results:
        print(chg_char)

    # print all decrypted original messages
    show_msgs(str_cipher_text, str_chg_cipher_text)
