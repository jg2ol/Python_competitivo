# Hash Table -> dicionário que guarda strings com mesmo valor ASCII e seus respectivos values (strings)

class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, key):
        result = 0
        for char in key:
            result += ord(char)
        return result

    def add(self, key, value):
        hash_key = self.hash(key)
        if hash_key not in self.collection.keys():
            self.collection[hash_key] = {key: value}
        else:
            self.collection[hash_key][key] = value
    
    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection.keys():
            del self.collection[hash_key][key]
        else:
            return
    
    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key not in self.collection.keys() or key not in self.collection[hash_key].keys():
            return None
        else:
            return self.collection[hash_key][key]
