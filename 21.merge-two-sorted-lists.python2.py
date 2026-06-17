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
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = list1
        p2 = list2
        dummy = ListNode(0)
        current = dummy
        while True:
            if not p1 and not p2:
                break
            elif p1 and not p2:
                current.next = p1
                break
            elif not p1 and p2:
                current.next = p2
                break
            else:
                if p1 and p2:
                    if p1.val <= p2.val:
                        current.next = ListNode(p1.val)
                        if p1:
                            p1 = p1.next
                    else:
                        current.next = ListNode(p2.val)
                        if p2:
                            p2 = p2.next
            current = current.next
        return dummy.next


# @leet end

