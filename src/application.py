from trie import Trie
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "dark-blue", "green"

class AddContactWindow(ctk.CTkToplevel):
    def __init__(self, parent, trie, refresh_callback):
        super().__init__(parent)
        self.title("Add New Contact")
        self.geometry("300x350")
        self.trie = trie
        self.refresh_callback = refresh_callback
        self.grab_set()
        self.setup_ui()
    
    def setup_ui(self):
        def create_input(label_text):
            label = ctk.CTkLabel(self, text=label_text)
            label.pack(pady=(10, 0))
            entry = ctk.CTkEntry(self, width=200)
            entry.pack(pady=(0, 10))
            return entry

        self.name_entry = create_input("Full Name")
        self.phone_entry = create_input("Phone Number")
        self.email_entry = create_input("Email Address")

        add_button = ctk.CTkButton(self, text="Add Contact", command=self.add_contact)
        add_button.pack(pady=20)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name:
            ctk.CTkLabel(self, text="Name is required!", text_color="red").pack()
            return

        info = {"phone": phone, "email": email, "name": name}
        self.trie.insert(name, info)

        self.refresh_callback()
        self.destroy()

class ViewContactWindow(ctk.CTkToplevel):
    def __init__(self, parent, trie, name, refresh_callback):
        super().__init__(parent)
        self.title("Contact Details")
        self.geometry("300x300")
        self.trie = trie
        self.name = name
        self.refresh_callback = refresh_callback
        self.grab_set()
        self.setup_ui()
    
    def setup_ui(self):
        contact_info = self.trie.search(self.name)
        if not contact_info:
            ctk.CTkLabel(self, text="Contact not found!", text_color="red").pack(pady=20)
            return
        
        ctk.CTkLabel(self, text=contact_info["name"], font=("Arial", 20, "bold")).pack(pady=(10, 10))

        ctk.CTkLabel(self, text="Phone:", font=("Arial", 12)).pack()
        ctk.CTkLabel(self, text=contact_info.get("phone", "N/A"), font=("Arial", 14)).pack(pady=(0, 10))

        ctk.CTkLabel(self, text="Email:", font=("Arial", 12)).pack()
        ctk.CTkLabel(self, text=contact_info.get("email", "N/A"), font=("Arial", 14)).pack(pady=(0, 20))

        delete_button = ctk.CTkButton(self,
                                      text="Delete Contact",
                                      fg_color="red",
                                      command=self.delete_contact)
        delete_button.pack(side="bottom", pady=10)

    def delete_contact(self):
        success = self.trie.remove(self.name)
        if success:
            self.refresh_callback()
            self.destroy()

class PhonebookApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Phonebook Application")
        self.geometry("600x500")
        self.trie = Trie()
        self.load_sample_contacts()
        self.setup_ui()
        self.update_contact_list()

    def load_sample_contacts(self):
        sample_contacts = [
            ("Alice Doe", {"phone": "123-456-7890", "email": "alice@example.com"}),
            ("Ashley Morgan", {"phone": "987-654-3210", "email": "ashley@example.com"}),
            ("Charlie Benner", {"phone": "555-555-5555", "email": "charlie@example.com"}),
            ("Chris Smith", {"phone": "111-222-3333", "email": "chris@example.com"}),
            ("Antone Johnson", {"phone": "444-333-2222", "email": "antone@example.com"}),
            ("Christopher Miller", {"phone": "777-888-9999", "email": "christopher@example.com"}),
            ("Ivan Petrov", {"phone": "666-777-8888", "email": "ivan@example.com"}),
            ("Ann Marie", {"phone": "222-333-4444", "email": "annmarie@example.com"}),
            ("Alina Smith", {"phone": "555-555-5555", "email": "alina@example.com"}),
            ("Anthony Johnson", {"phone": "999-888-7777", "email": "anthony@example.com"})
        ]
        for name, info in sample_contacts:
            self.trie.insert(name, info)
    
    def setup_ui(self):
        # Create top div for search and add contact
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.pack(pady=20, padx=20, fill="x")

        # Search bar
        self.search_input = ctk.StringVar()
        self.search_bar = ctk.CTkEntry(
            self.top_frame, 
            textvariable=self.search_input, 
            width=300)
        self.search_bar.pack(side="left", padx=(0, 10))
        self.search_bar.bind("<KeyRelease>", self.on_search)

        # Add Contact Button
        self.add_button = ctk.CTkButton(
            self.top_frame, 
            text="Add Contact", 
            command=self.add_contact)
        self.add_button.pack(side="right")

        # Scrollable frame for contact list
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text="Contacts")
        self.scroll_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    def on_search(self, event=None):
        query = self.search_input.get()
        self.update_contact_list(query)

    def update_contact_list(self, prefix=""):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        results = self.trie.autocomplete(prefix)
        if not results:
            label = ctk.CTkLabel(self.scroll_frame, text="No contacts found.")
            label.pack(pady=10)
        else:
            for name, info in results:
                self.create_contact_card(name, info)

        # Reset scroll
        self.scroll_frame._parent_canvas.yview_moveto(0)
    
    def create_contact_card(self, name, info):
        card = ctk.CTkFrame(self.scroll_frame)
        card.pack(padx=5, pady=5, fill="x")

        name_label = ctk.CTkLabel(card, 
                                  text=info["name"], 
                                  font=ctk.CTkFont(size=16, weight="bold"))
        name_label.pack(side="left", padx=10)

        view_button = ctk.CTkButton(card,
                                    text="View",
                                    width=80,
                                    command = lambda n=name: self.view_contact(n))
        view_button.pack(side="right", padx=10, pady=10)

    def add_contact(self):
        AddContactWindow(
            parent=self,
            trie=self.trie,
            refresh_callback=lambda: self.update_contact_list(self.search_input.get())
        )
    
    def view_contact(self, name):
        ViewContactWindow(
            parent=self,
            trie=self.trie,
            name=name,
            refresh_callback=lambda: self.update_contact_list(self.search_input.get())
        )


if __name__ == "__main__":
    app = PhonebookApp()
    app.mainloop()