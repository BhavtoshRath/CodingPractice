def hash(astring, tablesize):
    sum = 0
    for char in astring:
        sum += ord(char)

    return sum%tablesize

hash('rath', 7)


class HashTable:
    def __init__(self):
        self.size = 11
        self.map = [None] * self.size


    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list(key_value)
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
            self.map[key_hash].append(key_value)

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] in None:
            return None
        else:
            for i in range(0, len(self.map[key_hash])): # Coz we are popping an index.
                if self.map[key_hash][0] == key:
                    self.map[key_hash].pop(i)
                    return True






# def hash(astring, tablesize):
#     sum = 0
#     for char in astring:
#         sum += ord(char)
#
#     return sum%tablesize
# 
#
# class HashTable:
#     def __init__(self):
#         self.size = 11
#         self.map = [None]*self.size
#
#
#     def _get_hash(self, key):
#         hash = 0
#         for char in str(key):
#             hash += ord(char)
#         return hash % self.size
#
#     def add(self, key, value):
#         key_hash = self._get_hash(key)
#         key_value = [key, value]
#
#         if self.map[key_hash] is None:
#             self.map[key_hash] = list(key_value)
#             return True
#         else:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = value




























































