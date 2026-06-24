# @leet imports start
from bisect import *
from collections import *
from copy import *
from datetime import *
from heapq import *
from math import *
from re import *
from string import *
from random import *
from itertools import *
from functools import *
from operator import *
import string
import re
import datetime
import collections
import heapq
import bisect
import copy
import math
import random
import itertools
import functools
import operator
# @leet imports end


# @leet start
class Node(object):
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.prev_map = {}  # key -> previous node
        self.head = Node()  # dummy head
        self.tail = self.head  # tail of singly linked list

    def _move_to_tail(self, key):
        prev = self.prev_map[key]
        node = prev.next

        if node == self.tail:
            return node

        prev.next = node.next
        if node.next:
            self.prev_map[node.next.key] = prev

        self.tail.next = node
        self.prev_map[node.key] = self.tail
        self.tail = node
        node.next = None

        return node

    def get(self, key):
        if key not in self.prev_map:
            return -1

        node = self._move_to_tail(key)
        return node.val

    def put(self, key, value):
        if key in self.prev_map:
            node = self._move_to_tail(key)
            node.val = value
            return

        node = Node(key, value)
        self.tail.next = node
        self.prev_map[key] = self.tail
        self.tail = node

        if len(self.prev_map) > self.capacity:
            lru = self.head.next
            self.head.next = lru.next
            del self.prev_map[lru.key]

            if self.head.next:
                self.prev_map[self.head.next.key] = self.head
            else:
                self.tail = self.head


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @leet end

