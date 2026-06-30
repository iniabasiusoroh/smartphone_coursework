# Task 1 -------------------------------------------------------------------------------------------------------------
class Smartphone:
    
    def __init__(self, storage_capacity):
        self.storage_capacity = storage_capacity
        self.battery = 100
        self.battery_saver_mode = False
        
    def use_battery(self, amount):
        if self.battery - amount >= 0:
            self.battery -= amount
        else:
            self.battery = 0
        
    def charge_battery(self):
        if self.battery_saver_mode == False:
            self.battery = 100
        else:
            self.battery = 80
            
    def __str__(self):
        output = f"BnL Smartphone - Storage: {self.storage_capacity}GB, Battery: {self.battery}%, Battery Saver Mode: "
        
        if self.battery_saver_mode == False:
            output += "Disabled"
        else:
            output += "Enabled"
            
        return output

# Test Smartphone
def test_smartphone():
    # Create an instance of the Smartphone class with a storage capacity of 512 gigabytes.
    test_phone = Smartphone(512)
    # Use 30% of its battery using the appropriate method.
    test_phone.use_battery(30)
    # Print your instance to display its current state.
    print(test_phone)
    # Enable battery saver mode by directly updating the instance variable.
    test_phone.battery_saver_mode = True
    # Charge the battery using the appropriate method.
    test_phone.charge_battery()
    # Print the object again to display its updated state.
    print(test_phone)

# -----------------------------------------------------------------------------------------------------------------------
# Task 2 ----------------------------------------------------------------------------------------------------------------
class PhotosApp:
    def __init__(self):
        self.num_photos = 0
    
    def take_photo(self):
        self.num_photos += 1
        
    def delete_photo(self):
        if self.num_photos > 0:
            self.num_photos -= 1
    
    def calculate_storage_used(self):
        total_storage_in_mb = self.num_photos * 24
        return total_storage_in_mb / 1024

    def __str__(self):
        output = f"Photos App - Photos: {self.num_photos}, Storage Used: {self.calculate_storage_used():.2f}GB"
        return output
        
# Test PhotosApp
def test_photos_app():
    # Create an instance of PhotosApp.
    photos_app = PhotosApp()
    # Take 5 photos (you can use a loop and call the appropriate method).
    for i in range(5):
        photos_app.take_photo()
    # Print the instance of the PhotosApp.
    print(photos_app)
    # Delete 2 photos.
    for i in range(2):
        photos_app.delete_photo()
    # Print the PhotosApp instance again.
    print(photos_app)

# -----------------------------------------------------------------------------------------------------------------------
# Task 3 ----------------------------------------------------------------------------------------------------------------
class MailBoxApp:
    def __init__(self):
        self.emails = {}
    
    def receive_email(self, sender, content):
        if sender not in self.emails:
            self.emails[sender] = []
        self.emails[sender].append(content)
    
    def count_emails(self):
        emails_count = 0
        for messages in self.emails.values():
            emails_count += len(messages)
        return emails_count
    
    def calculate_storage_used(self):
        count = self.count_emails()
        total_storage_takeup = count * 5  # 5 megabites per email
        
        # Currently returns are GB
        return total_storage_takeup / 1024
    
    def __str__(self):
        output = f"Number of emails: {self.count_emails()}, Storage used: {self.calculate_storage_used():.2f}GB \n"
        output += f"List of the emails: \n"
        for sender,messages in self.emails.items():
            output += f"{sender}: {messages} \n"
        return output
    
def test_mail_box_app():
    test_box = MailBoxApp()
    test_box.receive_email("Ini", "Hello, This is a test")
    test_box.receive_email("Max", "Good afternoon sir")
    test_box.receive_email("Jack", "Hello mate.")
    test_box.receive_email("Jason", "This is another test")
    print(test_box)
    test_box.receive_email("Jill", "This is one more test")
    test_box.receive_email("Jason", "This is an extra test")
    print(test_box)
    
# -----------------------------------------------------------------------------------------------------------------------    
    
    