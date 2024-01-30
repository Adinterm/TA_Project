import tkinter as tk
from tkinter import ttk
import os, glob, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# set the working directory
try:
    os.chdir(f"{os.path.dirname(os.path.realpath(__file__))}/data")
 
    print(f"work on {os.getcwd()}")
except:
    print("wrong directory")

#get files
file_list = sorted(glob.glob('*.JPG'))
print(f"with {len(file_list)} image data")

#import program modules
from interface_setup.image_crop import ImageCropApp
from interface_setup.image_process import ImageProcess
 
#Interface Properties
screen_size = "1366x768"
root = tk.Tk()
root.title("Data Processing")
root.geometry(screen_size)

class Window_App:
    def __init__(self, root):
        self.root = root

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs
        self.create_tab("Cut Images", ImageCropApp)
        self.create_tab("Process Images", ImageProcess )

    def create_tab(self, tab_name, tab_function):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_name)
        tab_function(tab)


if __name__ == "__main__":
    app = Window_App(root)
    #Avoid error quit
    root.protocol("WM_DELETE_WINDOW", root.quit)
    #Start the Tkinter event loop
    root.mainloop()
