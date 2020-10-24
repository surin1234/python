import pygame as p #파일저장명 :20200523_키보드 조작키

p.init() # 라이브러리 초기화

size = (800,400) #(가로,세로)


sc = p.display.set_mode(size) # 해상도 크기 설정 
w = (255,255,255) #(R,G,B) 흰색
b = (0,0,0) #검정
#이미지 변수에 업로드 
pl = p.image.load("plane.png")
bg = p.image.load("bg.png")
bg1_1 = bg.copy()
em = p.image.load("bullet.png")
eem = p.image.load("bbb.png")

p.display.set_caption("키보드 조작") #게임창 제목

playing = True
# 동그라미 좌표 
x= 10
y= 0
# 동그라미 부드럽게
y_c = 0
#배경 좌표
bg_x = 0 #첫번째 배경 
bg1_x = 800
#총알좌표
e = 400
ee = 100
while playing:

      for event in p.event.get(): # 사용자가 뭘 눌렀는지 감지
            if event.type == p.QUIT: #게임창 x버튼을 누른다면
                  playing = False # 게속반복을 종료
                  p.quit() #게임창x버튼 누르면 사라짐 
                  quit #sell 창 종료
            if event.type == p.KEYDOWN: #키보드를 눌렀을때 반응
                  if event.key == p.K_UP: #위 방향키를 누르면 
                        y = -5
                  if event.key == p.K_DOWN: 
                        y = 5
            if event.type == p.KEYUP: #키보드를 때었을때 반응
                  if event.key == p.K_UP or event.key == p.K_DOWN:
                        y = 0
      y_c += y
      
      

            
      sc.fill(w) #바탕화면 흰색으로
      sc.blit(bg,(bg_x,0)) #배경 화면에 업로드
      sc.blit(bg1_1,(bg1_x,0))
      sc.blit(em,(e,0))
      sc.blit(eem,(ee,0))
      e-=8
      ee-=10
      bg_x-=4#2픽셀 이동
      bg1_x-=4#2픽셀 이동
      if bg_x == -800:
            bg_x = 800
      if bg1_x == -800:
            bg1_x = 800
      if e == 0:
            e = 800
      if ee == 0:
            ee = 800
             
      sc.blit(pl,(x,y_c)) #비행기 화면에 업로드 
      if y_c > 350:
            y = 0
      if y_c < 0:
            y = 0



      p.display.flip() #화면 업데이트 
                                                                                                                                                                                                                                                                                                  #||
                                                                                                                                                                                                                                                                                                  #\
      
      

      











