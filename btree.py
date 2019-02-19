
def to_hex(num):
    return list("".join(hex(num).split("0x")))

class Node(object):
    

if __name__ == '__main__':
    # binary str to int
    print(int('f', 16)) ## 0 0 0 0 0 0 0 0
    # char to binary
    for i in range(ord('a'), ord('b')):
        print(format(ord(chr(i)), 'b'), chr(i))
    # int to binary
    x = 255
    print(to_hex(x))