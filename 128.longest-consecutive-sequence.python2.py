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
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                # num is the start
                current = num
                length = 1

                while current + 1 in nums_set:
                    current += 1
                    length += 1
                if max_length < length:
                    max_length = length
        return max_length


# @leet end

