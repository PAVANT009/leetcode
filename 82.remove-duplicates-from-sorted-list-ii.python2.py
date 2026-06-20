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
# Definition for singly-lninked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(200)
        if head is None:
            return dummy.next
        curr = dummy
        init = head
        last = float("inf")
        seen = {}
        while init.next:
            if init.val not in seen and init.val != init.next.val:
                temp = ListNode(init.val)
                curr.next = temp
                curr = curr.next
            seen[init.val] = 0
            last = init.val
            init = init.next
        if init.val != last:
            curr.next = ListNode(init.val)
        return dummy.next


# @leet end

