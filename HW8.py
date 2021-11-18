import hashlib


def counter(string):

    string = str(string).lower()

    length = len(string)

    hash_set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            h = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)

    return len(hash_set)


a = 'Thanks for the lecture!'

print(f'Количество различных подстрок в строке {a}: {counter(a)}')