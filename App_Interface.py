import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from PIL import Image, ImageTk

class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor App")

        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Add tabs
        self.create_tab("Cut Images", self.cut_images_tab)
        self.create_tab("Process Images", self.process_images_tab)

    def create_tab(self, tab_name, tab_function):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=tab_name)
        tab_function(tab)

    def cut_images_tab(self, tab):
        # UI elements for the "Cut Images" tab
        label = ttk.Label(tab, text="Select images to cut:")
        label.pack(pady=10)

        self.folder_path_var = tk.StringVar()
        entry = ttk.Entry(tab, textvariable=self.folder_path_var, state="readonly")
        entry.pack(pady=5, side=tk.LEFT, padx=5)

        browse_button = ttk.Button(tab, text="Browse", command=self.browse_folder)
        browse_button.pack(pady=5, side=tk.LEFT)

        cut_button = ttk.Button(tab, text="Cut Images", command=self.cut_images)
        cut_button.pack(pady=10)

    def process_images_tab(self, tab):
        # UI elements for the "Process Images" tab
        label = ttk.Label(tab, text="Select folder to process images:")
        label.pack(pady=10)

        self.folder_path_var_process = tk.StringVar()
        entry_process = ttk.Entry(tab, textvariable=self.folder_path_var_process, state="readonly")
        entry_process.pack(pady=5, side=tk.LEFT, padx=5)

        browse_button_process = ttk.Button(tab, text="Browse", command=self.browse_folder_process)
        browse_button_process.pack(pady=5, side=tk.LEFT)

        process_button = ttk.Button(tab, text="Process Images", command=self.process_images)
        process_button.pack(pady=10)

        # Placeholder for image display
        self.image_label = ttk.Label(tab)
        self.image_label.pack(pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path_var.set(folder_selected)

    def cut_images(self):
        # Implement your image cutting code here using self.folder_path_var.get()
        # Update this method based on your first code

        # Example:
        # folder_path = self.folder_path_var.get()
        # Your image cutting code goes here

        print("Cutting images...")

    def browse_folder_process(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path_var_process.set(folder_selected)

    def process_images(self):
        # Implement your image processing code here using self.folder_path_var_process.get()
        # Update this method based on your second code

        # Example:
        # folder_path = self.folder_path_var_process.get()
        # Your image processing code goes here

        # Placeholder for image display
        self.display_image_placeholder()

        print("Processing images...")

    def display_image_placeholder(self):
        # Placeholder for displaying processed image
        image_path = "path_to_processed_image.png"  # Update this with the actual path
        image = Image.open(image_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Update label with the new image
        self.image_label.config(image=photo)
        self.image_label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
