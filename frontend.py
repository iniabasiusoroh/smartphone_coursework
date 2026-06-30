# Task 4 ----------------------------------------------------------------------------------------------------------------

from tkinter import Tk, Frame, Label, IntVar, StringVar, Button, Entry

class SmartphoneGUI:
    def __init__(self):
        self.win = Tk()
        self.win.title("SmartphoneGUI")
        self.win.geometry("600x380")
        
        self.capacity_gb = 512.0
        self.battery = 75
        self.battery_percent = IntVar(value=100)
        self.saver_mode = False
        self.storage_left = 511.98
        
        self.num_of_photos = 42
        self.photo_storage_amount_used = 0.98
        
        self.num_of_emails = 18
        self.storage_used_mailbox = 0.09
        
        self.sender_var = StringVar(value = "Write the sender here")
        self.content_var = StringVar(value = "Write the content here")
        
        self.main_frame = Frame(self.win, padx=10, pady=10)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
    def run(self):
        self.create_widgets()
        self.win.mainloop()


    def create_widgets(self):
        label_phone_name = Label(self.main_frame, text="BnL Smartphone")
        label_phone_name.grid(row = 0, column = 0, sticky = "w")
        
        # Storage Capacity
        label_storage_capacity = Label(self.main_frame, text = "Storage Capacity:")
        label_storage_capacity.grid(row = 1, column = 0, sticky = "w")
        label_storage_capacity_amount = Label(self.main_frame, text = f"{int(self.capacity_gb)}GB")
        label_storage_capacity_amount.grid(row = 1, column = 1, sticky = "w")
        
        # Battery
        label_battery = Label(self.main_frame, text = "Battery:")
        label_battery.grid(row = 2, column = 0, sticky = "w")
        label_battery_amount = Label(self.main_frame, text = f"{int(self.battery)}%")
        label_battery_amount.grid(row = 2, column = 1, sticky = "w")
        
        # Battery Saver Mode
        label_battery_saver_mode = Label(self.main_frame, text = "Battery Saver Mode:")
        label_battery_saver_mode.grid(row = 3, column = 0, sticky = "w")
        if not self.saver_mode:
            label_battery_saver_status = Label(self.main_frame, text="Disabled")
            label_battery_saver_status.grid(row=3, column=1, sticky = "w")
        else:
            label_battery_saver_status = Label(self.main_frame, text="Enabled")
            label_battery_saver_status.grid(row=3, column=1, sticky = "w")

        # Storage Left
        label_storage_left = Label(self.main_frame, text="Storage Left:")
        label_storage_left.grid(row=4, column=0, sticky = "w")
        label_storage_left_amount = Label(self.main_frame, text=f"{self.storage_left}GB")
        label_storage_left_amount.grid(row=4, column=1, sticky = "w")
        
        # Battery Buttons
        button_toggle_saver = Button(self.main_frame, text = "Toggle Battery Saver", width = 20)
        button_toggle_saver.grid(row = 5, column = 0, sticky = "w")
        button_change_battery = Button(self.main_frame, text = "Charge Battery", width = 15)
        button_change_battery.grid(row = 5, column = 1, sticky = "w")
        
        # Photo Things
        label_photos = Label(self.main_frame, text = "Photos App")
        label_photos.grid(row = 6, column = 0, sticky = "w")
        
        label_num_of_photos = Label(self.main_frame, text = "Number of photos:")
        label_num_of_photos.grid(row = 7, column = 0, sticky = "w")
        
        label_num_of_photos_amount = Label(self.main_frame, text=f"{self.num_of_photos}")
        label_num_of_photos_amount.grid(row=7, column=1, sticky = "w")

        label_photo_storage = Label(self.main_frame, text="Storage Used:")
        label_photo_storage.grid(row=8, column=0, sticky = "w")

        label_photo_storage_amount = Label(self.main_frame, text=f"{self.photo_storage_amount_used}GB")
        label_photo_storage_amount.grid(row=8, column=1, sticky = "w")

        button_take_photo = Button(self.main_frame, text="Take Photo", width=15)
        button_take_photo.grid(row=9, column=0, sticky = "w")

        button_delete_photo = Button(self.main_frame, text="Delete Photo", width=15)
        button_delete_photo.grid(row=9, column=1, sticky = "w")
        
        # Mailbox App Things
        label_mailbox_app = Label(self.main_frame, text = "Mailbox App")
        label_mailbox_app.grid(row = 10, column = 0, sticky = "w")
        
        label_number_of_emails = Label(self.main_frame, text = "Number of Emails:")
        label_number_of_emails.grid(row = 11, column = 0, sticky = "w")
        
        label_num_of_emails = Label(self.main_frame, text = f"{self.num_of_emails}")
        label_num_of_emails.grid(row = 11, column = 1, sticky = "w")
        
        label_storage_used = Label(self.main_frame, text = "Storage Used:")
        label_storage_used.grid(row = 12, column = 0, sticky = "w")
        
        label_storage_amount_used = Label(self.main_frame, text = f"{self.storage_used_mailbox}GB")
        label_storage_amount_used.grid(row = 12, column = 1, sticky = "w")
        
        entry_write_sender = Entry(self.main_frame, width = 25, textvariable = self.sender_var)
        entry_write_sender.grid(row = 13, column = 0, sticky = "w")
        
        entry_write_content = Entry(self.main_frame, width = 25, textvariable = self.content_var)
        entry_write_content.grid(row = 13, column = 1, sticky = "w")
        
        button_recieve_email = Button(self.main_frame, width = 10, text = "Recieve Email")
        button_recieve_email.grid(row = 14, column = 0, sticky = "w", padx = 0, pady = 5)
        

        


def main():
    smartphone = SmartphoneGUI()
    smartphone.run()
    
    
main()