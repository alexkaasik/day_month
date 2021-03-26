d=int(input("d put number"))
m=int(input("m put number"))

if 1<=d<=31 and 1<=m<=12:
    if (d>=22 and m==12) or (d<20 and m==1):
        z="Козерог"
    elif (d>=20 and m==1) or (d<18 and m==2):
        z="Водолей"
    elif (d>=19 and m==2) or (d<20 and m==3):
        z="Рыбы"
    elif (d>=21 and m==3) or (d<19 and m==4):
        z="Овен"
    elif (d>=20 and m==4) or (d<20 and m==5):
        z="Телец"
    elif (d>=21 and m==5) or (d<20 and m==6):
        z="Близнецы"
    elif (d>=21 and m==6) or (d<22 and m==7):
        z="Рак"
    elif (d>=23 and m==7) or (d<22 and m==8):
        z="Лев"
    elif (d>=23 and m==8) or (d<22 and m==9):
        z="Дева"
    elif (d>=23 and m==9) or (d<22 and m==10):
        z="Весы"
    elif (d>=23 and m==10) or (d<21 and m==11):
        z="Скорпион"
    elif (d>=22 and m==11) or (d<21 and m==12):
        z="Стрелец"
    if m == 1:
        text="January"
    elif m == 2:text="February"
    elif m == 3:text="March"
    elif m == 4:text="April"
    elif m == 5:text="May"
    elif m == 6:text="June"
    elif m == 7:text="July"
    elif m == 8:text="August"
    elif m == 9:text="September"
    elif m == 10:text="October"
    elif m == 11:text="November"
    elif m == 12:text="December"
        
    print(f"{z}. {d}. {text}") #или print(f"{z}. day:{d}, month:{m}")
else:
    print("invalid")
