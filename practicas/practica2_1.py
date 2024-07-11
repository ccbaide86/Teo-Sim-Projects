# Figuras Geometricas con RoboDK

from robodk.robolink import *  # RoboDK API
from robodk.robomath import *  # Robot toolbox

# Crear instancia rLink
rLink = Robolink()

# Vincular el Robot
Robot = rLink.Item('', ITEM_TYPE_ROBOT)

# Variables para las coordenadas
vHome = rLink.Item('Home')
vSuelo = rLink.Item('Suelo')
vSuelo2 = rLink.Item('Suelo2')
vSuelo3 = rLink.Item('Suelo3')
vSuelo4 = rLink.Item('Suelo4')
vSuelo5 = rLink.Item('Suelo5')
vSuelo6 = rLink.Item('Suelo6')

# Verificar que los elementos existen
if not vHome.Valid():
    raise Exception("La posición 'Home' no existe en la estación.")
if not vSuelo.Valid():
    raise Exception("La posición 'Suelo' no existe en la estación.")
if not vSuelo2.Valid():
    raise Exception("La posición 'Suelo2' no existe en la estación.")
if not vSuelo3.Valid():
    raise Exception("La posición 'Suelo3' no existe en la estación.")
if not vSuelo4.Valid():
    raise Exception("La posición 'Suelo4' no existe en la estación.")
if not vSuelo5.Valid():
    raise Exception("La posición 'Suelo5' no existe en la estación.")
if not vSuelo6.Valid():
    raise Exception("La posición 'Suelo6' no existe en la estación.")


# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Funciones para dibujar figuras geométricas
def dibujar_esfera(Robot, PosRef, Radio, Resolucion):
    for i in range(Resolucion):
        theta = pi * i / Resolucion
        for j in range(Resolucion):
            phi = 2 * pi * j / Resolucion
            x = Radio * sin(theta) * cos(phi)
            y = Radio * sin(theta) * sin(phi)
            z = Radio * cos(theta)
            Posei = PosRef * transl(x, y, z)
            Robot.MoveL(Posei)
    Robot.MoveJ(vHome)


def dibujar_cilindro(Robot, PosRef, Radio, Altura, Resolucion):
    for h in range(Resolucion + 1):
        z = h * Altura / Resolucion
        for i in range(Resolucion + 1):
            theta = 2 * pi * i / Resolucion
            x = Radio * cos(theta)
            y = Radio * sin(theta)
            Posei = PosRef * transl(x, y, z)
            Robot.MoveL(Posei)
    Robot.MoveJ(vHome)

def dibujar_cubo(Robot, PosRef, Lado):
    vertices = [
        (0, 0, 0), (Lado, 0, 0), (Lado, Lado, 0), (0, Lado, 0), 
        (0, 0, Lado), (Lado, 0, Lado), (Lado, Lado, Lado), (0, Lado, Lado)
    ]
    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    for a in aristas:
        v1, v2 = vertices[a[0]], vertices[a[1]]
        Posei = PosRef * transl(v1[0], v1[1], v1[2])
        Robot.MoveL(Posei)
        Posei = PosRef * transl(v2[0], v2[1], v2[2])
        Robot.MoveL(Posei)
    Robot.MoveJ(vHome)

def dibujar_cono(Robot, PosRef, RadioBase, Altura, Resolucion):
    for h in range(Resolucion + 1):
        z = h * Altura / Resolucion
        radio = RadioBase * (1 - h / Resolucion)
        for i in range(Resolucion + 1):
            theta = 2 * pi * i / Resolucion
            x = radio * cos(theta)
            y = radio * sin(theta)
            Posei = PosRef * transl(x, y, z)
            Robot.MoveL(Posei)
    Robot.MoveJ(vHome)

def dibujar_piramide(Robot, PosRef, Base, Altura):
    vertices = [
        (0, 0, 0), (Base, 0, 0), (Base, Base, 0), (0, Base, 0), (Base/2, Base/2, Altura)
    ]
    aristas = [
        (0, 1), (1, 2), (2, 3), (3, 0), 
        (0, 4), (1, 4), (2, 4), (3, 4)
    ]
    for a in aristas:
        v1, v2 = vertices[a[0]], vertices[a[1]]
        Posei = PosRef * transl(v1[0], v1[1], v1[2])
        Robot.MoveL(Posei)
        Posei = PosRef * transl(v2[0], v2[1], v2[2])
        Robot.MoveL(Posei)
    Robot.MoveJ(vHome)

def dibujar_prisma(Robot, PosRef, Radio, Altura, Resolucion):
    # Definir los vértices del prisma hexagonal
    vertices_base = [(Radio * cos(2 * pi * i / 6), Radio * sin(2 * pi * i / 6), 0) for i in range(6)]
    vertices_top = [(Radio * cos(2 * pi * i / 6), Radio * sin(2 * pi * i / 6), Altura) for i in range(6)]
    
    # Dibujar las aristas verticales
    for i in range(6):
        Posei = PosRef * transl(vertices_base[i][0], vertices_base[i][1], vertices_base[i][2])
        Robot.MoveL(Posei)
        Posei = PosRef * transl(vertices_top[i][0], vertices_top[i][1], vertices_top[i][2])
        Robot.MoveL(Posei)
    
    # Dibujar las aristas de la base
    for i in range(6):
        v1, v2 = vertices_base[i], vertices_base[(i + 1) % 6]
        Posei = PosRef * transl(v1[0], v1[1], v1[2])
        Robot.MoveL(Posei)
        Posei = PosRef * transl(v2[0], v2[1], v2[2])
        Robot.MoveL(Posei)
    
    # Dibujar las aristas del top
    for i in range(6):
        v1, v2 = vertices_top[i], vertices_top[(i + 1) % 6]
        Posei = PosRef * transl(v1[0], v1[1], v1[2])
        Robot.MoveL(Posei)
        Posei = PosRef * transl(v2[0], v2[1], v2[2])
        Robot.MoveL(Posei)
    
    Robot.MoveJ(vHome)

# Llamar a las funciones para dibujar las figuras deseadas

# Dibujar una esfera
dibujar_esfera(Robot, PosRef, Radio=50, Resolucion=20)

# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo2)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Dibujar un cilindro
dibujar_cilindro(Robot, PosRef, Radio=50, Altura=100, Resolucion=20)

# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo3)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Dibujar un cubo
dibujar_cubo(Robot, PosRef, Lado=100)

# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo4)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Dibujar un cono
dibujar_cono(Robot, PosRef, RadioBase=50, Altura=100, Resolucion=20)

# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo5)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Dibujar una pirámide
dibujar_piramide(Robot, PosRef, Base=100, Altura=100)

# Mover el Robot a las posiciones iniciales
Robot.MoveJ(vHome)
Robot.MoveJ(vSuelo6)

# Obtener Pose del Robot
PosRef = Robot.Pose()

# Mostrar Matriz de la Pose
print('La matriz Inicial es: ', PosRef)

# Dibujar un prisma hexagonal
dibujar_prisma(Robot, PosRef, Radio=50, Altura=100, Resolucion=20)

# Regresar el Robot a Home
Robot.MoveJ(vHome)