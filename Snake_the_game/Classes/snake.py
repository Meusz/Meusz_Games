#Head sprites
head_up = "(··)"
head_down = "(··)"
head_right = "(:)"
head_left = "(:)"
#Middle Tail Sprites
middle_tail_up = "||"
middle_tail_down = "||"
middle_tail_right = "="
middle_tail_left = "="
#Last Tail Sprite
last_tail_up = "v"
last_tail_down = "^"
last_tail_right = ">"
last_tail_left = "<"

class head:
    def __init__(self,direction,pos):
        self.direction = direction  # Valid values: up down right left
        self.pos = pos


class tail:
    def __init__(self,direction,pos,last):
        self.direction = direction  # Valid values: up down right left
        self.pos = pos
        self.last = last    #True if it's the last tail piece


class snake:
    def __init__(self,direction,pos,speed):
        self.head = head(direction, pos)
        self.speed = speed
        self.tail = [] #This array will keep the position of the tail

    def set_direction(self,new_direction):
        if( not (self.head.direction == "up" and new_direction == "down") and
            not (self.head.direction == "down" and new_direction == "up") and
            not (self.head.direction == "right" and new_direction == "right") and
            not (self.head.direction == "left" and new_direction == "left") ):
            self.head.direction = new_direction

    def refresh_tail(self):
        if len(self.tail) > 1 :
            new_tail = tail(self.head.direction, self.head.pos, True)
            list_tail = []

            iterator = len(self.tail)-1
            while (iterator > 0):

                list_tail = [self.tail[iterator - 1]] + list_tail  # The tail at that position takes the value of the following tail
                # if iterator == len(self.tail) -1:
                #    self.tail[iterator].last = True             #If it's the last one we have to set to True the last value
                iterator -= 1
            self.tail = [new_tail] + list_tail

        elif len(self.tail) > 0:
            new_tail = tail(self.head.direction, self.head.pos, False)
            self.tail = [new_tail]

    def pos_in_snake(self,pos):
        if self.head.pos == pos:
            return True
        else:
            for t in self.tail:
                if t.pos == pos:
                    return True
        return False
    def eat_apple(self):
        self.tail.append(tail(0,0,False))

    def head_collide_tail(self):
        rturn = False
        if len(self.tail) > 2:
            t = 0
            while(t < len(self.tail) and not rturn):
                rturn = self.head.pos == self.tail[t].pos
                t += 1
        return rturn

    def move(self):
        if self.head.direction == "up":
            self.move_up()
        elif self.head.direction == "down":
            self.move_down()
        elif self.head.direction == "left":
            self.move_left()
        elif self.head.direction == "right":
            self.move_right()


    def move_up(self):
        self.refresh_tail()
        self.head.pos = (self.head.pos[0],self.head.pos[1] - 30)


    def move_down(self):
        self.refresh_tail()
        self.head.pos = (self.head.pos[0],self.head.pos[1] + 30)


    def move_right(self):
        self.refresh_tail()
        self.head.pos = (self.head.pos[0] + 30 ,self.head.pos[1])

    def move_left(self):
        self.refresh_tail()
        self.head.pos = (self.head.pos[0] - 30 ,self.head.pos[1])






