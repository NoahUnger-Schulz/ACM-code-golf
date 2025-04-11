f=lambda a:["Tues","Wednes","Thurs","Fri","Satur","Sun","Mon"][(int(":400351362402"[a[1]])+a[2]+int(1.2425*a[0]))%7]
print(f(list(map(int,input().split("-"))))+"day")