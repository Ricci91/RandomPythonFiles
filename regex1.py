import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall(message)
print(mo.group())