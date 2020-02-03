from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',{'name':'nive'})

class Rover(object):

    def __init__(self,x,y,direction,m_x,m_y,r_id):
        self.directions=('n','e','s','w')
        self.u_x=int(x)
        self.u_y=int(y)
        self.dir=direction
        self.m_x=m_x
        self.m_y=m_y
        self.r_id=r_id


    def updated_rover_position(self):
        return self.u_x,self.u_y,self.u_dir


    def turnLeft(self):
        if self.dir=='n':
            self.dir=self.directions[-1]
            # print(self.dir,"--u_dir--left->")
            # self.updated_directions(self.u_dir)
            # self.updated_rover_position.up_dir = u_dir
        else:
            self.dir=self.directions[self.directions.index(self.dir)-1]
            # print(self.dir,"--u_dir---left->")



    def turnRight(self):
        if self.dir=='w':
            self.dir=self.directions[0]
            # print(self.dir,"--u_dir---right-->")

        else:
            self.dir=self.directions[self.directions.index(self.dir)+1]
            # print(self.dir,"--u_dir--right-->")


    def moveForward(self):
        if self.dir=='n':
            self.u_y=self.u_y+1
            # print(self.u_y,"--y--moveforward---")
        elif self.dir== 'e':
            self.u_x=self.u_x+1
            # print(self.u_x, "--x--moveforward---")
        elif self.dir=='s':
            self.u_y=self.u_y-1
            # print(self.u_y, "--y--moveforward---")
        elif self.dir== 'w':
            self.u_x=self.u_x-1
            # print(self.u_x, "--x--moveforward---")

        # self.updated_coordinates(u_x,u_y)

    def make_movement(self,move_input):
        for i in move_input:
            if i== 'r':
                self.turnRight()
            elif i == 'l':
                self.turnLeft()
            elif i == 'm':
                self.moveForward()


    def move_rover(self):
        move_input=input("\n enter series of rover movement with space separated [ r = turnRight,l = turnLeft, m = moveForward ]: ").split()
        self.make_movement(move_input)



def validate_rover(x,y,dir):
    directions=('n','e','w','s')
    if x>=0 and x<=5 and y>=0 and y<=5 and dir in directions:
        return x,y,dir
    else:
        print("wrong input")



def add_rover():
    mars_x=5
    mars_y=5

    while True:

        try:
            rov=input("\n enter rovers current position space separated [x-axis,y-axis,direction]: ").split()
            print(rov)
            if len(rov)==3 and validate_rover(int(rov[0]),int(rov[1]),rov[2]):
                # print("yes ")
                r_id=id(rov)
                # print(r_id,"----r id---")
                r=Rover(rov[0],rov[1],rov[2],mars_x,mars_y,r_id)
                r.move_rover()
                print("\n final position x-axis: {} , y-axis: {} , dir facing: {} ".format(r.u_x,r.u_y,r.dir))

                break
            else:
                print("no")



        except:
            print("some error occured")

add_rover()