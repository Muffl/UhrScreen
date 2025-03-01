import tkinter as tk
from datetime import datetime

root.title("Uhrzeit Anzeige")

# Maximieren des Fensters
root.attributes('-fullscreen', True)

# Erstellen eines Labels zur Anzeige der Uhrzeit ohne Hintergrundfarbe
label = tk.Label(root, font=('Arial', 100), fg='black', bg=None)
label.pack(expand=True, fill='both')

# Erstellen eines Buttons zum Schließen des Fensters
close_button = tk.Button(root, text="Schließen", command=close_window, font=('Arial', 30))
close_button.pack(side=tk.BOTTOM, pady=20)

# Initialisieren der Uhrzeit-Aktualisierung
update_time()

# Starten der Tkinter Ereignisschleife
root.mainloop()
