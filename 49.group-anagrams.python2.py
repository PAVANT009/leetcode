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
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        maps = {}
        for x in range(len(strs)):
            sorted_word = "".join(sorted(strs[x]))
            if sorted_word in maps:
                maps[sorted_word].append(strs[x])
            else:
                maps[sorted_word] = [strs[x]]
        ans = []
        for x in maps:
            ans.append(maps[x])
        return ans


# @leet end

