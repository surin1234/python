import pygame as p

p.init()

w = (255,255,255)
r = (255,255,0)
b = (255,0,255)


size=(400,400)

sc = p.display.set_mode(size)

i = p.image.load("a.png")
ii = p.image.load("g.png")


p.display.set_caption("Goonso")
x = 100
y = 100


done = True

while done:

      for event in p.event.get():
            if event.type == p.QUIT:
                  done == False
                  p.quit()
                  quit()
            if event.type == p.KEYDOWN: # 키보드를 눌렀을때를 감지
                  if event.key == p.K_DOWN:
                        y = y+6

                        
                  if event.key == p.K_UP:
                        y = y-6
                  
            
                  if event.key == p.K_RIGHT:
                        x = x+3

                        
                  if event.key == p.K_LEFT:
                        x = x-3
                        

                  if event.key == p.K_a:
                        w = r


                  if event.key == p.K_b:
                        w = b = r
                        





      sc.fill(w)
      sc.blit(i,(x,y)) # 이미지 올리는 코드(xy좌표)
      sc.blit(ii,(x,y+100))
      p.display.flip()






      
      
