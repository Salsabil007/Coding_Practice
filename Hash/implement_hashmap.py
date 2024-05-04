class hashtable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def set_val(self, key, value):
        ind = hash(key) % self.size
        tab = self.table[ind]

        found = False
        for i,record in enumerate(tab):
            rkey, rval = record
            if rkey == key:
                found = True
                break
        if found == True:
            tab[i] = (key, value)
        else:
            tab.append((key,value))

        return

    def get_val(self, key):
        ind = hash(key) % self.size
        tab = self.table[ind]

        found = False
        for i,record in enumerate(tab):
            rkey, rval = record
            if rkey == key:
                found = True
                break

        if found == True:
            rkey, rval = record
            return rval
        else:
            return "No record found"
        
    def delete_val(self, key):
        ind = hash(key) % self.size
        tab = self.table[ind]

        found = False
        for i,record in enumerate(tab):
            rkey, rval = record
            if rkey == key:
                found = True
                break
        if found == True:
            tab.pop(i)

        return
    
    def __str__(self):
        return "".join(str(item) for item in self.table)

hash_table = hashtable(5)
 
# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()
 
hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()
 
# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()
 
# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)

