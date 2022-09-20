import hashlib

string = 'papa'
under_strings = []
strings = []

for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        if string[i:j] != string:
            strings.append(string[i:j])
            under_strings.append(hashlib.sha256(string[i:j].encode()).hexdigest())

print(len(set(under_strings)))
print(set(strings))
