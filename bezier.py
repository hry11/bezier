from fltk import *
from time import sleep

points = [[]]
curve = []

def lerp(p0, p1, t):
    return [(1-t)*p0[0] + t*p1[0], (1-t)*p0[1] + t*p1[1]]

def drawPoints(n):
    for i in range(len(points[n])):
        cercle(points[n][i][0], points[n][i][1], 3, remplissage="blue")

def drawLines(n):
    for i in range(len(points[n])-1):
        ligne(points[n][i][0], points[n][i][1], points[n][i+1][0], points[n][i+1][1], couleur="red")

def bezier(t):
    for i in range(len(points)):
        for j in range(len(points[i])-1):
            points[i+1][j] = lerp(points[i][j], points[i][j+1], t)
            if len(points[i]) == 2:
                curve.append(points[i+1][j])
        drawPoints(i)
        drawLines(i)

cree_fenetre(1800,1000)
tev = ""
p = 100
s = 0.01

while tev != "Quitte":
    ev = donne_ev()
    tev = type_ev(ev)
    drawPoints(0)
    drawLines(0)
    if tev == "ClicDroit":
        points[0].append([abscisse(ev), ordonnee(ev)])
    if tev == "ClicGauche":
        #reset array except for first line
        del points[1:len(points)]
        #each line of the array has one less element than the previous one, cf notebook
        for i in range(len(points[0])-1):
            newLine = []
            for j in range(len(points[0])-1-i):
                newLine.append([])
            points.append(newLine)
        #run the bezier func
        for i in range(p):
            bezier(i/p)
            sleep(s)
            mise_a_jour()
            #inefficient, dont care
            efface_tout()
            for j in range(len(curve)):
                cercle(curve[j][0], curve[j][1], 3, remplissage="black")
    mise_a_jour()
