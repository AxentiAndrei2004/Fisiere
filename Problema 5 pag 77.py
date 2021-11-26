vocale='AaEeIiOoUu'
x=0
with open('Text 1.txt','r') as f:
    vo=f.read()
with open('Text 2.txt','w') as f:
    for a in vo:
        if a in vocale:
            f.write(a)
            x+=1
print('Vocalele sunt',x)