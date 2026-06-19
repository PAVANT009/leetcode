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
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        i = 1
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy.next
        if left == 1:
            leftBNode = dummy
            leftNode = curr
        else:
            while True:
                if i == left - 1:
                    leftBNode = curr
                    leftNode = leftBNode.next
                    curr = curr.next
                    i += 1
                    break
                i += 1
                curr = curr.next
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if i == right:
                break
            i += 1
        leftNode.next = curr
        leftBNode.next = prev
        return dummy.next


# @leet end
