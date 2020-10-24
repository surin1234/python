import pygame as p

p.init()

w = (255,255,255)

size=(740,370)

sc = p.display.set_mode(size) 

i = p.image.load("f.png")#비행기 이미지 
ii = p.image.load("bg.png")

p.display.set_caption("Goonso")
x = 0 
y = 0
k = 0
g = 0
y_2 = 0



done = True

while done:

      for event in p.event.get():
            if event.type == p.QUIT:
                  done == False
                  p.quit()
                  quit()
            if event.type == p.KEYDOWN: # 키보드를 눌렀을때를 감지
                  if event.key == p.K_UP:
                        y = -1

                        
                  if event.key == p.K_DOWN:
                        y = 1

                  if event.key == p.K_RIGHT:
                        x = -1

                  if event.key == p.K_LEFT:
                        x = 1
            if event.type == p.KEYUP: #키보드를 땟을때 감지 
                  if event.key == p.K_UP or event.key == p.K_DOWN:
                        y_2 == 0
                        
      y_2 += y 

      sc.fill(w)
      sc.blit(ii,(k,g))#배경 
      sc.blit(i,(x,y_2)) # 이미지 올리는 코드(xy좌표)
      p.display.flip()






      
      
