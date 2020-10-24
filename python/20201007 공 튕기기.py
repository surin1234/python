import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,600)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
#0이미지 생성
d = p.image.load("d.png")
d_rect = d.get_rect(left = 370, top = 270)
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
    sc.blit(d,d_rect)
    #공 튕기는 코드
    d_rect.top += d_y
    d_y += 1
    if d_rect.top > 600:
        d_y = -20
    if d_rect.left > 800:
        d_rect.left = 770
    if d_rect.left < 0:
        d_rect.left = 10
    p.display.flip()#화면 업데이트






    
