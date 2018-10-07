
# coding: utf-8

# ### lone_sum

# In[ ]:

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  if (a != b) and (b != c) and (c != a):
    return a+b+c
  if (a == b) and (b != c):
    return c
  if (b == c) and (c != a):
    return a
  if (c == a) and (a != b):
    return b

  ### OK
