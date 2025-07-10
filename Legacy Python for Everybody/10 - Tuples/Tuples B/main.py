lst = []
for key, val in counts.items(): # type: ignore
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)