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
from typing import List
# @leet imports end


# @leet start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        dummyH = ListNode(0)
        dummyL = ListNode(0)
        high = dummyH
        low = dummyL
        curr = head
        while curr:
            if curr.val < x:
                low.next = ListNode(curr.val)
                low = low.next
            else:
                high.next = ListNode(curr.val)
                high = high.next
            curr = curr.next
        low.next = dummyH.next
        return dummyL.next


# @leet end

