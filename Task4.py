import hashlib

hash_url = {}

def check_hash_url(url):
    hashed_url = hashlib.sha512('mysaltword'.encode() + url.encode()).hexdigest()
    if url in hash_url:
        return hashed_url
    else:
        hash_url[url] = hashed_url
        return 'Веб-страница кэширована'

print(check_hash_url('www.ya.ru'))
print(check_hash_url('www.ya.ru'))
print(check_hash_url('www.ya.ru'))
print(check_hash_url('www.google.com'))
