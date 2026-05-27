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
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapw = {}
        maps = {}

        for x in range(len(pattern)):
            a = pattern[x]
            b = words[x]
            if a in mapw and mapw[a] != b:
                return False
            if b in maps and maps[b] != a:
                return False
            mapw[a] = b
            maps[b] = a
        return True


# @leet end
