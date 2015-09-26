import pygame,time,math
import sys
import random
from pygame import gfxdraw
from pygame.locals import *

color1 = (100,55,130)
color=(75,0,130)
red = (255,0,0)
green = (118,238,0)
blue = (255,130,171)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
yellow=(238,238,0)
pink = (255,200,200)
darkred=(250,90,90)
darkgreen=(0,100,0)
b=(204,255,255)

pygame.init()
pygame.mixer.init()
#pygame.display.set_caption("My Game")

def font1():
	font=pygame.font.Font(None,70)
	text=font.render("STICK",True,color)
	text_rect=text.get_rect()
	text_rect.centery=120
	text_rect.centerx=250
	screen.blit(text,text_rect)
	font=pygame.font.Font(None,70)
	text=font.render("AND",True,color)
	text_rect=text.get_rect()
	text_rect.centery=180
	text_rect.centerx=250
	screen.blit(text,text_rect)
	font=pygame.font.Font(None,70)
	text=font.render("BRIDGE",True,color)
	text_rect=text.get_rect()
	text_rect.centery=240
	text_rect.centerx=250
	screen.blit(text,text_rect)
	font=pygame.font.Font(None,70)
	text=font.render("Arun",True,pink)
	text_rect=text.get_rect()
	text_rect.centery=540
	text_rect.centerx=250
	screen.blit(text,text_rect)

screen = pygame.display.set_mode((500, 670))
screen.fill((255,255,255))
clock = pygame.time.Clock()
pygame.display.update()
flag3=0
game=0
score=0
over=0

def event() :
        while True :
                for event in pygame.event.get() :
                        if event.type==pygame.QUIT :
                                sys.exit()
                                pygame.quit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                return True

def random1():
	global length, width
	width = random.randrange(20,100)
	length = random.randrange(100,300)

def score1(score):
	font=pygame.font.Font(None,70)
        scoreText = font.render(str(score), True, red)
        scoreRect = scoreText.get_rect()
	pygame.draw.rect(screen,black,(400,35,200,50))
        scoreRect.centerx=450
        scoreRect.centery=60
        screen.blit(scoreText,scoreRect)
	pygame.display.update()
	


def screendraw():
	random1()
	global px1,py1,px2,py2,length,width
	pygame.draw.rect(screen,blue,[50,400,40,220])
	pygame.draw.rect(screen,blue,[length,400,width,220])
	pygame.display.update()
	px1=50
	py1=40
	px2=length
	py2=width


def rescreen(p,q,r,s):
	global t1,px1,px2,py1,py2
	flag=0
	random1()
	t=500
	global length,width
	while flag==0:
		pygame.draw.rect(screen,black,[p,400,q,220])
		pygame.draw.rect(screen,black,[r,400,s,220])
		if r+s<500:
			pygame.draw.rect(screen,black,[t,400,width,220])
		if r>=50:
			p-=2
			r-=2
			if t>length+50:
				t-=2
			pygame.draw.rect(screen,blue,[p,400,q,220])
			pygame.draw.rect(screen,blue,[r,400,s,220])
			if r+s<500:
				pygame.draw.rect(screen,blue,[t,400,width,220])
			pygame.display.update()
			clock.tick(100)
			if r==50:
				flag=1
	px1=r
	py1=s
	px2=t
	py2=width
	t1=s+r-3

def pendulum(xc,yc,r):
	global endx,endy,flag3,game,score
	ang=angl=270
	while angl<=360:
		x=int(r * math.cos(math.radians(angl)))
		y=int(r * math.sin(math.radians(angl)))
		pygame.draw.line(screen,green,[xc,yc],[x+xc,y+yc],3)
		pygame.display.update()
		angl+=2
		pygame.draw.line(screen,black,[xc,yc],[x+xc,y+yc],3)
		clock.tick(80)	
	pygame.draw.line(screen,green,[xc,yc],[x+xc,y+yc],3)
	endx=x+xc
	time.sleep(0.5)
	if endx>=px2 and endx<=px2+py2:
		pygame.draw.line(screen,black,[xc,yc],[x+xc,y+yc],3)
		score+=1
		score1(score)
		rescreen(px1,py1,px2,py2)

	else:
		game=1

def game1():
	#time.sleep(1)
	global flag3,t1,game
	t1=87
	game=0
	while game==0:
		x1=1
		y_speed=0
		y_coord=400
		done=False
		
		while not done:
			for event in pygame.event.get():
        			if event.type == pygame.QUIT:
            				done = True
        			elif event.type == pygame.KEYDOWN:
        				if event.key == pygame.K_UP:
                				y_speed = -2
						x1+=1
				elif event.type == pygame.KEYUP:
        	      			if event.key == pygame.K_UP:
                				y_speed = 0
						done=True
					
        		y_coord = y_coord + y_speed
    			pygame.draw.line(screen,yellow,[t1,400],[t1,y_coord],3)
    			pygame.display.update()
    			clock.tick(100)
		
		x1=400-y_coord
		pendulum(t1,400,x1)
			
	gameover()


def gameover():
	global score,over
	mouse=False
	screen.fill((255,255,255))
	font=pygame.font.Font(None,80)
        scoreText = font.render("GAME OVER", True, color)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=250
        scoreRect.centery=150
        screen.blit(scoreText,scoreRect)
	font=pygame.font.Font(None,50)
	scoreText = font.render("Your Score Is ", True, darkgreen)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=250
        scoreRect.centery=300
        screen.blit(scoreText,scoreRect)
	font=pygame.font.Font(None,70)
        scoreText = font.render(str(score), True, red)
        scoreRect = scoreText.get_rect()
        scoreRect.centerx=250
        scoreRect.centery=400
        screen.blit(scoreText,scoreRect)
	font=pygame.font.Font(None,40)
        scoreText = font.render("Retry", True, black)
        scoreRect1 = scoreText.get_rect()
        scoreRect1.centerx=150
        scoreRect1.centery=500
        screen.blit(scoreText,scoreRect1)
	font=pygame.font.Font(None,40)
        scoreText = font.render("Quit", True, black)
        scoreRect2 = scoreText.get_rect()
        scoreRect2.centerx=350
        scoreRect2.centery=500
        screen.blit(scoreText,scoreRect2)
	pygame.display.update()
	while mouse==False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				mouse=True
			if event.type == pygame.MOUSEBUTTONDOWN:
				mx,my = pygame.mouse.get_pos()
				if mx>=scoreRect1[0]-10 and mx <= (scoreRect1[2]+scoreRect1[0]+10) and my >=scoreRect1[1]-10 and my < (scoreRect1[1]+scoreRect1[3]+10):
					over=0
				else:
					over=1
				mouse=True

screen.fill((255,255,255))
pygame.draw.circle(screen,b,(250,200),200)
font1()
font=pygame.font.Font(None,30)
text = font.render("PLAY", True, black)
rect = text.get_rect()
rect.centerx=250
rect.centery=400
pygame.draw.circle(screen,darkred,[250,400],70)
screen.blit(text, rect)

pygame.display.update()

while True :
        if event() :
                break
while over==0:
	flag3=0
	game=0
	score=0
	screen.fill((0,0,0))
	pygame.draw.line(screen,darkBlue,[0,622],[500,622],5)
	screendraw()
	score1(score)
	game1()
pygame.quit()
sys.exit()

while 1:
	for event in pygame.event.get():
     		if event.type==pygame.QUIT:
			sys.exit()






