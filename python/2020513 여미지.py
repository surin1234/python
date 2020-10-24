import pygame as p

p.init() # 라이브러리 초기화

size = (1000,1000)
white = (255,255,255) # (R,G,B)
e = p.image.load("a.png")
ee = p.image.load("b.png")
eee = p.image.load("c.png")
p.mixer.music.load("1.mp3")
p.mixer.music.play(0)

sc =p.display.set_mode(size) # 해상도 설정
p.display.set_caption("image") #창이름 변경

done= False

while not done:
      for event in p.event.get(): # 우리가 누르는거 감지
            if event .type == p.QUIT: #게임창 x버튼 누르면
                  done = True 

      sc.fill(white)
      sc.blit(e,(100,100))
      sc.blit(ee,(900,100))
      sc.blit(eee,(500,100))
      p.display.flip() #화면 업데이트









