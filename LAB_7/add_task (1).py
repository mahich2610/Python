import tkinter as tk
from PIL import Image, ImageTk
import requests
import io


SITE_URL = "https://randomfox.ca/floof/"
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 500
BTN_BG_COLOR = 'orange'
BTN_TEXT_COLOR = 'black'
FONT_PARAMETERS = ('Verdana', 14)


def get_fox_image(url):
    data = requests.get(url).json()
    image_data = requests.get(data['image']).content
    new_image = Image.open(io.BytesIO(image_data))
    new_image = new_image.resize((500, 400))
    tk_image = ImageTk.PhotoImage(new_image)
    return tk_image


def change_fox_image():
    tk_image =  get_fox_image(SITE_URL)
    
    label.config(image=tk_image)
    label.image = tk_image


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fox images")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (WINDOWS_WIDTH // 2)
    y = (screen_height // 2) - (WINDOWS_HEIGHT // 2)

    root.geometry(f"{WINDOWS_WIDTH}x{WINDOWS_HEIGHT}+{x}+{y}")

    tk_image = get_fox_image(SITE_URL)

    label = tk.Label(root, image=tk_image)
    label.pack()

    button = tk.Button(
        root, 
        text="Next", 
        command=change_fox_image,
        bg=BTN_BG_COLOR, 
        fg=BTN_TEXT_COLOR, 
        font=FONT_PARAMETERS, 
        bd=5)
    button.pack()

    root.mainloop()
