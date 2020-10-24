import pygame as py

py.init() #초기화


# (R,G,B)
Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)

# (가로,세로)
size = [400,400]

screen = py.display.set_mode(size)#해상도설정


py.display.set_caption("Game title")#창제목부분 *


done = False
clock = py.time.Clock()#초당 몇번 출력할 것인가

while not done:#ture
      clock.tick(10) #초당 10번 출력하겠다

      for event in py.event.get():#이벤트 체크
            if event.type == py.QUIT:#만약 창 위에 x를 눌렀으면 
                  done = True#무한반복 종료



      screen.fill(White)#화면색 흰색





      py.draw.rect(screen,Blue,[75,175,50,50],5)
      py.draw.rect(screen,Blue,[350,350,50,50],5)
      


      py.draw.polygon(screen,Red,[[30,150],[125,100],[220,150]])
      py.draw.rect(screen,Blue,[30,150,190,190],5)









      py.display.flip() #화면 업데이트











      
