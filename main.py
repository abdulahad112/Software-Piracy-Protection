import tkinter
import tkinter as tk
from pygame import mixer
from tkinter import PhotoImage
import webbrowser
import os
class MyApp:
    def __init__(self, root):       
        self.root = root
        root.title("Software Protection Application")
        root.geometry("1366x768")
        #root.configure(bg="gray")
        self.create_main_menu()
    def play_click_sound():
        mixer.init()
        mixer.music.load("welcome.wav")  # Replace with the path to your click sound file
        mixer.music.play()
        def __init__(self, root):
         self.root = root
         self.root.title("Click Sound App")
         def on_button_click(self):
             print("")
    play_click_sound()
 
# this is main page the menuw page Some pages in this Software used multiple times to 
# Save Time Thank you 
    def create_main_menu(self):
        self.clear_screen()
         # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        self.title_label = tk.Label(self.root, text="Welcome", font=("Helvetica", 24), bg="blue", fg="black")
        self.title_label.pack(pady=60)

        self.protect_button = tk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, font=("Helvetica", 14), fg="black")
        self.protect_button.pack()

        self.help_pagea = tk.Button(self.root, text="Help", command=self.open_help, font=("Helvetica", 14), fg="black")
        self.help_pagea.pack()

        self.help_pageb = tk.Button(self.root, text="Bug Report", command=self.bug_page, font=("Helvetica", 14), fg="black")
        self.help_pageb.pack()

        self.about_button = tk.Button(self.root, text="About Us", command=self.open_about_page, font=("Helvetica", 14), fg="black")
        self.about_button.pack()

        self.visit_button = tk.Button(self.root, text="Visit Us", command=self.visit_link, font=("Helvetica", 14), fg="black")
        self.visit_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, font=("Helvetica", 14), fg="black")
        self.exit_button.pack()

      

# The Protect Page 
    def open_protect_page(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        protect_frame = tk.Frame(self.root, bg="light blue")
        protect_frame.pack()

        title_label = tk.Label(protect_frame, text="Protect Piracy Page", font=("Helvetica", 24), bg="yellow", fg="black")
        title_label.pack(pady=20)

        register_button = tk.Button(protect_frame, text="Register Software", command=self.open_link, font=("Helvetica", 14), fg="black")
        register_button.pack()

        lock_button = tk.Button(protect_frame, text="Pack", command=self.open_packer, font=("Helvetica", 14), fg="black")
        lock_button.pack()

        encrypt_button = tk.Button(protect_frame, text="Encrypt-Decrypt", command=self.open_encrypt_decrypt, font=("Helvetica", 14), fg="black")
        encrypt_button.pack()

        back_button = tk.Button(protect_frame, text="Back To Main Menu", command=lambda: self.create_main_menu(), font=("Helvetica", 14), fg="black")
        back_button.pack()
# The Help Page
    def open_help(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        about_frame = tk.Frame(self.root, bg="light blue")
        about_frame.pack()

        title_label = tk.Label(about_frame, text="Help Page", font=("Helvetica", 24), bg="blue", fg="black")
        title_label.pack(pady=20)

        about_text = "Register Button will Lead you to register website Of USA gov\n"\
                     "You can Create Account and Register The Product Directly\n"\
                     "________________________________________________________________\n"\
                     "Pack Button Will Lead you to external App In which\n"\
                     "First You Have To Browse The App or File Then you Have To click Pack \n"\
                     "And after Clicking Pack You can also unpack it by Unpack Button \n Or you can Extract\n"\
                     "The File Later By 7Z Archiver Or Winrar\n"\
                     "_________________________________________________________________\n"\
                     "Encrypt-Decrypt Button Can Help You to encrypt and Decrypt file \n"\
                     "First You Have To Click Browse then Click Encrypt Done\n"\
                     "Now You can Decrypt it Anytime You want \n"\
                     "Just Browse Again and Click Decrypt Done\n"\
                     "________________________________________________________________________________\n"\
                     
                        
        about_label = tk.Label(about_frame, text=about_text, font=("Helvetica", 14), bg="white", fg="black")
        about_label.pack()

        back_button = tk.Button(about_frame, text="Back To Main Menu", command=lambda: self.create_main_menu(), font=("Helvetica", 14), fg="black")
        back_button.pack()
# The Report Bug Page
    def bug_page(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        protect_frame = tk.Frame(self.root, bg="light blue")
        protect_frame.pack()

        title_label = tk.Label(protect_frame, text="Report The Bug", font=("Helvetica", 24), bg="Red", fg="black")
        title_label.pack(pady=20)

        register_button = tk.Button(protect_frame, text="Email Us", command=self.open_linke, font=("Helvetica", 14), fg="black")
        register_button.pack()

        global email_label
        email_label = tk.Label(protect_frame, text="", font=("Helvetica", 14), fg="black")
        email_label.pack()

        back_button = tk.Button(protect_frame, text="Back To Main Menu", command=lambda: self.create_main_menu(), font=("Helvetica", 14), fg="black")
        back_button.pack()
# The about Page
    def open_about_page(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        about_frame = tk.Frame(self.root, bg="light blue")
        about_frame.pack()

        title_label = tk.Label(about_frame, text="About Us Page", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack(pady=20)

        about_text = "This collaborative Python project is the result of the combined efforts of three students\n"\
        "Zafran, Ahad, and Huzaifa, enrolled in the 5th semester of the BS IT program at Mirpur University of Science and Technology\n"\
        "Crafted using fundamental code and leveraging online tools, this mini project showcases their skills and creativity.\n"\
            "Gratitude for exploring this endeavor! Thank you"
        
        about_label = tk.Label(about_frame, text=about_text, font=("Helvetica", 14), bg="white", fg="black")
        about_label.pack()
#credits Button here
        ver_button = tk.Button(self.root, text="Credits", command=self.open_linked, font=("Helvetica", 14), fg="black")
        ver_button.pack()

        global ver_b
        ver_b = tk.Label(self.root, text="", font=("Helvetica", 14), fg="black")
        ver_b.pack()

        back_button = tk.Button(about_frame, text="Back To Main Menu", command=lambda: self.create_main_menu(), font=("Helvetica", 14), fg="black")
        back_button.pack()

    def visit_link(self):
        webbrowser.open("https://www.linkedin.com/in/syed-zafran-haider/")

    def open_link(self):
        webbrowser.open("https://eservice.eco.loc.gov/siebel/app/eservice/enu?SWECmd=Start")

    def open_linkec(self):
        webbrowser.open("zraaeae@gmail.com")
#Email Us Button Function
    def open_linke(self):
        email_label.config(text="Email Here: zraaeae@gmail.com")

#The version button function
    def open_linked(self):
        ver_b.config(text="Syed Zafran Haider \n Abdul ahad \n Huzaifa Iftikhar \n Students of \n Mirpur university Of Science and Technology ")
    
    def open_packer(self):
        os.system("packer.exe")

    def open_encrypt_decrypt(self):
        os.system("enc.exe")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
