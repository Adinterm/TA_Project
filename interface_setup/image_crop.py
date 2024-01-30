import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageCropApp:
    def __init__(self, master):
        self.master = master

        pos_x = 0.1
        pos_y = 0.7

        self.input_folder_path = None
        self.output_folder_path = None
        self.image_paths = []
        self.original_images = []
        self.displayed_image = None
        self.cropped_images = []

        # Create widgets
        self.import_folder_button = tk.Button(master, text="Import Folder", command=self.refresh_ui)
        self.import_folder_button.grid(column=0, row=1)

        self.crop_button = tk.Button(master, text="Crop", command=self.crop_images)
        self.crop_button.grid(column=0, row=2)

        self.save_button = tk.Button(master, text="Save Images", command=self.save_images)
        self.save_button.grid(column=0, row=3)

        self.top_entry = tk.Entry(master, width=10)
        self.bottom_entry = tk.Entry(master, width=10)
        self.right_entry = tk.Entry(master, width=10)
        self.left_entry = tk.Entry(master, width=10)

        self.top_label = tk.Label(master, text="Top:")
        self.bottom_label = tk.Label(master, text="Bottom:")
        self.right_label = tk.Label(master, text="Right:")
        self.left_label = tk.Label(master, text="Left:")

        self.top_label.place(relx=pos_x, rely=pos_y)
        self.top_entry.place(relx=pos_x+0.1, rely=pos_y)
        self.bottom_label.place(relx=pos_x+0.2, rely=pos_y)
        self.bottom_entry.place(relx=pos_x+0.3, rely=pos_y)
        self.right_label.place(relx=pos_x+0.4, rely=pos_y)
        self.right_entry.place(relx=pos_x+0.5, rely=pos_y)
        self.left_label.place(relx=pos_x+0.6, rely=pos_y)
        self.left_entry.place(relx=pos_x+0.7, rely=pos_y)

    def refresh_ui(self):
        # Reset UI components
        if hasattr(self, 'image_label'):
            self.image_label.destroy()

        self.input_folder_path = None
        self.output_folder_path = None
        self.image_paths = []
        self.original_images = []
        self.displayed_image = None
        self.cropped_images = []

        # Call the import_folder method to import images again
        self.import_folder()

    def import_folder(self):
        self.input_folder_path = filedialog.askdirectory(title="Select Input Folder")
        if self.input_folder_path:
            self.output_folder_path = os.path.join(self.input_folder_path, "cropped_images")
            os.makedirs(self.output_folder_path, exist_ok=True)

            self.image_paths = [os.path.join(self.input_folder_path, file) for file in os.listdir(self.input_folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

            if not self.image_paths:
                print("No valid images found in the selected folder.")
                return

            first_image = Image.open(self.image_paths[0])  # Use the first image path in the list
            original_width, original_height = first_image.size
            aspect_ratio = original_width / original_height
            new_height = 300
            new_width = int(new_height * aspect_ratio)

            resized_image = first_image.resize((new_width, new_height))

            self.original_images = [resized_image for image_path in self.image_paths]
            self.displayed_image = ImageTk.PhotoImage(self.original_images[0])

            self.image_label = tk.Label(self.master, image=self.displayed_image)
            self.image_label.place(relx=0.1,rely=0.1)

    def crop_images(self):
        try:
            top = int(self.top_entry.get())
            bottom = int(self.bottom_entry.get())
            right = int(self.right_entry.get())
            left = int(self.left_entry.get())

            self.cropped_images = [original_image.crop((left, top, original_image.width - right, original_image.height - bottom)) for original_image in self.original_images]

            cropped_image_tk = ImageTk.PhotoImage(self.cropped_images[0])
            self.image_label.config(image=cropped_image_tk)
            self.image_label.image = cropped_image_tk  # Keep a reference to prevent garbage collection

        except ValueError:
            print("Invalid input. Please enter numeric values for crop coordinates.")

    def save_images(self):
        if self.cropped_images:
            for i, cropped_image in enumerate(self.cropped_images):
                save_path = os.path.join(self.output_folder_path, f"cropped_image_{i+1}.png")
                cropped_image.save(save_path)
                print(f"Image {i+1} saved to: {save_path}")
        else:
            print("No images to save. Please import and crop images first.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image Crop App")
    root.geometry("800x600")
    app = ImageCropApp(root)
    root.mainloop()
    