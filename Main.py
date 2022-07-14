from Car import Car
from Front import Front
#from multiprocessing import Process
from threading import Thread

car_a = Car("Toyota Chaser Tourer V", 265, "RWD", {60: 7.9, 120: 5.4, 180: 3.3, 240: 2, 265: 1.6}, 600, (3.5, 11.8))
car_b = Car("Audi RS4", 270, "AWD", {60: 9.9, 100: 7.9, 160: 4.8, 200: 4.2, 240: 1.9, 270: 1}, 625, (2.8, 10.8))

#S = 804 м, t = 18 c, 100 - 3,5 , 200 - 11,8 v_max = 237 км\ч    60: 3.4, 120: 2.2, 180: 1.3, 240: 1, 265: 0.8
#S = 804 м, t = 17,5 c, 100 - 3 , 200 - 12 v_max = 245 км\ч      60: 3.7, 100: 2.5, 160: 1.5, 200: 1.2, 240: 1, 270: 0.8

i = 0
#proc = []
thr = []

#Front.Interface()

if __name__ == '__main__':
    Car.start()
    for obj in Car.cars:
        #proc.append(Process(target = obj.race))
        thr.append(Thread(target = obj.race))
        #print(f'{Car.cars[i].model}, {Car.cars[i].engine}')
    
    thr[0].start()
    thr[1].start()

    #proc[0].start()
    #proc[1].start()

    #for p in proc:
    #    p.start()
    #for p in proc:
    #    p.join()





#car_a.race()
#car_b.race()


#car_a.wheel_drive()

#print(car_a.gearbox[60])

#print(car_a.start_delay())
#print(car_b.start_delay())
#car_a.start()
#car_a.race(car_a.max_speed)
#car_a.stop()


