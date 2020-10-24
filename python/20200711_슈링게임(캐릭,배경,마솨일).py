import pygame as p

p.init()
w =(255,255,255)








size = (600,900)
sc = p.display.set_mode(size)
p.display.set_caption("슈팅게임")
playing = True

p_image = p.image.load("pp.png")
p_rect = p_image.get_rect(left=250,top=750)
x = 0
y = 0

bg = p.image.load("space.png")

b_image = p.image.load("bul.png")
b_list = []

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                y =-5
            if event.key == p.K_DOWN:
                y = 5
            if event.key == p.K_LEFT:
                x =-5
            if event.key == p.K_RIGHT:
                x = 5
            if event.key == p.K_SPACE:
                b_rect = b_image.get_rect(left=p_rect.left+45, top=p_rect.top)
                b_list.append(b_rect)
        if event.type == p.KEYUP:
            if event.key == p.K_UP:
                y = 0
            if event.key == p.K_DOWN:
                y = 0
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    p_rect.left += x     # += --> p_rect.left = p_rectt.left + x
    p_rect.top += y
    

    
    sc.fill(w)
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(b_image,b_rect)
    for b_rect in b_list:
        b_rect.top -= 5
        if b_rect.top <= 10:
            b_list.remove(b_rect)

        
    sc.blit(p_image,p_rect) #비행기 업로드

    
    p.display.flip()

    
