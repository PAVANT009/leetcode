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
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapS = {}
        mapT = {}
        length = len(s)
        for x in range(length):
            a = s[x]
            b = t[x]

            if a in mapS and mapS[a] != b:
                return False
            if b in mapT and mapT[b] != a:
                return False

            mapS[a] = b
            mapT[b] = a
        return True


# @leet end

