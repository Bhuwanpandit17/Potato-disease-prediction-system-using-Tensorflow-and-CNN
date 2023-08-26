import tkinter as tk
from tkinter import filedialog
import tensorflow as tf
import numpy as np
from PIL import Image, ImageTk


class ImageClassificationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Classification")
        master.configure(bg="#f7f7f7")

        # Load the pre-trained model and classes
        self.model = tf.keras.models.load_model('./potatoes.h5')
        # Manual class input
        self.classes = ['Potato___Early_blight',
                        'Potato___healthy', 'Potato___Late_blight']

        # Create the widgets
        self.label1 = tk.Label(master, text="Select an image to classify:",
                               bg="#f7f7f7", font=("Helvetica", 16, "bold"))
        self.label1.pack(pady=(20, 0))
        self.button1 = tk.Button(master, text="Choose File", command=self.load_image,
                                 bg="#0077cc", fg="white", font=("Helvetica", 14, "bold"), padx=20)
        self.button1.pack(pady=20)
        self.image_label = tk.Label(master, bg="#f7f7f7")
        self.image_label.pack()
        self.result_label = tk.Label(
            master, bg="#f7f7f7", font=("Helvetica", 14, "bold"))
        self.result_label.pack(pady=(20, 0))

    # Load the selected image and classify it
    def load_image(self):
        # Open the file dialog to choose an image file
        filename = filedialog.askopenfilename(initialdir=".", title="Select Image File",
                                              filetypes=(("Image Files", "*.png;*.jpg;*.jpeg"), ("All Files", "*.*")))
        if filename:
            # Load and display the selected image
            image = Image.open(filename)
            image.thumbnail((400, 400))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

            # Preprocess the image and classify it
            tensor = self.preprocess_image(image)
            predicted_class = self.predict(tensor)

            # Display the classification result
            result_text = f"The image is classified as {predicted_class}."
            self.result_label.configure(text=result_text)

    # Preprocess the image for input to the model
    def preprocess_image(self, image):
        image_array = np.array(image)
        image_array = np.expand_dims(image_array, axis=0)
        image_array = image_array.astype('float32') / 255
        tensor = tf.convert_to_tensor(image_array)
        return tensor

    # Predict the class label for the input image
    def predict(self, tensor):
        prediction = self.model.predict(tensor)
        predicted_class_index = np.argmax(prediction)
        predicted_class = self.classes[predicted_class_index]
        return predicted_class


root = tk.Tk()
gui = ImageClassificationGUI(root)
root.geometry("500x600")
root.configure(bg="#f7f7f7")
root.resizable(False, False)
root.mainloop()

      
