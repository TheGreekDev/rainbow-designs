from turtle import *;

speed(25); #You can change

bgcolor('black');

R, G, B = 255, 0, 0;

for i in range(255 * 2):
    colormode(255);

    if i < 255 // 3:
        G += 3;
    elif i < 255 * 2 // 3:
        R -= 3;
    elif i < 255:
        B += 3;
    elif i < 255 * 4 // 3:
        G -= 3;
    elif i < 255 * 5 // 3:
        R += 3;
    else:
        B -= 3;

    pencolor(R,G,B);
    fd(50 + i);
    rt(91);
