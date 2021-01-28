from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarPerilla():
    glColor3f(0.0,0.0,0.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.040 + 0.08, sin(angulo) * 0.040 - 0.5, 0.0)
    glEnd()

def dibujarVentana(): 
    glBegin(GL_QUADS)
    glColor3f(0.513,0.0,0.0)
    glVertex3f(0.15,-0.22,0.0)
    glVertex3f(0.42,-0.22,0.0)
    glVertex3f(0.42,0.02,0.0)
    glVertex3f(0.15,0.02,0.0)

    #abajo

    glColor3f(0.188,0.850,1.0)
    glVertex3f(0.16,-0.21,0.0)
    glVertex3f(0.27,-0.21,0.0)
    glVertex3f(0.27,-0.11,0.0)
    glVertex3f(0.16,-0.11,0.0)

    glColor3f(0.188,0.850,1.0)
    glVertex3f(0.30,-0.21,0.0)
    glVertex3f(0.41,-0.21,0.0)
    glVertex3f(0.41,-0.11,0.0)
    glVertex3f(0.30,-0.11,0.0)

    #arriba

    glColor3f(0.188,0.850,1.0)
    glVertex3f(0.16,-0.08,0.0)
    glVertex3f(0.27,-0.08,0.0)
    glVertex3f(0.27, 0.01,0.0)
    glVertex3f(0.16, 0.01,0.0)

    glColor3f(0.188,0.850,1.0)
    glVertex3f(0.30,-0.08,0.0)
    glVertex3f(0.41,-0.08,0.0)
    glVertex3f(0.41, 0.01,0.0)
    glVertex3f(0.30, 0.01,0.0)

    glEnd()

def dibujarPuerta(): 
    glBegin(GL_QUADS)
    glColor3f(0.396,0.262,0.015)
    glVertex3f(-0.15,-0.7,0.0)
    glVertex3f(0.15,-0.7,0.0)
    glVertex3f(0.15,-0.3,0.0)
    glVertex3f(-0.15,-0.3,0.0)
    glEnd()

def dibujarPared(): #Pared
    glBegin(GL_QUADS)
    glColor3f(0.839,0.576,0.149)
    glVertex3f(-0.5,-0.7,0.0)
    glVertex3f(0.5,-0.7,0.0)
    glVertex3f(0.5,0.1,0.0)
    glVertex3f(-0.5,0.1,0.0)
    glEnd()

def dibujarTecho():
    #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    glColor3f(0.513,0.0,0.0)
    glVertex3f(-0.6,0.1,0.0)
    glVertex3f(0.0,0.6,0.0)
    glVertex3f(0.6,0.1,0.0)

    glEnd()

def dibujarHojas():
    glColor3f(0.027,0.698,0.)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.16 - 0.78, sin(angulo) * 0.18 - 0.27, 0.0)
    glEnd()

def dibujarHojas2():
    glColor3f(0.027,0.698,0.)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.20 - 0.72, sin(angulo) * 0.18 - 0.15, 0.0)
    glEnd()

def dibujarHojas3():
    glColor3f(0.027,0.698,0.)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.16 - 0.78, sin(angulo) * 0.18 - 0.05, 0.0)
    glEnd()

def dibujarTronco(): 
    glBegin(GL_QUADS)
    glColor3f(0.396,0.262,0.015)
    glVertex3f(-0.78,-0.8,0.0)
    glVertex3f(-0.68,-0.8,0.0)
    glVertex3f(-0.68,-0.4,0.0)
    glVertex3f(-0.78,-0.4,0.0)
    glEnd()

def dibujarPasto(): #Pasto
    glBegin(GL_QUADS)
    glColor3f(0.027,0.698,0.0)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarSol():
    glColor3f(1.0,0.956,0.129)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - 0.65, sin(angulo) * 0.18 + 0.65, 0.0)
    glEnd()

def dibujarNube():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.14 + 0.68, sin(angulo) * 0.1 + 0.52, 0.0)
    glEnd()

def dibujarNube2():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.16 + 0.6, sin(angulo) * 0.1 + 0.48, 0.0)
    glEnd()

def dibujarNube3():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 + 0.47, sin(angulo) * 0.1 + 0.88, 0.0)
    glEnd()

def dibujarNube4():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 + 0.42, sin(angulo) * 0.1 + 0.85, 0.0)
    glEnd()

def dibujarNube5():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 -0.05, sin(angulo) * 0.1 + 0.76, 0.0)
    glEnd()

def dibujarNube6():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.18 - 0.12, sin(angulo) * 0.1 + 0.72, 0.0)
    glEnd()

def dibujarRaya(): 
    glBegin(GL_QUADS)
    glColor3f(1.0,0.956,0.129)

    glVertex3f(-0.68,0.42,0.0)
    glVertex3f(-0.62,0.42,0.0)
    glVertex3f(-0.62,0.32,0.0)
    glVertex3f(-0.68,0.32,0.0)

    glVertex3f(-0.42,0.68,0.0)
    glVertex3f(-0.32,0.68,0.0)
    glVertex3f(-0.32,0.62,0.0)
    glVertex3f(-0.42,0.62,0.0)

    glVertex3f(-0.68,0.98,0.0)
    glVertex3f(-0.62,0.98,0.0)
    glVertex3f(-0.62,0.88,0.0)
    glVertex3f(-0.68,0.88,0.0)

    glVertex3f(-0.98,0.68,0.0)
    glVertex3f(-0.88,0.68,0.0)
    glVertex3f(-0.88,0.62,0.0)
    glVertex3f(-0.98,0.62,0.0)

    glEnd()

def dibujar():
    glColor3f(1.0,0.0,0.0)
    dibujarRaya()
    dibujarPasto()
    dibujarPared()
    dibujarSol()
    dibujarTecho()
    dibujarPuerta()
    dibujarPerilla()
    dibujarVentana()
    dibujarTronco()
    dibujarHojas()
    dibujarHojas2()
    dibujarHojas3()
    dibujarNube()
    dibujarNube2()
    dibujarNube3()
    dibujarNube4()
    dibujarNube5()
    dibujarNube6()
    

def main():
    #inicia glfw
    ancho = 800
    alto = 800
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,ancho,alto)
        #Establece color de borrado
        glClearColor(0.188,0.854,1.0,0.0)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()