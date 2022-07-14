import time
import random

class Car():
    gear_delay = 0.2
    way = 1609 #804
    cars = []
    cars_front = []

    def __init__(self, model, max_speed, wd, gearbox, engine, dynamic):
        self.model = model
        self.max_speed = max_speed
        self.wd = wd
        self.gearbox = gearbox
        self.engine = engine #torque
        self.dynamic = dynamic
        Car.cars.append(self)
        Car.cars_front.append(self.model)

    def __str__(self):
        return f'{self.model}, {self.max_speed}, {self.wd}, {self.gearbox}, {self.engine}, {self.dynamic}'

    def start_delay(self):
        start_delay = random.randrange(0, 4, 1) * 0.1
        return start_delay

    def speed_random(self):
        speed_random = random.randrange(95, 100, 1) * 0.01
        return speed_random

    def wheel_drive(self):
        if(self.wd == "RWD"):
            self.gearbox[60] = self.dynamic[0] * 0.6 + random.randrange(0, 3, 1) * 0.1
            self.gearbox.update()
        if(self.wd == "FWD"):
            self.gearbox[60] = self.dynamic[0] * 0.6 + random.randrange(0, 3, 1) * 0.1
            self.gearbox.update()
        if(self.wd == "AWD"):
            self.gearbox[60] = self.dynamic[0] * 0.6 + 0.1
            self.gearbox.update()

    @staticmethod
    def start():
        # i - timer
        i = 3
        print("All cars on a start")
        while i > 0:
            print(i)
            i -= 1
            time.sleep(1)
        print("GO!")

    def race(self):
        way = 1609 #804
        # j - gears, v - speed, s - way, sk - gearbox 
        v = 0
        j = 1
        s = 0
        sk = list(self.gearbox.keys())  #уточнть
        
        #ограничитель преедач
        time.sleep(self.start_delay())
        while j <= len(self.gearbox):
            print("{} Gear".format(j))
            time.sleep(self.gear_delay)
            while v <= sk[j - 1]:
                time.sleep(1)
                s += (self.gearbox[sk[j - 1]] - v) / 2 + v
                v += self.gearbox[sk[j - 1]] / 1000 * 3600 * self.speed_random()
                if s >= way:
                    s = way
                if v > self.max_speed:
                    v = self.max_speed
                if v > sk[j - 1] and j != len(self.gearbox):
                    v = sk[j - 1] - random.randrange(1, 5, 1)
                    print("{0} speed is {1} km/h. {2} meters till finish".format(self.model, int(v), int(way - s)))
                    break
                else:
                    print("{0} speed is {1} km/h. {2} meters till finish".format(self.model, int(v), int(way - s)))
                    if s >= way:
                        break
                
            j += 1
            if s >= way:
                break

        print("{0} reached the finish line at speed of {1} km/h".format(self.model, int(v)))

    def engine_start(self):
        print("Engine started")

    def engine_stop(self):
        print("Engine stopped")
