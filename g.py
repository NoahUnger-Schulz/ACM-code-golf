a,b,c=*map(int,input().split("-")),
print("Tues,Wednes,Thurs,Fri,Satur,Sun,Mon".split(",")[(int(1.2425*a)+int("-400351362402"[b])+c)%7]+"day")