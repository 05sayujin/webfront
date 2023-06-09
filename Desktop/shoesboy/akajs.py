import sys
import random
import pygame
import time
from math import *
from tkinter import *
import tkinter.messagebox
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,Rect,MOUSEBUTTONDOWN,K_SPACE
pygame.init()
FPSCLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode((700,700))
SURFACE.fill((150,75,0))
Concave=[[0 for i in range(15)]for g in range(15)]
start=0
change=0
color=[(0,0,0),(255,255,255)]
dy=[-1,-1,-1,0]
dx=[-1,0,1,1]
finsh=0
def count(y,x,gy,gx,color):
    cnt=0
    while 1:
        y+=gy
        x+=gx
        if y<0 or y>14 or x<0 or x>14:return cnt
        if Concave[y][x]==color:cnt+=1
        else:return cnt
def put(ypos,xpos):
    global start
    if 0<=floor(ypos)<14 and 0<=floor(xpos)<14:
        if ypos-int(ypos)<=int(ypos)+1-ypos:#up
            print("up")
            if xpos-int(xpos)<=int(xpos)+1-xpos: #left
                if Concave[int(ypos)][int(xpos)]==0:
                    print("left")
                    #pygame.draw.circle(SURFACE,color[start%2],[int(xpos)*40+70,int(ypos)*40+70],20)
                    Concave[int(ypos)][int(xpos)]=start%2+1 # 1 black 2 white
                    return [1,int(ypos),int(xpos)]
                
            else:#right
                if Concave[int(ypos)][int(xpos)+1]==0:
                    print("right")
                    #pygame.draw.circle(SURFACE,color[start%2],[(int(xpos)+1)*40+70,int(ypos)*40+70],20)
                    Concave[int(ypos)][int(xpos)+1]=start%2+1 # 1 black 2 white
                    return [1,int(ypos),int(xpos)+1]
        else:
            if xpos-int(xpos)<=int(xpos)+1-xpos:#left
                if Concave[int(ypos)+1][int(xpos)]==0:
                    print("left")
                    #pygame.draw.circle(SURFACE,color[start%2],[int(xpos)*40+70,(int(ypos)+1)*40+70],20)
                    Concave[int(ypos)+1][int(xpos)]=start%2+1 # 1 black 2 white
                    return [1,int(ypos)+1,int(xpos)]
            else:#right'
                if Concave[int(ypos)+1][int(xpos)+1]==0:
                    print("right")
                    #pygame.draw.circle(SURFACE,color[start%2],[(int(xpos)+1)*40+70,(int(ypos)+1)*40+70],20)
                    Concave[int(ypos)+1][int(xpos)+1]=start%2+1 # 1 black 2 white
                    return [1,int(ypos)+1,int(xpos)+1]
    return [0,0,0]
while 1:
    SURFACE.fill((150,75,0))
    if start%2==0:
        #print("black turn")
        font=pygame.font.SysFont('notosansmonocjkkrregular',50)
        img=font.render("Black turn",True,(0,0,0))
        SURFACE.blit(img, (300,10))
    else:
        #print("white turn")
        font=pygame.font.SysFont('notosansmonocjkkrregular',50)
        img=font.render("White turn",True,(255,255,255))
        SURFACE.blit(img, (300,10))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            xpos,ypos=(event.pos[0]-70)/40,(event.pos[1]-70)/40
            print(ypos,xpos)
            yx=put(ypos,xpos)
            if yx[0]:
                for i in range(4):
                    left=count(yx[1],yx[2],dy[i],dx[i],start%2+1)
                    right=count(yx[1],yx[2],-dy[i],-dx[i],start%2+1)
                    print("left,right",left,right)
                    if left+right==4:
                        finsh=1
                        break
                start+=1
    for i in range(70,655,40):
        pygame.draw.lines(SURFACE,(0,0,0),False,[[70,i],[630,i]],2)
        pygame.draw.lines(SURFACE,(0,0,0),False,[[i,70],[i,630]],2)
    for i in range(15):
        for g in range(15):
            if Concave[i][g]!=0:pygame.draw.circle(SURFACE,color[Concave[i][g]-1],[g*40+70,i*40+70],20)
    pygame.display.update()
    if finsh==1:
        if start%2==1:
            tkinter.messagebox.showinfo("","balck win!")
            print("black win")
        else:
            tkinter.messagebox.showinfo("","white win!")
            print("white win")
        sys.exit()