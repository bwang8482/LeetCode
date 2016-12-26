"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
"""

"""Solution:

Structure:
	1. order list for usage order
	2. dictionary for key and value pair
	3. constant for capacity

Algorith:
	1. Using order list to maintain using order
	2. Using dictionary to keep track of key and value
	3. If capacity is full, remove the first element from order list
	4. remove the key and value from dictionary
"""

"""
Error:
	1. check if key already in map when set
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.order = []
        self.map = {}
        

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.map:
        	return -1
        self.order.remove(key)
        self.order.append(key)
        return self.map[key]

        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
        	num = self.get(key)
        	if num != value:
        		self.map[key] = value
        else:
            if self.length == self.capacity:
            	remove_key = self.order[0]
            	self.order = self.order[1:]
            	self.length -= 1
            	self.map.pop(remove_key, None)
            self.order.append(key)
            self.map[key] = value
            self.length += 1
