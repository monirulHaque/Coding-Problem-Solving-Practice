inp = int(input())
 
for i in range(inp):
  a, b, c = list(map(int, input().split()))
  if a + b >= 10 or b + c >= 10 or a + c >= 10:
    print("YES")
  else:
    print("NO")