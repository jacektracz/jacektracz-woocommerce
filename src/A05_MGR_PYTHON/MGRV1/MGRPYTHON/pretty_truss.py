import fileinput
import sys
import string
import re

def parse_char(c):
    if c.startswith('\\'):
        c = c.decode('string_escape')
    elif c.startswith(' '):
        c = c[1]
    else:
        c = c.decode('hex')
    return c

PRINTABLE_CHARACTERS = set(string.digits + string.letters + string.punctuation)

def quotechars(chars):
    return "".join(c if c in PRINTABLE_CHARACTERS else '.' for c in chars)

def hexdump(chars, sep=' ', width=16):
    while chars:
        line = chars[:width]
        chars = chars[width:]
        yield "%-*s%s%s" % (width * 3, sep.join("%02x" % ord(c) for c in line), sep, quotechars(line))

def format_hexdump(bin_id, binary):
    for b in hexdump("".join(binary)):
        yield "%s\t  %s" % (bin_id, b)

def prettify_truss(data):
    parsing_binary = False
    binary = []
    bin_id = ""
    for line in data:
        line = line.rstrip('\n')
        try:
            id, details = line.split('\t', 1)
        except ValueError:
            if line:
                yield line
            continue
        command = ""
        r = re.match('^(\w+)\(', details)
        if r:
            #line with command
            command = r.group(1)
            if binary:
                for b in format_hexdump(bin_id, binary):
                    yield b
                binary = []
            #enter parse binary mode if one of the commands found
            parsing_binary = command in ('read', 'write', 'send', 'recv')
            yield "%s\t%s" % (id, details)
        elif parsing_binary and details.startswith('  '):
            #line with binary output
            #xrange from 2 because truss indents binary content by 2 spaces
            d = "".join(parse_char(details[i:i+2]) for i in xrange(2, len(line), 2))
            binary.append(d)
            bin_id = id
        else:
            #everything else
            yield "%s\t%s" % (id, details)
    if binary:
        for b in format_hexdump(bin_id, binary):
            yield b
    

if __name__ == '__main__':
    data = prettify_truss(fileinput.input())
    for line in data:
        print line
