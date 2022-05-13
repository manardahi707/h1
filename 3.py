print("answer a questions")
name=input("enter your name")
infile=open("q.txt",'r')
outfile=open("manar.txt",'w')
s=infile.read()
l=s.splitlines()
infile.close()
n=0
for i in l:
    t=i.split('$')
    print(t[0])
    s=input()
    if s==t[1]:
        n+=1
print("welcome",name,"your result is", n)
outfile.write(name)
outfile.write("\n")
outfile.write(str(n))
outfile.close()
