import pygame as p

p.init()
w =(255,255,255)
size = (600,800)
sc = p.display.set_mode(size)
p.display.set_caption("벽돌깨기")
playing = True

pan = p.image.load("pan.png")

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()

    sc.fill(w)
    sc.blit(pan,(250,725))
    p.display.flip()
