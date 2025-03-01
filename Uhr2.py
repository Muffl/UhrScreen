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

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Uhrzeit Anzeige")

# Maximieren des Fensters
root.attributes('-fullscreen', True)

# Laden eines zufälligen Bildes aus dem Internet
response = requests.get('https://picsum.photos/800/600')
img_data = response.content
image = Image.open(BytesIO(img_data))
photo = ImageTk.PhotoImage(image)

# Hinzufügen des Bildes als Label-Hintergrund
background_label = tk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Erstellen eines Labels zur Anzeige der Uhrzeit ohne Hintergrundfarbe
label = tk.Label(root, font=('Arial', 100), fg='black', anchor='center')
label.pack(expand=True)

# Erstellen eines Buttons zum Schließen des Fensters
close_button = tk.Button(root, text="Schließen", command=close_window, font=('Arial', 30))
close_button.pack(side=tk.BOTTOM, pady=20)

# Initialisieren der Uhrzeit-Aktualisierung
update_time()

# Starten der Tkinter Ereignisschleife
root.mainloop()
