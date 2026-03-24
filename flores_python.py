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
    
    t.color("darkgreen")
    t.pensize(5)
    t.forward(size * 1.5)
    
    centro_y = y + (size * 1.5)
    
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
    
    t.penup()
    offset = size / 3
    t.goto(x, centro_y - offset)
    t.setheading(0)
    t.pendown()
    t.color("saddlebrown", "#3b200b")
    t.begin_fill()
    t.circle(offset)
    t.end_fill()

def main():
    pantalla = turtle.Screen()
    pantalla.setup(width=800, height=600)
    pantalla.bgcolor("#121212")
    pantalla.title("Flores Amarillas para ti")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    
    flores = [
        (-150, -200, 80),
        (150, -180, 70),
        (0, -250, 100),
        (-75, -230, 85),
        (75, -240, 90)
    ]
    
    for pos in flores:
        dibujar_flor(t, pos[0], pos[1], pos[2])
        
    time.sleep(0.5)
    
    t.penup()
    t.goto(0, 150)
    t.color("white")
    
    mensaje = (
        "Sabía que no podía darte flores amarillas en persona hoy,\n"
        "así que decidí escribirlas en código para ti.\n"
        "💛"
    )
    t.write(mensaje, align="center", font=("Arial", 18, "bold italic"))
    
    pantalla.mainloop()

if __name__ == "__main__":
    main()
