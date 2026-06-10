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
    def summaryRanges(self, nums):
        if not nums:
            return []

        ans = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    ans.append(str(start))
                else:
                    ans.append("{}->{}".format(start, nums[i - 1]))

                start = nums[i]

        if start == nums[-1]:
            ans.append(str(start))
        else:
            ans.append("{}->{}".format(start, nums[-1]))

        return ans


# @leet end

