# with open("ok.txt","w")as fp:
#    fp.write("hello world")
# with open("ok.txt","r")as fp:
#    a=fp.read()
#    print(a)
#    #append
# with open("ok.txt","a")as fp:
#    fp.write(" imran loose __")

dt1 = dt2 = ""
with open("note1.txt", "r") as fp:
    dt1=fp.read()
with open("note2.txt", "r") as fp:
    dt2=fp.read()
dt=dt1+dt2
with open("note3.txt","w") as fp:
    fp.write(dt)
