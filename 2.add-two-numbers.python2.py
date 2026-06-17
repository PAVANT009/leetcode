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
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = ""
        num2 = ""
        p1 = l1
        p2 = l2
        while True:
            num1 = str(p1.val) + num1
            if p1.next:
                p1 = p1.next
            else:
                break
        while True:
            num2 = str(p2.val) + num2
            if p2.next:
                p2 = p2.next
            else:
                break
        result = int(num1) + int(num2)
        dummy = ListNode(0)
        current = dummy
        reversed = str(result)[::-1]
        for x in reversed:
            current.next = ListNode(int(x))
            current = current.next
        return dummy.next


# @leet end

