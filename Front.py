from Car import Car
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Front(Car):
    

    @staticmethod
    def Interface():
        root = Tk()
        root.title("Race")
        root.geometry("1000x700")

        #def Gear_Output(output):
        #    gear_g1.insert('end', f'{output}')
        #def Speed_Output(output):
        #    speed_s1.insert('end', f'{output}')
        #def Distance_Output(output):
        #    distance_d1.insert('end', f'{output}')

        def start_race():
            timer.config(state = 'normal')
            Car.start()
            data = raw_input()
            timer.insert(1.0, data)
            timer.config(state = 'disabled')

        def clear_textbox():
            gear_g1.config(state = 'normal')
            gear_g1.delete(1.0, 'end')
            gear_g1.insert('end', "N")
            gear_g1.config(state = 'disabled')

            speed_s1.config(state = 'normal')
            speed_s1.delete(1.0, 'end')
            speed_s1.insert('end', "0")
            speed_s1.config(state = 'disabled')

            distance_d1.config(state = 'normal')
            distance_d1.delete(1.0, 'end')
            distance_d1.insert('end', "{}".format(Car.way))
            distance_d1.config(state = 'disabled')

        label_r1 = Label(text="Racer #1:", fg = "black", font= ('Times New Roman', 16))
        label_r1.place(x=50, y=60)
        label_r2 = Label(text="Racer #2:", fg = "black", font= ('Times New Roman', 16))
        label_r2.place(x=700, y=60)

        label_g1 = Label(text="Gear:", fg = "black", font= ('Times New Roman', 16))
        label_g1.place(x=50, y=130)
        label_s1 = Label(text="Speed:", fg = "black", font= ('Times New Roman', 16))
        label_s1.place(x=50, y=220)
        label_d1 = Label(text="Distance:", fg = "black", font= ('Times New Roman', 16))
        label_d1.place(x=50, y=310)

        label_g2 = Label(text="Gear:", fg = "black", font= ('Times New Roman', 16) )
        label_g2.place(x=700, y=130)
        label_s2 = Label(text="Speed:", fg = "black", font= ('Times New Roman', 16))
        label_s2.place(x=700, y=220)
        label_d2 = Label(text="Distance:", fg = "black", font= ('Times New Roman', 16))
        label_d2.place(x=700, y=310)

        gear_g1 = Text(root, height = 1, width = 3, font= ('Times New Roman', 24))
        gear_g1.pack(expand = True)
        gear_g1.insert('end', "N")
        gear_g1.config(state = 'disabled')
        gear_g1.place(x=50, y=160)

        speed_s1 = Text(root, height = 1, width = 4, font= ('Times New Roman', 24))
        speed_s1.pack(expand = True)
        speed_s1.insert('end', "0")
        speed_s1.config(state = 'disabled')
        speed_s1.place(x=50, y=250)

        distance_d1 = Text(root, height = 1, width = 5, font= ('Times New Roman', 24))
        distance_d1.pack(expand = True)
        distance_d1.insert('end', "{}".format(Car.way))
        distance_d1.config(state = 'disabled')
        distance_d1.place(x=50, y=340)

        gear_g2 = Text(root, height = 1, width = 3, font= ('Times New Roman', 24))
        gear_g2.pack(expand = True)
        gear_g2.insert('end', "N")
        gear_g2.config(state = 'disabled')
        gear_g2.place(x=700, y=160)

        speed_s2 = Text(root, height = 1, width = 4, font= ('Times New Roman', 24))
        speed_s2.pack(expand = True)
        speed_s2.insert('end', "0")
        speed_s2.config(state = 'disabled')
        speed_s2.place(x=700, y=250)

        distance_d2 = Text(root, height = 1, width = 5, font= ('Times New Roman', 24))
        distance_d2.pack(expand = True)
        distance_d2.insert('end', "{}".format(Car.way))
        distance_d2.config(state = 'disabled')
        distance_d2.place(x=700, y=340)

        winner_l = Label(text="Winner of the race:", fg = "black", font= ('Times New Roman', 16) )
        winner_l.place(x=400, y=460)

        winner_m = Text(root, height = 1, width = 40, font= ('Times New Roman', 24))
        winner_m.pack(expand = True)
        winner_m.insert('end', "")
        winner_m.config(state = 'disabled')
        winner_m.place(x=200, y=500)

        btn1 = Button(
             text="Start Race",
			 background="dodger blue",
			 foreground="azure",
			 padx="25",
			 pady="10",
			 command=start_race )
        btn1.place(x=445, y=55)
        btn2 = Button(
             text="Restart Race",
			 background="dodger blue",
			 foreground="azure",
			 padx="25",
			 pady="10",
			 command=print())
        btn2.place(x=440, y=110)
        btn3 = Button(
             text="Clear",
			 background="dodger blue",
			 foreground="azure",
			 padx="25",
			 pady="10",
			 command=clear_textbox)
        btn3.place(x=460, y=165)
        btn4 = Button(
             text="Exit",
			 background="dodger blue",
			 foreground="azure",
			 padx="25",
			 pady="10",
			 command=sys.exit )
        btn4.place(x=460, y=220)

        list_of_cars = ttk.Combobox(values = Car.cars_front, width=20, font= ('Times New Roman', 16) )
        list_of_cars.config(state = 'readonly')
        list_of_cars.place(x=50, y=90)

        list_of_cars = ttk.Combobox(values = Car.cars_front, width=20, font= ('Times New Roman', 16))
        list_of_cars.config(state = 'readonly')
        list_of_cars.place(x=700, y=90)

        timer = Text(root, height = 5, width = 10, font= ('Times New Roman', 24))
        timer.pack(expand = True)
        timer.config(state = 'disabled')
        timer.place(x=420, y=300)

        try:
            root.mainloop()
        except:
            sys.exit()

    