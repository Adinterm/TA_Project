 
import sys, os, glob, time
import tkinter as tk
from tkinter import Label, ttk
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

file_list = [1,2,3,4,5,6,7,8,9]
screen_size = "1366x768"
# User Interface Properties
class ImageProcess:
    def __init__(self, master ):

        self.master = master
 
        self.properties()
        self.main_window()
        self.create_widgets()
    
    def properties(self):
        #Position
        self.posbel_x = 0.84
        self.postry_x = 0.89

        self.pos_yinput = 0.01
        self.distance = 0.07

        #Details
        self.fg1 = "black"
        self.green_color = "#30bd09"
        self.font1 = ('Times New Roman', 9, 'bold')
        self.font2 = ('Times New Roman', 11)
        self.font3 = ("Helvetica", 10)
        self.font4 = ("Arial", 12)

        self.data_options = ('data1', 'data2', 'data3')

    def create_widgets(self):
        data_labels = ['Data 1', 'Data 2', 'Data 3']

        for col, label in enumerate(data_labels, start=1):
            ttk.Label(self.master, text=label, font=self.font1).place(relx=(self.posbel_x + 0.008 + (col-1)*0.047), rely=0.002)
            data_var = tk.StringVar()
            data_opts = ttk.Combobox(self.master, width=6, textvariable=data_var, state='readonly')
            data_opts.place(relx=(self.posbel_x + 0.002 + (col-1)*0.047), rely=self.pos_yinput+0.02)
            data_opts['values'] = self.data_options
            data_opts.current(1)


    def get_data(self):
        self.selected_data = [child.get() for child in self.master.winfo_children() if isinstance(child, ttk.Combobox)]
        print("Selected Data:", self.selected_data)

    def loading_process(self):
        total_length = eval(screen_size[:4])  # Total length of the loading bar
        # Create a progress bar
        self.progress_bar = tk.Canvas(self.master, width=total_length, height=20, bg="white")
        self.progress_bar.pack(side=tk.BOTTOM)

        # Loading label
        self.loading_label = tk.Label(self.master, text="Processing...", font=self.font4)
        self.loading_label.pack(side=tk.BOTTOM)

        #input part
        location = (self.location_entry)
        time_zone = [self.time_entry]
        date = [self.date_entry]
        ar_peak = []
        elvt = []
        c = []



        i = 0
        rgb_val_r = []
        rgb_val_g = []
        rgb_val_b = []
        
        for file in file_list:
            i += 1
            #progress bar
            progress = int((i / len(file_list)) * total_length)
            self.progress_bar.delete("progress")
            self.progress_bar.create_rectangle(0, 0, progress, 20, fill=self.green_color, tags="progress")
            percent = int((i / len(file_list)) * 100)
            #self.master.title(f"Loading... {percent}% complete")
            self.master.update()  # Update the window
            #time.sleep(0.01)

            # calling functions from main module to get the data
            # rgb_val_r.append(rgb_value(file, 'r'))
            # rgb_val_g.append(rgb_value(file, 'g'))
            # rgb_val_b.append(rgb_value(file, 'b'))

        #self.master.title("Complete!")
        self.loading_label.destroy()

        self.x = [1,2,3,4,5,6,7,8,9]
        self.y1 = [1,2,3,9,5,6,7,8,9]
        self.y2 = [1,9,3,4,5,6,7,8,9]
        self.y3 = [1,2,3,4,5,6,7,8,9]

    def plot_data(self):
        #initial input data
        x = self.x
        y1 = self.y1 # get_all_value(img_type_input)
        y2 = self.y2
        y3 = self.y3
        
        # Create a figure and axes
        fig, ax = plt.subplots()
        
        # Plot the data
        ax.plot(x, y1, label='Data RGB')
        ax.plot(x, y2, label='Data HSV')
        ax.plot(x, y3, label='Data FT')
        
        # Set the title and labels
        ax.set_title("Grafik Perbandingan Data")
        ax.set_xlabel("Altitude")
        ax.set_ylabel("Value")
        
        # Add a legend
        ax.legend()
        
        # Create a Tkinter canvas and display the plot
        canvas = FigureCanvasTkAgg(fig, master= self.master)
        canvas.draw()
        canvas.get_tk_widget().place(x=0.84, y=0, relwidth=0.82, relheight=0.87)

        self.get_data()

    def data_details(self):
        data = [
            f"Data Details :",
            f"Total Files : {len(file_list)}",
            f"Image Size : "#{Image.open(file_list[0]).size}",
            f"Average Size : {len(file_list)}",
            f"Location : {str(self.location_entry.get())}",
            f"Date : {str(self.date_entry.get())}",
            f"Time : {str(self.time_entry.get())}"
        ]

        for idx, detail in enumerate(data, start=5):
            if idx == 5:
                label = Label(self.master, text=detail, font=('Arial', 12, 'bold'), fg=self.fg1)
                label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*idx)+0.02)
            else :
                label = Label(self.master, text=detail, font=self.font2, fg=self.fg1)
                label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*idx))

    def button_clicked(self):
        #process button to run the application
        self.process_button.config(state="disable")
        self.process_button.config(bg="white")
        self.loading_process()
        if self.progress_bar is not None:
            self.progress_bar.destroy()
            self.progress_bar = None
        self.process_button.config(state="normal")
        self.process_button.config(bg=self.green_color)
        #self.master.title("Complete")
        self.get_data()
        
        self.plot_data()
        self.data_details()
    
    def save_plt_data(self):
        print()

    def main_window(self):
        #1st frame, plot

        # Create the input fields and process button on the right
        location_label = tk.Label(self.master, text="Location :")
        location_label.place(relx=self.posbel_x, rely=self.pos_yinput+self.distance)
        self.location_entry = tk.Entry(self.master)
        self.location_entry.place(relx=self.postry_x, rely=self.pos_yinput+self.distance)

        date_label = tk.Label(self.master, text="Date :")
        date_label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*2))
        self.date_entry = tk.Entry(self.master)
        self.date_entry.place(relx=self.postry_x, rely=self.pos_yinput+(self.distance*2))

        time_label = tk.Label(self.master, text="Time :")
        time_label.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*3))
        self.time_entry = tk.Entry(self.master)
        self.time_entry.place(relx=self.postry_x, rely=self.pos_yinput+(self.distance*3))

        self.process_button = tk.Button(self.master, text="Process", bg=self.green_color, command=self.button_clicked)
        self.process_button.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*4), relwidth=0.143, relheight=0.05)

        self.save_button = tk.Button(self.master, text="Save Graph", command=self.save_plt_data)
        self.save_button.place(relx=self.posbel_x, rely=self.pos_yinput+(self.distance*11.6), relwidth=0.143, relheight=0.05)


        #3rd frame, Details

if __name__ == "__main__":
    file_list = [1,2,3,4,5,6,7,8,9]


    #window properties
    screen_size = "1366x768"
    root = tk.Tk()
    root.title("Data Processing")
    root.geometry(screen_size)
    
    ImageProcess(root )
    root.protocol("WM_DELETE_WINDOW", root.quit) #to avoid error during closing the app

    # Start the Tkinter event loop
    root.mainloop()
