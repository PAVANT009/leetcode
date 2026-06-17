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
from typing import NoDefault
# @leet imports end

# @leet start
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        dummy = Node(0)
        currentn = dummy
        p1 = head
        hash = {}
        while p1:
            hash[p1] = Node(p1.val)
            p1 = p1.next
        p1 = head
        while p1:
            currentn = hash[p1]
            if p1.next:
                nextn = hash[p1.next]
                currentn.next = nextn
            randomn = None
            if p1.random != None:
                randomn = hash[p1.random]
            currentn.random = randomn
            p1 = p1.next
        return hash[head]


# @leet end

