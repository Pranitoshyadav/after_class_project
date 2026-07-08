class circle:
    def __init__(self):
        
        self.r = ""

    def radius(self):
        r = input("enter the radius : ")


    def circle_peremeter(self):
        print("the peremeter is : ", 2*3.14*self.r)

    
    def circlr_area(self):
        print("the area is : ", 2*3.14*self.r)

c = circle()

c.radius()
c.circle_peremeter()
c.circlr_area()