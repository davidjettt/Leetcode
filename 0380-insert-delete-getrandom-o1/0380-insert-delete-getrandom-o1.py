import random
class RandomizedSet:
    '''
    '''
    def __init__(self):
        self.arr = []
        self.hashmap = {} #{val: idx}

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.arr)
            self.arr.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            last_value = self.arr[-1]

            # overwrite in array
            self.arr[idx] = last_value
            self.arr.pop()

            # overwrite in hashmap
            self.hashmap[last_value] = idx
            del self.hashmap[val]

            return True
        else:
            return False
        

    def getRandom(self) -> int:
        # rand_idx = random.randint(0, len(self.arr) - 1)
        # return self.arr[rand_idx]
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()