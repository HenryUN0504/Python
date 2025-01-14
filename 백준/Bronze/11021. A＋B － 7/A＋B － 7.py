var2 = int(input())
for i in range (var2):
    var, var1 = map(int, input().split())
    print("Case #" + str(i+1) + ": " + str(var + var1))