"""total = 0
birlik = 0
onlik = 0
yuzlik = 0
def sum_numbers():
    global total, birlik, onlik, yuzlik
    
    for a in range(101):
        birlik = a%10
        onlik = a//10
        #yuzlik = a//100
        total += birlik+onlik+yuzlik
  
    print("1 dan 100 gacha bo'lgan raqamlar yig'indisi: ", total)

sum_numbers()   
  """

"""s = 0

for i in range(1, 101):
    k1 = i//100
    k2 = (i%100)//10
    k3 = i%10

    s += k1 + k2 + k3

print(s)
"""
"""s = 0

for i in range(1, 101):
    while i>0:
        s += i%10
        i//=10
print(s)"""

n = 17284682

while n>0:
    print(n%10)
    n//=10