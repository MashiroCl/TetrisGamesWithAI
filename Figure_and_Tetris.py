import random
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]

class Figure:
    #x y represents the current position of the figure
    x=0
    y=0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self,x,y):
        self.x=x
        self.y=y

        #randomly pick a type and color
        self.type=random.randint(0,len(self.figures)-1)
        self.color=random.randint(1,len(colors)-1)
        self.rotation=0

    #return type and the rotation of the figure
    def image(self):
        return self.figures[self.type][self.rotation]

    #return the shape after rotation
    def rotate(self):
        len_types=len(self.figures[self.type])
        self.rotation=(self.rotation+1)%len_types

class Tetris:
        #Variable control speed, higher level higher speed
        level = 2
        #User score
        score=0

        state = "start"
        field=[]
        height=0
        width=0
        x=100
        y=60
        zoom=20
        figure=None

        #filled the whole screen with 0
        def __init__(self,height,width):
            self.height=height
            self.width=width
            self.field=[]
            self.score=0
            self.state="start"
            for i in range (height):
                temp_line=[]
                for j in range(width):
                    temp_line.append(0)
                self.field.append(temp_line)

        #create a new figure at the top middle of the screen
        def new_figure(self):
            self.figure=Figure(3,0)

        """
        Check each cell in the 4*4 matrix of the current Figure
        Whether it is out of the bound or collapse with other field
        """
        def intersects(self):
            intersection=False
            for i in range(4):
                for j in range(4):
                    if i*4 + j in self.figure.image():
                        if i+self.figure.y>self.height-1\
                            or j+self.figure.x >self.width -1 \
                               or j+self.figure.x <0 \
                            or self.field[i+self.figure.y][j+self.figure.x]>0:
                            intersection=True
            return intersection

        #Figure reach the bottom or intersect with other figures
        def freeze(self):
            for i in range(4):
                for j in range(4):
                    if i*4 + j in self.figure.image():
                        self.field[i+self.figure.y][j+self.figure.x]=\
                        self.figure.color
            self.break_lines()
            self.new_figure()
            if self.intersects():
                self.state="gameover"

        #From bottom to top, check wheteher the line is full with figure
        #If it is full, clear it and the line one it comes down
        def break_lines(self):
            lines=0
            for i in range(1,self.height):
                zeros=0
                for j in range(self.width):
                    if self.field[i][j]==0:
                        zeros+=1
                if zeros==0:
                        lines+=1
                        for i1 in range(i,1,-1):
                            for j in range(self.width):
                                self.field[i1][j]=self.field[i1-1][j]
            self.score+=lines**2

        #Moving control of the figures
        def go_space(self):
            while not self.intersects():
                self.figure.y+=1
            self.figure.y-=1
            self.freeze()

        def go_down(self):
            self.figure.y+=1
            if self.intersects():
                self.figure.y-=1
                self.freeze()

        def go_side(self,dx):
            old_x=self.figure.x
            self.figure.x+=dx
            if self.intersects():
                self.figure.x=old_x

        def rotate(self):
            old_rotation=self.figure.rotation
            self.figure.rotate()
            if self.intersects():
                self.figure.rotation=old_rotation