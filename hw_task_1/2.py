def maxlen(s1, s2):
  return len(max(s1, s2, key=len))

print(maxlen([1,2,3,4],[1,23,2]))