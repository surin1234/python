import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,600)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
#0이미지 생성
d = p.image.load("d.png")
d_rect = d.get_rect(left = 0, top = 270)
g= p.image.load("g.png")
pan = p.image.load("gg.png")
kim = p.image.load("k.png")
p_rect = pan.get_rect(left = 0, top = 520)
p_rect2 = pan.get_rect(left = 100 , top = 520)
p_rect3 = pan.get_rect(left = 200 , top = 420)
p_rect4 = pan.get_rect(left = 300 , top = 320)
p_rect5 = pan.get_rect(left = 400 , top = 220)
p_rect6 = pan.get_rect(left = 500 , top = 320)
p_rect7 = pan.get_rect(left = 600 , top = 620)
p_rect8 = pan.get_rect(left = 550 , top = 420)
kim_rect = kim.get_rect(left = 600, top = 520)
p_rect9 = pan.get_rect(left = 550 , top = 420)
p_rect10 = pan.get_rect(left = 250 , top = 720)
p_rect11 = pan.get_rect(left = 600 , top = 120)
p_rect12 = pan.get_rect(left = 50 , top = 440)
p_rect13 = pan.get_rect(left = 510 , top = 240)
p_rect14 = pan.get_rect(left = 300 , top = 510)
p_rect15 = pan.get_rect(left = 500 , top = 120)
p_rect16 = pan.get_rect(left = 300 , top = 100)
p_rect17 = pan.get_rect(left = 200 , top = 120)
p_rect18 = pan.get_rect(left = 90 , top = 120)
kim_rect2 = kim.get_rect(left = 90 , top = 70)
#font
font = p.font.SysFont("malgungothic",50)
#fps 설정
clock = p.time.Clock()
#공 위치변수
d_y = 0
d_x = 0
#상태변수
eat = True
eat2 = True
cl = False
cl2 = False
while playing:
    clock.tick(60) #보여지느느 프레임 개수
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()   
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                d_x = -3
            if event.key == p.K_RIGHT:
                d_x = 3
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                d_x = 0
            if event.key == p.K_RIGHT:
                d_x = 0
       
    d_rect.left +=d_x        
    sc.fill(w)
    sc.blit(g,(0,0))
    sc.blit(pan,p_rect)
    sc.blit(pan,p_rect2)
    sc.blit(pan,p_rect3)
    sc.blit(pan,p_rect4)
    sc.blit(pan,p_rect5)
    sc.blit(pan,p_rect6)
    sc.blit(pan,p_rect7)
    sc.blit(pan,p_rect8)
    sc.blit(pan,p_rect9)
    sc.blit(pan,p_rect10)
    sc.blit(pan,p_rect11)
    sc.blit(pan,p_rect12)
    sc.blit(pan,p_rect13)
    sc.blit(pan,p_rect14)
    sc.blit(pan,p_rect15)
    sc.blit(pan,p_rect16)
    sc.blit(pan,p_rect17)
    sc.blit(pan,p_rect18)    
    sc.blit(d,d_rect)
    if d_rect.colliderect(p_rect):
        d_y = -20
    if d_rect.colliderect(p_rect2):
        d_y = -20
    if d_rect.colliderect(p_rect4):
        d_y = -20
    if d_rect.colliderect(p_rect5):
        d_y = -20
    if d_rect.colliderect(p_rect7):
        d_y = -20
    if d_rect.colliderect(p_rect8):
        d_y = -20
    if d_rect.colliderect(p_rect9):
        d_y = -20
    if d_rect.colliderect(p_rect10):
        d_y = -20
    if d_rect.colliderect(p_rect11):
        d_y = -20
    if d_rect.colliderect(p_rect12):
        d_y = -20
    if d_rect.colliderect(p_rect13):
        d_y = -20
    if d_rect.colliderect(p_rect14):
        d_y = -20
    if d_rect.colliderect(p_rect15):
        d_y = -20
    if d_rect.colliderect(p_rect16):
        d_y = -20
    if d_rect.colliderect(p_rect18):
        d_y = -20
    #먹이관련 변수
    if eat:
        sc.blit(kim,kim_rect)
    if d_rect.colliderect(kim_rect):
        eat = False
        cl = True
    if eat2:
        sc.blit(kim,kim_rect2)
    if d_rect.colliderect(kim_rect2):
        eat2 = False
        cl2 = True

    if d_rect.top > 650:
        d_rect.left = 0
        d_rect.top = 270
    #공 튕기는 코드
    d_rect.top += d_y
    d_y += 1
    if cl and cl2:
        sc.blit(clear,(300,200))
        playing = False
        
    if d_rect.left > 800:
        d_rect.left = 770
        
    if d_rect.left < 0:
        d_rect.left = 10


    clear = font.render("game clear!",False,(16,113,215))


    p.display.flip()#화면 업데이트






    
