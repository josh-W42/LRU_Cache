from collections import OrderedDict

class LRU_Cache():

    def __init__(self, capacity):

        # We'll use an OrderedDict to keep items in
        # dictionary-like hash table and also keep track
        # of when they're inserted like a queue.
        if type(capacity) != int:
            raise TypeError('Arg, capacity, must be of type int')

        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key):
        '''
        Retrieves item from cache provided by key.

        Args:
            key: any valid dictionary key.

        Returns:
            Item from the cache dictionary related to key/
            -1 if not found in cache.
         '''
        if key in self.cache:
            self.cache.move_to_end(key)

            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        '''
        Inputs data into the cache. If the cache is at capacity, removes the oldest item.
        
        Args:
            key: dictionary key to be stored
            value: data to be stored in dictionary, related to key
            
            Raises TypeError if either args are of None type.

        '''
        if key is None or value is None:
            raise TypeError('Cannot input type: None')

        if self.cap < 1:
            print("Logical Error: cache capacity is less than 1")
        else: 
            if self.is_at_capacity():
                self.cache.popitem(last = False)

            self.cache[key] = value
            
            
    
    def is_at_capacity(self):
        '''
        Checks if the cache is full or not.

        Returns:
            True if the cache is at capacity
            False otherwise
        '''
        return len(self.cache) == self.cap

def test_suite():
    '''Performs a series of tests on the LRU-cache'''
    
    print('\nRunning set and get Function Tests:\n')

    print('Illogical capacity test: ')

    our_cache = LRU_Cache(0)
    
    our_cache.set(1, 1)

    print('Result: ', end=' ')
    if our_cache.get(1) == -1:
        print('pass')
    else:
        print('Fail')




    our_cache = LRU_Cache(5)
    
    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)
    
    print('\nget Retrevial Test: ', end=' ')
    if our_cache.get(1) == 1 and our_cache.get(2) == 2:
        print('pass')
    else:
        print('Fail')

    print('get invalid input Test: ', end=' ')
    if our_cache.get(9) == -1:
        print('pass')
    else:
        print('Fail')


    print('get Null input Test: ', end=' ')
    if our_cache.get(None) == -1:
        print('pass')
    else:
        print('Fail')

    print('set Null input Test: ', end=' ')
    try:
        our_cache.set(None, 2)
    except TypeError:
        print('pass')
    else:
        print('Fail')


    our_cache.set(5, 5)
    our_cache.set(6, 6)
    
    print('\nLRU Capacity Test 1:', end=' ')
    # Should return -1 because the cache reached it's capacity and 3 was the least recently used entry
    if our_cache.get(3) == -1:
        print('pass')
    else:
        print('Fail')

    our_cache.set(7, 7)
    
    print('LRU Capacity Test 2:', end=' ')
    # 4 is thrown out
    if our_cache.get(4) == -1:
        print('pass')
    else:
        print('Fail')


if __name__ == "__main__":
    test_suite()