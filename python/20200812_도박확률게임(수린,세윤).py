import pygame as p
import random as ra


p.init()
w =(255,255,255)
size = (800,400)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True

b = p.image.load("100.png")
b_rect = b.get_rect(left =600 ,top = 50)

c = p.image.load("1000.png")
c_rect = c.get_rect(left =600 ,top = 150)

m = p.image.load("10000.png")
m_rect = m.get_rect(left =600 ,top = 250)

re = p.image.load("sky.png")
r_rect = re.get_rect(left =0 ,top = 300)

bg = p.image.load("bg1.png")

#돈 관련 변수
money = 10000
font = p.font.SysFont("malgungothic",30)
#확률변수
box = 0
#효과음
mja = p.mixer.Sound("m.wav")
# vktks
font2 = p.font.SysFont("malgungothic",150)

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.MOUSEBUTTONDOWN:
            if b_rect.collidepoint(event.pos):
                box = ra.choice([1,1,2,1,1])
                if money <= 0:
                    break 
                if box == 2:
                    mja.play()
                    money = money + 500
                else:
                    money = money - 1000
            if c_rect.collidepoint(event.pos):
                if money <= 0:
                    break 
                box = ra.choice([1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
                if box == 2:
                    mja.play()
                    money = money + 11100
                else:
                    money = money - 200
            if m_rect.collidepoint(event.pos):
                if money <= 0:
                    break 
                box = ra.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
                if box == 2:
                    mja.play()
                    money = money + 11500
                else:
                    money = money - 100
            if r_rect.collidepoint(event.pos):
                money = money + 1 #money += 1
                
            
            

    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(b,b_rect)
    sc.blit(c,c_rect)
    sc.blit(m,m_rect)
    sc.blit(re,r_rect)

    text = font.render("돈 : {}".format(money),True,(244,23,144))
    text2 = font2.render("파산한!",True,(255,0,0))
    sc.blit(text,(0,0))
    sc.blit(text2,(250,100))
                       
    p.display.flip()
