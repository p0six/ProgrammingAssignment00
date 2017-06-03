#!/usr/bin/env python
import sys
import string


def usage(script_name):
    msg = 'Usage: %s FILE' % script_name
    sys.exit(msg)


def main(file_name):
    with open(file_name) as f:
        for clear_text in f:
            ascii = map(ord, clear_text.rstrip('\n'))
            cipher = [c - 1 for c in ascii]
            cipher_text = map(chr, cipher)
            print string.join(cipher_text, '')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage(sys.argv[0])
    main(sys.argv[1])