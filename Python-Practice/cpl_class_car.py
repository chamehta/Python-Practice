class cars:
    def __init__(self):
        self.color = "white"
        self.doors = "fixed4"
        self.stearing = "power"

    def modify_stearing(self, stearing):
        self.stearing = stearing

    def modify_color(self, color):
        self.color = color

    def modify_doors(self, doors):
        self.doors = doors

    def manufacture_car(self):
        print(self.color, ' ', self.doors, ' ', self.stearing)

    my_car = cars()
    my_car.manufacture_car()
