# duplicate_finder.py
import os, hashlib

def hash_file(path):
    h = hashlib.md5()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

def find_duplicates(folder):
    hashes = {}
    duplicates = []
    for root, dirs, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            file_hash = hash_file(path)
            if file_hash in hashes:
                duplicates.append((path, hashes[file_hash]))
            else:
                hashes[file_hash] = path
    return duplicates

folder = input("Pasta pra checar: ")
dupes = find_duplicates(folder)
if dupes:
    print("Duplicados encontrados:")
    for f1, f2 in dupes:
        print(f"{f1} == {f2}")
else:
    print("Nenhum duplicado encontrado")
