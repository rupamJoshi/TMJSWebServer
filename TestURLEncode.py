import sys
import urllib
from urllib.parse import urlencode
sys.path.insert(0,'one.com\\private')
sys.path.insert(0,'two.com\\private')
print(sys.path)
f={'nm':'kunal gangaher','ct':'ujjain'}
print(urllib.urlencode(f))

