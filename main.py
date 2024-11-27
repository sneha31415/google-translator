from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from PIL import Image, ImageTk


root = Tk()
root.title("Google Translate")
root.geometry("1200x400")

# --------------------------------------
def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text = c1)
    label2.configure(text = c2)
    root.after(1000, label_change)

def translate_func():
    try :
        # text that is to be translated
        src_text = text1.get(1.0, END)
        # text of both the dropdowns
        c1 = combo1.get()
        c2 = combo2.get()

        if src_text:
            for code, lang in language.items():
                if (lang.lower() == c1.lower()):
                    src_lan_code = code
                if (lang.lower() == c2.lower()):
                    dest_lan_code = code

            translator = googletrans.Translator()
            translated = translator.translate(src_text, src=src_lan_code, dest=dest_lan_code)
            text2.delete(1.0, END)
            text2.insert(END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"cannot translate due to error: {e}")

# --------------------------------------
# icon
# image_icon = PhotoImage(file = "google.png")
# root.iconphoto(False, image_icon)

# arrow
# Load the image (tkinter does not support jpg)
pil_image = Image.open("self_projects/translator/assets/arrow.jpg")
resized_image = pil_image.resize((250, 150))
arrow_image = ImageTk.PhotoImage(resized_image)

image_label = Label(root, image=arrow_image)
image_label.image = arrow_image  # Keep a reference to avoid garbage collection
image_label.place(x=440, y=120)


language = googletrans.LANGUAGES
# print(language)
languageList = list(language.values())
lang1 = language.keys()

# src language
combo1 = ttk.Combobox(root, values= languageList, font = "Roboto 14", state = "r")
combo1.place(x = 80, y = 20)
# bydefault the dropdown has english
combo1.set("English")

label1 = Label(root, font = "segoe 20 bold", bg = "white", width = 18, bd = 5,relief = GROOVE) 
label1.place(x = 10, y = 50)

# frame for target text
f1 = Frame(root, bg = "Black", bd = 5)
f1.place(x = 10, y = 110, width = 440, height=210)

# textbox for target text
text1 = Text(f1, font = "Roboto 20", bg = "white", relief=GROOVE)
text1.place(x = 0, y = 0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side = "right", fill = "y")

scrollbar1.configure(command = text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)




# translated lang
combo2 = ttk.Combobox(root, values = languageList, font = "RobotV 14", state = "r")
combo2.place(x = 735, y = 20)
combo2.set("Select Language")   

label2 = Label(root, font = "segoe 20 bold", bg = "white", width = 18, bd = 5,relief = GROOVE) 
label2.place(x = 670, y = 50)

# frame for translated text
f2 = Frame(root, bg = "Black", bd = 5)
f2.place(x = 670, y = 110, width = 440, height=210)

# textbox for target text
text2 = Text(f2, font = "Roboto 20", bg = "white", relief=GROOVE)
text2.place(x = 0, y = 0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side = "right", fill = "y")

scrollbar2.configure(command = text2.yview)
text1.configure(yscrollcommand=scrollbar1.set) 

# translate button
translate_btn = Button(root, text = "Translate", font = "Roboto 15 bold italic", activebackground="purple", cursor= "hand2", bd = 5, bg = "red", fg = "white", command = translate_func)
translate_btn.place(x = 480, y = 250)
# ----------------------------------------------

label_change()

root.configure(bg = "white")
root.mainloop()