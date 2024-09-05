class time:
    """this is the blueprint of time"""

    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print(self.hour, ":", self.minute, ":", self.second)


mytime1 = time()
mytime1.print_time()
mytime1.set_time(1, 2, 3)
mytime1.print_time()
