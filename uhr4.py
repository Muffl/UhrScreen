import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from datetime import datetime

def update_time():
    """Aktualisiert die angezeigte Uhrzeit."""
    current_time = datetime.now().strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)  # Aktualisiere jede Sekunde

def close_window():
    """Schließt das Fenster."""
    root.destroy()

def load_new_image():
    """Lädt ein neues zufälliges Hintergrundbild."""
    response = requests.get('https://picsum.photos/2048/1152')
    img_data = response.content
    image = Image.open(BytesIO(img_data))
    image = image.resize((screen_width, screen_height), Image.LANCZOS)
    new_photo = ImageTk.PhotoImage(image)
    
    # Update the background label with the new image
    background_label.config(image=new_photo)
    background_label.image = new_photo  # Store reference to avoid garbage collection

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Uhrzeit Anzeige")

# Maximieren des Fensters
root.attributes('-fullscreen', True)

# Bestimmen der Fenstergröße
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Initiales Laden eines zufälligen Bildes aus dem Internet
response = requests.get('https://picsum.photos/2048/1152')
img_data = response.content
image = Image.open(BytesIO(img_data))
image = image.resize((screen_width, screen_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Hinzufügen des Bildes als Label-Hintergrund
background_label = tk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Erstellen eines Labels zur Anzeige der Uhrzeit ohne Hintergrundfarbe
label = tk.Label(root, font=('Arial', 100), fg='white', bg="black", anchor='center')
label.pack(expand=True)

# Erstellen eines Buttons zum Schließen des Fensters
close_button = tk.Button(root, text="Schließen", command=close_window, fg='white', bg="black", font=('Arial', 20))
close_button.pack(side=tk.BOTTOM, pady=(20, 10))  # Padding angepasst für neuen Button

# Erstellen eines Buttons zum Laden eines neuen Hintergrundbildes
new_image_button = tk.Button(root, text="Neues Bild laden", command=load_new_image, fg='white', bg="black", font=('Arial', 10))
new_image_button.pack(side=tk.BOTTOM, pady=(0, 0))

# Initialisieren der Uhrzeit-Aktualisierung
update_time()

# Starten der Tkinter Ereignisschleife
root.mainloop()
