from clifford import Cl, pretty
from clifford import BladeMap

import pygame
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

pygame.init()
scale=10
window = pygame.display.set_mode((800, 600))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
screen = window

def renderFunction(vec):
    window.fill((255, 255, 255))
    print(400+(vec|d0))
    print(300+(vec|d1))

    tl=vec|d0
    sl=vec|d1

    text_surface1 = my_font.render('Time Dilation(Gamma):'+str((tl.mag2())), False, (0, 0, 0))
    screen.blit(text_surface1, (0,0))
    text_surface2 = my_font.render('speed(m/s):'+str((sl.mag2()*300000000/tl.mag2())), False, (0, 0, 0))
    screen.blit(text_surface2, (0,25))
    text_surface2 = my_font.render('Length Contraction(1/Gamma):'+str(1/(tl.mag2())), False, (0, 0, 0))
    screen.blit(text_surface2, (0,50))
    #draw axes
    pygame.draw.line(window, (50,50,60), (400,0), (400,600),1)
    pygame.draw.line(window, (50,50,60), (0,300), (800,300),1)

    #draw light paths
    pygame.draw.line(window, (5,5,6), (100,0), (700,600),1)
    pygame.draw.line(window, (5,5,6), (100,600), (700,0),1)

    #draw our 4-D vector
    pygame.draw.line(window, (240,45,67), (400,300), (int(400+(sl)*100),int(300-(tl)*100)),1)
    pygame.display.update()
    # pygame.time.wait(1000)
    

from math import e,pi,sqrt


pretty(precision=2)

# Dirac Algebra  `D`
D, D_blades = Cl(1,3, firstIdx=0, names='d')

# Pauli Algebra  `P`
P, P_blades = Cl(3, names='p')

# put elements of each in namespace
locals().update(D_blades)
locals().update(P_blades)

def lorentzRotor(phi,theta=0,psi=0):
    return e**(-(phi/2.0)*d01)*(e**(-(theta/2.0)*d02))*(e**(-(psi/2.0)*d03))


bm = BladeMap([(d01,p1),
               (d02,p2),
               (d03,p3),
               (d12,p12),
               (d23,p23),
               (d13,p13),
               (d0123, p123)])

start=d0
renderFunction(start)

#smallest boost
rotor=lorentzRotor(pi/64)
print("Rotor:",rotor,rotor.mag2())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #boost left, by performing a rotation
                start = rotor*start*~rotor
                print(start)
                start=start/sqrt(start.mag2())
                renderFunction(start)
               
            # checking if key "J" was pressed
            if event.key == pygame.K_RIGHT:
                #boost right, by performing a rotation
                start = ~rotor*start*rotor
                start=start/sqrt(start.mag2())
                renderFunction(start)




