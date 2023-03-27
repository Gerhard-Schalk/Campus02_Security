#print bytes in hexadecimal representation
def print_bytes(_prefix_text, _bytes, _charPerLine = 16):

    print(_prefix_text, end='')
    i = 0
    for b in _bytes:
        print('{0:02X}'.format(b),end=' ')
        if( (i + 1) % _charPerLine == 0 and i != 0):
            print()
            for j in range(len(_prefix_text)):
                print(' ', end='')
        i += 1
    print()

