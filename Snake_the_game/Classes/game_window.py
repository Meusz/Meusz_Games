#https://github.com/MagnoEfren/gui_python_tkinter/blob/main/Juego%20Snake/juego%20Snake.py
from tkinter import *
from Classes.snake import *
from Classes.apple import *
import random

#The first posible square position is 15,15
#The size of the game board is 16x16
#The last posible square position is 465,465

posiciones = [15, 45, 75,105,135,165, 195, 225, 255, 285, 315, 345, 375, 405, 435, 465] #All the posible x or y positions

class game_window:
    def __init__(self):
        """The game_window class will be the one in which we will launch the game and play on it
            OBJ :
            PRE:
        """
        #Initializase the tk window with a title
        self.window = Tk()
        self.window.geometry("495x510")     #Set a geometry width x height
        self.window.resizable(0,0)          #With this option the window wont be resizable
        self.window.title = "Game Window"   #Set a name for the tk window

        #Add the top frames with the game exit, start game options and quantity of apples ate

        frame_1 = Frame(self.window, width=495, height=25, bg='blue')
        frame_1.grid(column=0, row=0)
        frame_1.grid_propagate(False)
        frame_2 = Frame(self.window, width=510, height=500, bg='black')
        frame_2.grid(column=0, row=1)

        # Now we will need to ubicate the exit button, start game button and quantity of apples ate
        button1 = Button(frame_1, text='Exit', bg='orange', command=self.salir)
        button1.grid(row=0, column=0, padx=20)
        button2 = Button(frame_1, text='Iniciar', bg='aqua', command=self.play)
        button2.grid(row=0, column=1, padx=20)

        self.cantidad = Label(frame_1, text='Cantidad 🍎 :', bg='black', fg='red', font=('Arial', 12, 'bold'))
        self.cantidad.grid(row=0, column=2, padx=20)




        #Add actions when pressing an arrow
        self.window.bind("<KeyPress-Up>", lambda event: self.snake.set_direction("up") )
        self.window.bind("<KeyPress-Down>", lambda event: self.snake.set_direction("down") )
        self.window.bind("<KeyPress-Left>", lambda event: self.snake.set_direction("left") )
        self.window.bind("<KeyPress-Right>", lambda event: self.snake.set_direction("right") )

        # Add actions when pressing wasd
        self.window.bind("<KeyPress-w>", lambda event: self.snake.set_direction("up"))
        self.window.bind("<KeyPress-s>", lambda event: self.snake.set_direction("down"))
        self.window.bind("<KeyPress-a>", lambda event: self.snake.set_direction("left"))
        self.window.bind("<KeyPress-d>", lambda event: self.snake.set_direction("right"))


        ##Add the Canvas object which will enable to draw the squares for the game, apples and the snake
        self.canvas = Canvas(frame_2, bg='black', width=479, height=479)
        self.canvas.pack()

        #We will add a boolean variable to turn on or off the game whenever we want
        self.play = False

        #Start the tk window
        self.window.mainloop()

    def movimiento(self):
        """
        Function which will perform the main actions of the game:
            -Move the Snake, if it can eat it will
            -If the snake collides, kill it

        """
        self.snake.move()
        self.draw()

        if self.apple.pos == self.snake.head.pos:



            #La manzana ha sido comida, entonces debemos buscar una nueva posicion para la manzana

            self.apple.pos = (random.choice(posiciones), random.choice(posiciones))
            self.snake.eat_apple()

            n = len(self.snake.tail)

            self.cantidad['text'] = 'Cantidad 🍎 : {}'.format(n)


            if self.snake.pos_in_snake(self.apple.pos):
                self.canvas.coords(self.canvas.find_withtag("food"), self.apple.pos)

           # self.canvas.create_text(*self.snake.tail[-1].pos, text='▀', fill='green2', font=('Arial', 20), tag='snake')

        if self.snake.head_collide_tail():
            self.cruzar_snake()
        if self.snake.head.pos[0] < 15 or self.snake.head.pos[0] > 465 :
            self.cruzar_snake()
        if self.snake.head.pos[1] < 15 or self.snake.head.pos[1] > 465:
            self.cruzar_snake()

        if self.play:
            self.cantidad.after(300, self.movimiento)

    def cruzar_snake(self):
        self.play = False
        self.canvas.delete(ALL)
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, text=f"Intentelo\n de Nuevo \n\n 🍎",
                           fill='red', font=('Arial', 20, 'bold'))

    def salir(self):
        self.window.destroy()
        self.window.quit()

    def play(self):
        self.play = True
        self.canvas.delete(ALL)

        # Add the Snake and Apple objects
        self.snake = snake("right", (75, 75), 10)
        self.apple = apple((255, 75))

        n = len(self.snake.tail)
        self.cantidad['text'] = 'Cantidad 🍎 : {}'.format(n)

        self.movimiento()


    def draw(self):
        self.canvas.delete("all")
        # Draw the squares with Canvas
        for i in range(0, 460, 30):
            for j in range(0, 460, 30):
                self.canvas.create_rectangle(i, j, i + 30, j + 30, fill='gray')

        self.canvas.create_text(self.apple.pos[0], self.apple.pos[1], text='🍎', fill='red2', font=('Arial', 18),
                                tag='food')

        posiciones_snake = [self.snake.head.pos]
        if len(self.snake.tail) > 0:
            for cola in self.snake.tail:
                posiciones_snake.append(cola.pos)

        self.canvas.create_text(posiciones_snake[0][0], posiciones_snake[0][1], text='▀', fill='green', font=('Arial', 18, 'bold'),
                                tag='food')
        for parte in posiciones_snake[1:]:
            self.canvas.create_text(parte[0], parte[1], text='▀', fill='green', font=('Arial', 18,'bold'),
                                    tag='food')

