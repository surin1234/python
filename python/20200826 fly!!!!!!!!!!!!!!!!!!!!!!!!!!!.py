import pygame as p

p.init()
w =(255,255,255)
size = (800,600) 
sc = p.display.set_mode(size)
p.display.set_caption("게임판") 
playing = True
plane = p.image.load("bird.png")
p_rect = plane.get_rect(left = 20, top = 250)
while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
            
    sc.fill(w)
    sc.blit(plane,p_rect)
    p.display.flip()
