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
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        maps = {}
        for x in s:
            if x in maps:
                maps[x] += 1
                continue
            maps[x] = 1
        for y in t:
            if y in maps and maps[y] > 0:
                maps[y] -= 1
            else:
                return False
        return True


# @leet end
