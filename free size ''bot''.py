from math import *
#charracter1 stats
height:int=0
weight:int=0
strength:int=0
speed:int=0
charracter1_pov:int=0
#charracter2 stats
height2:int=0
weight2:int=0
strength2:int=0
speed2:int=0
charracter2_pov:int=0
#stats modifiers charracter1
is_athletic:float=1
body_type:float=1
#stats modifiers charracter2
is_athletic2:float=1
body_type2:float=1
#constant stat modifiers
w:float=70
sp:float=25
st:float=50
#this def is getting the input from the user
def user_input():
    global height,height2,is_athletic,is_athletic2,body_type,body_type2
    #charracter one
    while True:
        try:
            height=int(input('how tall is the first charracter in cm: '))
            break
        except ValueError:
            print('you typed something wrong')
    while True:
        try:
            is_athletic=float(input('how athletic is the first charracter on this scale 0.5----1(avrg)-----1.5: '))
            if is_athletic>=0.5 and is_athletic<=1.5:
                break
            else:
                print('this number is out of scale')
        except ValueError:
            print("you typed something wrong")
    while True:
        try:
            body_type=float(input('what body type is the first charracter on this scale 0.5----1(avrg)-----2: '))
            if body_type>=0.5 and body_type<=2:
                break
            else:
                print('this number is out of scale')
        except ValueError:
            print("you typed something wrong")
    #charracter two
    while True:
        try:
            height2=int(input('how tall is the second charracter in cm: '))
            break
        except ValueError:
            print('you typed something wrong')
    while True:
        try:
            is_athletic2=float(input('how athletic is the second charracter on this scale 0.5----1(avrg)-----1.5: '))
            if is_athletic2>=0.5 and is_athletic2<=1.5:
                break
            else:
                print('this number is out of scale')
        except ValueError:
            print("you typed something wrong")
    while True:
        try:
            body_type2=float(input('what body type is the second charracter on this scale 0.5----1(avrg)-----2: '))
            if body_type2>=0.5 and body_type2<=2:
                break
            else:
                print('this number is out of scale')
        except ValueError:
            print("you typed something wrong")
#calculates strength weight and speed
def calculations():
    global weight,weight2,strength,strength2,speed,speed2,charracter1_pov,charracter2_pov
    #charracter one
    weight=w*body_type*((height/170)**2)
    strength=st*is_athletic*(height/170)**2
    speed=sp*is_athletic*(height/170)
    charracter1_pov=(height2/height)*170
    weight="{:.3f}".format(weight)
    strength="{:.3f}".format(strength)
    speed="{:.3f}".format(speed)
    charracter1_pov="{:.3f}".format(charracter1_pov)
    #charracter two
    weight2=w*body_type2*((height2/170)**2)
    strength2=st*is_athletic2*(height2/170)**2
    speed2=sp*is_athletic2*(height2/170)
    charracter2_pov=(height/height2)*170
    weight2="{:.3f}".format(weight2)
    strength2="{:.3f}".format(strength2)
    speed2="{:.3f}".format(speed2)
    charracter2_pov="{:.3f}".format(charracter2_pov)
def print_stats():
    #charracter 1
    print("the first charracter is ",height,"cm tall. he/she weighs",weight,"kg. he/she can run at ",speed,"km/h, and can bench press about ",strength,"kg.")
    print("the second charracter looks to be about",charracter1_pov,"cm tall from his/hers pont of view.")
    #charracter 2
    print("the second charracter is ",height2,"cm tall. he/she weighs",weight2,"kg. he/she can run at ",speed2,"km/h, and can bench press about ",strength2,"kg.")
    print("the first charracter looks to be about",charracter2_pov,"cm tall from his/hers pont of view.")
#it runs the coded
while True:
    user_input()
    calculations()
    print_stats()
    while True:
        try:
            cont=int(input("do you wanna close the app? 1-yes or 2-calculate another charracters: "))
            if cont in range(0,3):
                break
            else:
                print("this number is out of scale")
        except ValueError:
            print('you typed smoething wrong')
    if cont==1:
        break