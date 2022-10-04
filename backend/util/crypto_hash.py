import hashlib
import json

"""
def stringify(data):
    # necessary if any of the args are not a string e.g. int or float
    return json.dumps(data)
"""


def crypto_hash(*args):
    # returns sha-256 hash of given arguments, * indicates many, but unknow how may
    #stringifiedargs = map(stringify, args)
    # next line replaces the stringify function above
    stringifiedargs = sorted(map(lambda data: json.dumps(data), args))
    #print(f'stringified_args: {stringifiedargs}')
    joined_data = ''.join(stringifiedargs)
    #print(f'joined_data: {joined_data}')
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()


def main():
    print(f"crypto_hash('foo'): {crypto_hash('foo')}")
    print(f"crypto_hash(2): {crypto_hash(2)}")
    print(f"crypto_hash('one', 2, [3, 4]): {crypto_hash('one', 2, [3, 4])}")

      
if __name__ == '__main__':
    # for testing
    main()