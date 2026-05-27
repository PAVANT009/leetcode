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
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        mapn = {}
        curr = n
        while curr > 1:
            Total = 0
            while curr > 0:
                digit = curr % 10
                Total += digit**2
                curr = curr // 10
            if Total == 1:
                return True
            elif Total in mapn:
                return False
            else:
                mapn[Total] = 0
            curr = Total


# @leet end

