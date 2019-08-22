# source: https://chriskiehl.com/article/parallelism-in-one-line

import urllib.request 
from multiprocessing.dummy import Pool as ThreadPool

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc..
  ]

results = []
for url in urls:
  result = urllib.request .urlopen(url)
  results.append(result)

# # ------- VERSUS ------- #


# # ------- 4 Pool ------- #
pool = ThreadPool(4)
results = pool.map(urllib.request .urlopen, urls)

# # ------- 8 Pool ------- #

pool = ThreadPool(8)
results = pool.map(urllib.request .urlopen, urls)

# # ------- 13 Pool ------- #

pool = ThreadPool(13)
results = pool.map(urllib.request .urlopen, urls)