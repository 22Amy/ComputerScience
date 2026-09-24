x=input('Enter price:')
x=int(x)
if x>10000:
    print(x*.15)
if 10000>=x>5000:
    print(x*.10)
if x<=5000:
    print(x*0.05)