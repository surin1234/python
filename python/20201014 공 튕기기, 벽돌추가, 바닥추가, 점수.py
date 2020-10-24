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
#font
font = p.font.SysFont("malgungothic",50)
#fps 설정
clock = p.time.Clock()
#공 위치변수
d_y = 0
d_x = 0

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
    sc.blit(kim,kim_rect)
    sc.blit(d,d_rect)
    if d_rect.colliderect(p_rect):
        d_y = -20
    if d_rect.colliderect(p_rect2):
        d_y = -20
    if d_rect.colliderect(p_rect3):
        d_y = -20
    if d_rect.colliderect(p_rect4):
        d_y = -20
    if d_rect.colliderect(p_rect5):
        d_y = -20
    if d_rect.colliderect(p_rect7):
        d_y = -20
    if d_rect.colliderect(p_rect8):
        d_y = -20

        
    #공 튕기는 코드
    d_rect.top += d_y
    d_y += 1
    if d_rect.top > 650:
        d_rect.left = 0
        d_rect.top = 270
        sc.blit(text,(310,210))
    if d_rect.left > 800:
        d_rect.left = 770
        
    if d_rect.left < 0:
        d_rect.left = 10


    text = font.render("-Game over-",True,(16,113,215))


    p.display.flip()#화면 업데이트






    
