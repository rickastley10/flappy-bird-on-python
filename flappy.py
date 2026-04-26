import turtle
import os
import random
t = turtle
t.setup(300, 500)
t.title("flappybird")
os.chdir("assets")


if os.path.exists("options"):
    ostype=open("options", "r").read()
    if ostype=="windows":
        import winsound
        # winsound.PlaySound('path\\to\\sound.wav', winsound.SND_FILENAME)
    elif ostype=="linux":
        import subprocess
        # subprocess.call(['aplay', 'path/to/sound.wav'])
    elif ostype=="mac":
        import subprocess
        # subprocess.call(['afplay', 'path/to/sound.wav'])
    else:
        pass
else:
    ostype=t.textinput("","what is your os?\nwindows | linux | mac")
    open("options", "w").write(f"{ostype}")
    if ostype=="windows":
        import winsound
        # winsound.PlaySound('path\\to\\sound.wav', winsound.SND_FILENAME)
    elif ostype=="linux":
        import subprocess
        # subprocess.call(['aplay', 'path/to/sound.wav'])
    elif ostype=="mac":
        import subprocess
        # subprocess.call(['afplay', 'path/to/sound.wav'])
    else:
        pass

    

    
    
t.register_shape("yellowbird-midflap.gif")
t.register_shape("pipe-green.gif")
t.register_shape("pipe-green2.gif")
t.register_shape("base.gif")
t.register_shape("yellowbird-upflap.gif")
t.register_shape("yellowbird-downflap.gif")

t.penup()
t.hideturtle()
t.bgpic("background-day.gif")

if os.path.exists("highscore"):
    highscore=int(open("highscore","r").read())
else:
    highscore=0
    open("highscore","w").write(f"{highscore}")
score=0
gameon=0
p1x=100
p1y=-300
p3x=300
p3y=-300
bx = -100
by = 0
jumping=0
jumpframe=10
t.tracer(0, 0)
flapanim=2

f=turtle.Turtle()
f.penup()
f.shape("yellowbird-midflap.gif")

p1=turtle.Turtle()
p1.penup()
p1.shape("pipe-green.gif")


p2=turtle.Turtle()
p2.penup()
p2.shape("pipe-green2.gif")
p2.setheading(180)



p3=turtle.Turtle()
p3.penup()
p3.shape("pipe-green.gif")


p4=turtle.Turtle()
p4.penup()
p4.shape("pipe-green2.gif")




ground=turtle.Turtle()
ground.penup()
ground.shape("base.gif")


def gameover():
    global p1x, p1y, bx, by, jumping, jumpframe, score, flapanim, gameon, p3x, p3y
    t.clear()
    if ostype == "windows":
        winsound.PlaySound('hit.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif ostype == "linux":
        subprocess.Popen(['aplay', 'hit.wav'])
    elif ostype == "mac":
        subprocess.Popen(['afplay', 'hit.wav'])
    else:
        pass
    p1x=100
    p1y=-300
    p3x=300
    p3y=-300
    bx = -100
    by = 0
    jumping=0
    jumpframe=10
    score=0
    gameon=0
    ground.hideturtle()
    p2.hideturtle()
    p1.hideturtle()
    p3.hideturtle()
    p4.hideturtle()
    f.hideturtle()
    t.bgpic("mainmenu.gif")
    
def start():
    global gameon
    ground.showturtle()
    p2.showturtle()
    p1.showturtle()
    p3.showturtle()
    p4.showturtle()
    
    f.showturtle()
    t.bgpic("background-day.gif")
    gameon=1

def flappy():
    global p1x, p1y, bx, by, jumping, jumpframe, score, flapanim
    if jumping == 0:
        by-=10
    flapanim+=1
    if flapanim==5:flapanim=0
    if by <=-250:
        gameover()
        
    if flapanim==1:
        f.shape("yellowbird-upflap.gif")
    elif flapanim==2:
        f.shape("yellowbird-midflap.gif")
    elif flapanim==3:
        f.shape("yellowbird-downflap.gif")
    elif flapanim==4:
        f.shape("yellowbird-midflap.gif")
    f.goto(bx, by)

def pipe():
    global p1x, p1y, bx, by, jumping, jumpframe, score, p3x, p3y, highscore
    p1x-=5
    p1.goto(p1x, p1y)
    p2.goto(p1x, (p1y+500))
    p2.setheading(180)
    if (p1x <= bx <= p1x+20 and (p1y+300)<by)or(p1x <= bx <= p1x+20 and (p1y+200)>=by):
        gameover()
    if p1x <= -150:
        p1x=300
        p1y=-300 + ((random.randint(1,10))*20)
        score+= 1
        if score > highscore:
            highscore = score
            open("highscore","w").write(f"{highscore}")
        if ostype == "windows":
            winsound.PlaySound('point.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif ostype == "linux":
            subprocess.Popen(['aplay', 'point.wav'])
        elif ostype == "mac":
            subprocess.Popen(['afplay', 'point.wav'])
        else:
            pass
    p3x-=5
    p3.goto(p3x, p3y)
    p4.goto(p3x, (p3y+500))
    if (p3x <= bx <= p3x+20 and (p3y+300)<by)or(p3x <= bx <= p3x+20 and (p3y+200)>=by):
        gameover()
    if p3x <= -150:
        p3x=300
        p3y=-300 + ((random.randint(1,10))*20)
        score+= 1
        if score > highscore:
            highscore = score
            open("highscore","w").write(f"{highscore}")
        if ostype == "windows":
            winsound.PlaySound('point.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        elif ostype == "linux":
            subprocess.Popen(['aplay', 'point.wav'])
        elif ostype == "mac":
            subprocess.Popen(['afplay', 'point.wav'])
        else:
            pass
    

def gui():
    t.goto(-100, 180)
    t.color("orange")
    t.write(f"{score}\nHI:{highscore}", align="center", font=("Arial Rounded MT Bold", 16, "normal"))
    ground.goto(0, -260)

def jumpanim():
    global bx, by, jumping, jumpframe, flapanim
    
    if jumpframe <= 10 and jumping==1:
        by+=10
        jumpframe += 1
        jumping = 1
        
        t.ontimer(jumpanim, 30)
        
    elif jumpframe > 10 and jumping==1:
        jumping=0
        
        pass
        
        
def jump():
    global bx, by, jumping, jumpframe
    if ostype == "windows":
        winsound.PlaySound('wing.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif ostype == "linux":
        subprocess.Popen(['aplay', 'wing.wav'])
    elif ostype == "mac":
        subprocess.Popen(['afplay', 'wing.wav'])
    else:
        pass
    jumping=1
    jumpframe=0
    jumpanim()
    
    
def key():
    global gameon
    if gameon==0:
        start()
    else:
        jump()
    
    
def click(x, y):
    global gameon
    if gameon==0:
        start()
    else:
        jump()
    
    
t.onscreenclick(click)
t.onkeypress(key, "space")
t.listen()

gameover()

def mainloop():
    if gameon==1:
        t.clear()
        flappy()
        pipe()
        gui()
        
        
        t.update()
        t.ontimer(mainloop, 30)
    else:
        t.ontimer(mainloop, 30)
    
mainloop()
t.mainloop()
