#!/usr/bin/env python
# coding=latin1

from visual import *
from math import *
#Los planetas son x veces mas pequeños
escala_planetas=1.0

#Los planetas giran a una velocidad x veces más pequeña
escala_ralentizacion_giro=50.0
#Las distancias son x veces mas pequeñas
escala_distancia_planetas=30.0
class Planeta:
    def __init__(self, nombre, distancia_sol,
                 periodo_rotacion, masa_relativa, radio, color):
        self.nombre=nombre
        self.distancia_sol=(1e6*distancia_sol)/escala_distancia_planetas
        self.periodo=periodo_rotacion
        self.radianes_por_dia=6.28/(periodo_rotacion)
        #Ralentizamos las esferas
        self.radianes_por_dia=self.radianes_por_dia/escala_ralentizacion_giro
        self.radianes_actuales=0
        self.masa=masa_relativa*5.98e24
        self.angulo_planeta=0
        self.radio=radio/escala_planetas
        self.color_r=int ("0x"+color[0:2], 16) /255.0
        self.color_g=int ("0x"+color[2:4], 16) /255.0
        self.color_b=int ("0x"+color[4:6], 16) /255.0
        self.x=self.distancia_sol
        self.y=0
        self.z=0
        self.curva=True
        self.crear()
    def get_distancia(self):
        return self.distancia_sol
    def get_pos(self):
        return (self.x, self.y, self.z)
    def get_radio(self):
        return self.radio
    def get_material(self):
        return self.datos_textura
    def get_r(self):
        return self.color_r
    def get_g(self):
        return self.color_g
    def get_b(self):
        return self.color_b
    def crear(self):
        distancia_al_sol=self.get_distancia()
        pos_planeta=(self.x, self.y, self.z)
        radio_planeta=self.get_radio()
        #print radio_planeta
        rojo=self.get_r()
        verde=self.get_g()
        azul=self.get_b()
        self.esfera_planeta=sphere(pos=pos_planeta, radius=radio_planeta,red=rojo, green=verde, blue=azul)
        self.nombre_planeta=label(pos=pos_planeta, y_offset=self.radio+100, text=self.nombre, opacity=0.1, box=False, line=True)
        self.esfera_planeta.trail=curve(color=color.white)
    def mover(self):
        #print self.nombre, self.radianes_actuales
        self.radianes_actuales+=self.radianes_por_dia
        self.x=sin(self.radianes_actuales)*self.get_distancia()
        self.y=cos(self.radianes_actuales)*self.get_distancia()
        self.esfera_planeta.x=self.x
        self.esfera_planeta.y=self.y
        if self.curva==True:
            self.esfera_planeta.trail.append(pos=self.esfera_planeta.pos)
        self.nombre_planeta.x=self.x
        self.nombre_planeta.y=self.y
        if self.radianes_actuales>6.28:
            self.radianes_actuales=0
            self.curva=False
    
    
#nombre=["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Neptuno", "Urano", "Pluton"]
nombre=["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
#Distancias al sol de los planetas en millones de km
distancias_sol=[57.9, 108.2, 149.6, 227.9, 778.3, 1427, 2871, 4497, 5913]



#Periodo de rotacion de los planetas en dias terrestres
#Rotation period of the planets measured in Earth days
periodo_rotacion=[87.96, 224.68, 365, 687, 11.862*365, 29.456*365, 84*365, 164*365, 247.7*365 ]

#Masas de los planetas
constante_masa=5.98e24
masas=[0.06, 0.82, 1, 0.11, 318, 95.1, 14.6, 17.2, 0.002]

radios=[2440, 6052, 6378, 3397, 71492, 60268, 25559, 24746, 1160]
colores=["3c3837", "d7d4cf", "a5bee7", "e8c187", "b4a49c", "c1b853", "a6c1d5", "90aee0", "3c3734"]
planetas=[]
for i in range (0, len (nombre)):
    planeta=Planeta(nombre[i], distancias_sol[i], periodo_rotacion[i],
                    masas[i], radios[i], colores[i])
    planetas.append(planeta)
    

#situamos el sol
pos_sol=(0,0,0)
color_sol=color.yellow
radio_sol=700000 
material_solar=materials.emissive

esfera_solar=sphere(pos=pos_sol, color=color_sol, radius=radio_sol, material=material_solar)
    
radianes=0

scene.visible=False
scene.title="Planetario (Usa boton derecho o los dos botones y arrastra) Teclas de 0-9 para situarte en Sol/Planetas"
scene.width=800
scene.heigth=600
scene.visible=True
while 1:
    rate(100)
    for i in range (0, len(nombre)):
        planeta=planetas[i]
        planeta.mover()
    #Fin del for
    if scene.kb.keys:
        codigo=scene.kb.getkey()
        if len(codigo)==1:
            if codigo in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                pos=int(codigo)
                planeta=planetas[pos-1]
                pos=planeta.get_pos()
                scene.center=pos
            if codigo=='0':
                scene.center=pos_sol
        #Fin de if
    #Fin de tecas
#Fin del while
    
    
    