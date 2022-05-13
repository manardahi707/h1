while True:
    d=int(input('enter number'))
    binary=[]
    while True:
        binary.append(str(d%2))
        d//=2
        if d==0:
            break
    binary.reverse()
    binary=''.join(binary)
    print(binary)
    print("enter 0 to stop")
    s=input()
    if s=='0':
        break
