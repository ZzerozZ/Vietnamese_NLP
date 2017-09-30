# -*- coding: utf-8 -*-

import time
from Checker import check


start = time.time()

check("input.txt")

print 'Total time: ', time.time() - start

