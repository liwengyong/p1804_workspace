
import re
ret = re.match('^1\d{10}$','12345678905')
print(ret.group())
