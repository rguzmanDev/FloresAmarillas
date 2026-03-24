import turtle
import math
import time

def dibujar_petalo(t, radio, angulo):
    """Auxiliar para dibujar el pétalo de una flor"""
    for _ in range(2):
        t.circle(radio, angulo)
        t.left(180 - angulo)

def dibujar_flor(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    
    # Dibujar el Tallo
    t.color("darkgreen")
    t.pensize(5)
    t.forward(size * 1.5)
    
    # Posición central de la flor
    centro_y = y + (size * 1.5)
    
    # Dibujar pétalos amarillos
    t.penup()
    t.goto(x, centro_y)
    t.pendown()
    t.pensize(1)
    
    colores_petalos = ["gold", "yellow", "orange"]
    
    numero_petalos = 12
    t.color("orange", "yellow")
    t.begin_fill()
    for _ in range(numero_petalos):
        t.penup()
        t.goto(x, centro_y)
        t.pendown()
        dibujar_petalo(t, size, 60)
        t.left(360 / numero_petalos)
    t.end_fill()
    
    # Dibujar el centro de la flor (girasol)
    t.penup()
    # Mover al borde inferior del círculo central
    offset = size / 3
    t.goto(x, centro_y - offset)
    t.setheading(0)
    t.pendown()
    t.color("saddlebrown", "#3b200b") # Cafés para el centro
    t.begin_fill()
    t.circle(offset)
    t.end_fill()

def main():
    pantalla = turtle.Screen()
    pantalla.setup(width=800, height=600)
    pantalla.bgcolor("#121212") # Color oscuro elegante en el fondo
    pantalla.title("Flores Amarillas para ti")
    
    t = turtle.Turtle()
    t.speed(0) # 0 es la velocidad máxima
    t.hideturtle()
    
    # Posiciones (x, y, tamaño) de las flores en el ramo
    flores = [
        (-150, -200, 80),
        (150, -180, 70),
        (0, -250, 100),
        (-75, -230, 85),
        (75, -240, 90)
    ]
    
    # Dibujar todas las flores
    for pos in flores:
        dibujar_flor(t, pos[0], pos[1], pos[2])
        
    # Esperar un poco antes de mostrar el mensaje
    time.sleep(0.5)
    
    # Mostrar el mensaje especial
    t.penup()
    t.goto(0, 150)
    t.color("white")
    
    mensaje = (
        "Sabía que no podía darte flores amarillas en persona hoy,\n"
        "así que decidí escribirlas en código para ti.\n"
        "💛"
    )
    t.write(mensaje, align="center", font=("Arial", 18, "bold italic"))
    
    # Mantener la ventana abierta
    pantalla.mainloop()

if __name__ == "__main__":
    main()
