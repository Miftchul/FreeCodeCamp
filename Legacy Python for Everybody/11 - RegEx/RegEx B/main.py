import re
s = 'A message from csev@umich.edu to cwen@input.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)