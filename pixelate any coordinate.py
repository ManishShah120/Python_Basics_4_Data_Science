x,y,p,q = input("Enter you coordinates x,y,-x,y space sepparated:").split()
x,y,p,q = [int(x),int(y),int(p),int(q)]
def moveit():
    global x
    global y
    global p
    global q
    x = x + takeinput
    y = y + takeinput
    p = p - takeinput
    q = q - takeinput
print('To execute this Program press 1:')
if1 = int(input())
while(if1 == 1):
    print('The value by which you want to pixelate')
    takeinput = int(input())
    print(x,y,p,q)
    moveit()
    print(x,y,p,q)