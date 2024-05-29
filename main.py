import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

import custom_messageboxes
from customers import *
from products import *
from orders import *
from error_handling import *
from custom_messageboxes import *

# Constant values
PADX = 5
PADY = 5
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


class GUI:
    def __init__(self, window):
        # window setup
        self.window = window
        self.window.title("Crazy Pizza Restaurant Management System")
        self.display_width = window.winfo_screenwidth()
        self.display_height = window.winfo_screenheight()
        self.left = int(self.display_width / 2 - (WINDOW_WIDTH / 2))
        self.top = int(self.display_height / 2 - (WINDOW_HEIGHT / 2))
        self.window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{self.left}+{self.top}")
        self.window.config(padx=PADX*2, pady=PADY*2)
        self.window.minsize(int(WINDOW_WIDTH/1.25), int(WINDOW_HEIGHT/1.25))

        # login screen
        self.login_frame = ttk.Frame(window)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.title_label = ttk.Label(self.login_frame, text="Welcome to Crazy Pizza!", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=PADX, pady=PADY)

        self.login_canvas = tk.Canvas(self.login_frame, width=200, height=200)
        self.login_canvas.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=PADX, pady=PADY)
        self.logo_image = tk.PhotoImage(file="crazy_logo.png")
        self.login_canvas.create_image(100, 100, image=self.logo_image)

        self.user_label = ttk.Label(self.login_frame, text="User: ")
        self.user_label.grid(row=2, column=0, sticky="nsew", padx=PADX, pady=PADY)
        self.user_tuple = ("Manager", "Waiter", "Chef")
        self.user_string = tk.StringVar(value=self.user_tuple[0])
        self.combobox_product = ttk.Combobox(self.login_frame, textvariable=self.user_string)
        self.combobox_product['values'] = self.user_tuple
        self.combobox_product.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        self.password_label = ttk.Label(self.login_frame, text="Password: ")
        self.password_label.grid(row=3, column=0, sticky="nsew", padx=PADX, pady=PADY)
        self.password_string = tk.StringVar(value="")
        self.password_entry = ttk.Entry(self.login_frame, width=30, textvariable=self.password_string, show="*")
        self.password_entry.grid(row=3, column=1, sticky="nsew", padx=PADX, pady=PADY)
        self.password = "123456"

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login_process)
        self.login_button.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=PADX, pady=PADY)

        self.grip = ttk.Sizegrip(window)
        self.grip.place(relx=1.0, rely=1.0, anchor="se")

        # operative methods
        # self.manager_menu()
        # self.waiter_menu()
        # self.chef_menu()

        # database instances
        self.pizzas = Pizza()
        self.snacks = Snack()
        self.drinks = Drink()
        self.active_orders = ActiveOrders()
        self.finished_orders = FinishedOrders()
        self.canceled_orders = CanceledOrders()
        self.customers = Customers()

    def login_process(self):
        user = self.user_string.get()
        password = self.password_string.get()
        if user == "Manager" and password == self.password:
            self.manager_menu()
        elif user == "Waiter":
            self.waiter_menu()
        elif user == "Chef":
            self.chef_menu()
        else:
            # custom_showerror(self.window, title="Error!", message="Oops! \nInvalid username or password.")
            messagebox.showerror(title="Error!", message="Oops! \nInvalid username or password.")

    def manager_menu(self):
        # Manager Window Setup
        manager_window = tk.Toplevel(self.window)
        manager_window.title("Crazy Pizza Management")

        self.left = int(self.display_width / 2 - (WINDOW_WIDTH / 2))
        self.top = int(self.display_height / 2 - (WINDOW_HEIGHT / 2))
        manager_window.geometry(f"{int(WINDOW_WIDTH*1.5)}x{WINDOW_HEIGHT}+{self.left}+{self.top}")
        manager_window.config(padx=PADX, pady=PADY)
        manager_window.minsize(int(WINDOW_WIDTH*1.5 / 1.25), int(WINDOW_HEIGHT / 1.25))

        # Multiple tabs for the manager window
        notebook = ttk.Notebook(manager_window)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        tab3 = ttk.Frame(notebook)
        notebook.add(tab1, text="Menu Management")
        notebook.add(tab2, text="Restaurant Analysis")
        notebook.add(tab3, text="<Placeholder>")
        notebook.pack(fill=tk.BOTH)

        # tab1 Menu Management window layout
        left_frame1 = ttk.Frame(tab1, width=280, height=self.display_height, relief=tk.GROOVE)
        left_frame1.pack(side="left", fill=tk.Y, expand=True, padx=PADX)
        right_frame1 = ttk.Frame(tab1, width=self.display_width, height=self.display_height, relief=tk.GROOVE)
        right_frame1.pack(side="left", fill=tk.BOTH, expand=True)
        right_frame1.pack_propagate(False)

        self.logo_in_manager(left_frame1, "crazy_manager_logo.png")

        show_menu_button = ttk.Button(left_frame1, text="Show Menu", command=lambda: show_menu(right_frame1))
        show_menu_button.pack(pady=PADY)
        add_product_button = ttk.Button(left_frame1, text="New Product", command=self.add_product)
        add_product_button.pack(pady=PADY)
        remove_product_button = ttk.Button(left_frame1, text="Remove Product", command=lambda: self.remove_product(self.tree_menu))
        remove_product_button.pack(pady=PADY)
        update_product_button = ttk.Button(left_frame1, text="Update Product", command=lambda: self.update_product(self.tree_menu))
        update_product_button.pack(pady=PADY)

        # Placing grip at the corner
        grip = ttk.Sizegrip(manager_window)
        grip.place(relx=1.0, rely=1.0, anchor="se")

        @handle_errors
        def show_menu(frame):
            self.cleaning_frame(frame)
            self.tree_menu = ttk.Treeview(frame, show="headings", selectmode="browse")
            self.tree_menu["columns"] = ("ID", "Type", "Name", "Price", "Ingredients")
            self.tree_menu.column("ID", anchor="center", width=25)
            self.tree_menu.column("Type", anchor="center", width=50)
            self.tree_menu.column("Name", anchor="center", width=200)
            self.tree_menu.column("Price", anchor="center", width=50)
            self.tree_menu.column("Ingredients", anchor="center", width=400)
            self.tree_menu.heading("ID", text="ID")
            self.tree_menu.heading("Type", text="Type")
            self.tree_menu.heading("Name", text="Name")
            self.tree_menu.heading("Price", text="Price")
            self.tree_menu.heading("Ingredients", text="Ingredients")
            self.tree_menu.pack(padx=PADX, pady=PADY, expand=True, fill=tk.BOTH)

            self.pizza = Pizza()
            self.snack = Snack()
            self.drink = Drink()

            pizzas = self.pizza.list_products()
            snacks = self.snack.list_products()
            drinks = self.drink.list_products()

            for pizza in pizzas:
                self.tree_menu.insert("", "end", values=(pizza[0], "Pizza", pizza[2], pizza[3], pizza[4]))

            for snack in snacks:
                self.tree_menu.insert("", "end", values=(snack[0], "Snack", snack[2], snack[3], snack[4]))

            for drink in drinks:
                self.tree_menu.insert("", "end", values=(drink[0], "Drink", drink[2], drink[3], drink[4]))

    @handle_errors
    def add_product(self):
        add_product_window = tk.Toplevel(self.window)
        add_product_window.title("New Product")
        add_product_window.geometry("500x400")
        add_product_window.resizable(False, False)

        product_type_label = ttk.Label(add_product_window, text="Product Type: ")
        product_type_label.grid(row=0, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_tuple = ("Pizza", "Snack", "Drink")
        product_string = tk.StringVar(value=product_tuple[0])
        combobox_product = ttk.Combobox(add_product_window, textvariable=product_string)
        combobox_product['values'] = product_tuple
        combobox_product.grid(row=0, column=1, sticky="nsew", padx=PADX, pady=PADY)

        product_name_label = ttk.Label(add_product_window, text="Product Name: ")
        product_name_label.grid(row=1, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_name_entry = ttk.Entry(add_product_window, width=30)
        product_name_entry.grid(row=1, column=1, sticky="nsew", padx=PADX, pady=PADY)

        product_price_label = ttk.Label(add_product_window, text="Product Price: ")
        product_price_label.grid(row=2, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_price_entry = ttk.Entry(add_product_window, width=30)
        product_price_entry.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        product_ingredients_label = ttk.Label(add_product_window, text="Ingredients: ")
        product_ingredients_label.grid(row=3, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_ingredients_entry = tk.Text(add_product_window, width=30, height=15)
        product_ingredients_entry.grid(row=3, column=1, sticky="nsew", padx=PADX, pady=PADY)

        @handle_errors
        def adding_product():
            product_type = product_string.get()
            product_name = product_name_entry.get()
            product_price = float(product_price_entry.get())
            product_ingredients = product_ingredients_entry.get("1.0", tk.END).strip()

            if product_type and product_name and product_price:

                if product_type == "Pizza":
                    self.pizzas.add_product(product_name, product_price, product_ingredients)
                elif product_type == "Snack":
                    self.snacks.add_product(product_name, product_price, product_ingredients)
                elif product_type == "Drink":
                    self.drinks.add_product(product_name, product_price, product_ingredients)
                else:
                    messagebox.showerror(title="Error!", message="Oops! \nInvalid product type.")

            else:
                messagebox.showwarning(title="Warning!", message="Please fill the Product Name and the Product Price.")

        adding_product_button = ttk.Button(add_product_window, text="Add Product", command=adding_product)
        adding_product_button.grid(row=4, column=0, columnspan=2, pady=PADY)

    @handle_errors
    def update_product(self, tree_menu):
        selected_item = tree_menu.selection()
        if not selected_item:
            messagebox.showwarning(title="Warning!", message="You haven't selected any product from the menu.")
            return

        update_product_window = tk.Toplevel(self.window)
        update_product_window.title("Update Product")
        update_product_window.geometry("500x400")
        update_product_window.resizable(False, False)

        item_values = tree_menu.item(selected_item)["values"]
        item_id = item_values[0]
        item_type = item_values[1]
        old_name = item_values[2]
        print(f"old name: {old_name}")
        old_price = item_values[3]
        print(f"old price: {old_price}")
        old_ingredients = item_values[4]

        product_name_label = ttk.Label(update_product_window, text="New Product Name: ")
        product_name_label.grid(row=1, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_name_entry = ttk.Entry(update_product_window, width=30)
        product_name_entry.insert(tk.END, old_name)
        product_name_entry.grid(row=1, column=1, sticky="nsew", padx=PADX, pady=PADY)

        product_price_label = ttk.Label(update_product_window, text="New Product Price: ")
        product_price_label.grid(row=2, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_price_entry = ttk.Entry(update_product_window, width=30)
        product_price_entry.insert(tk.END, old_price)
        product_price_entry.grid(row=2, column=1, sticky="nsew", padx=PADX, pady=PADY)

        product_ingredients_label = ttk.Label(update_product_window, text="New Ingredients: ")
        product_ingredients_label.grid(row=3, column=0, sticky="nsew", padx=PADX, pady=PADY)
        product_ingredients_entry = tk.Text(update_product_window, width=30, height=15)
        product_ingredients_entry.insert(tk.END, old_ingredients)
        product_ingredients_entry.grid(row=3, column=1, sticky="nsew", padx=PADX, pady=PADY)

        @handle_errors
        def updating_product():
            updated_name = product_name_entry.get()
            updated_price = float(product_price_entry.get())
            updated_ingredients = product_ingredients_entry.get("1.0", tk.END)
            if updated_name and updated_price:
                if item_type == "Pizza":
                    self.pizzas.update_product(item_id, updated_name, updated_price, updated_ingredients)
                    tree_menu.item(selected_item, values=(item_id, updated_name, updated_price, updated_ingredients))
                    messagebox.showinfo(title="Success!", message="Product updated successfully!")
                    update_product_window.destroy()
                elif item_type == "Snack":
                    self.snacks.update_product(item_id, updated_name, updated_price, updated_ingredients)
                    tree_menu.item(selected_item, values=(item_id, updated_name, updated_price, updated_ingredients))
                    messagebox.showinfo(title="Success!", message="Product updated successfully!")
                    update_product_window.destroy()
                elif item_type == "Drink":
                    self.drinks.update_product(item_id, updated_name, updated_price, updated_ingredients)
                    tree_menu.item(selected_item, values=(item_id, updated_name, updated_price, updated_ingredients))
                    messagebox.showinfo(title="Success!", message="Product updated successfully!")
                    update_product_window.destroy()
            else:
                messagebox.showwarning(title="Warning!", message="Please fill the New name and the New price.")

        updating_product_button = ttk.Button(update_product_window, text="Update Product", command=updating_product)
        updating_product_button.grid(row=4, column=0, columnspan=2, pady=PADY)

    @handle_errors
    def remove_product(self, tree_menu):
        selected_item = tree_menu.selection()
        if not selected_item:
            messagebox.showwarning(title="Warning!", message="You haven't selected any product from the menu.")
            return

        remove_product_window = tk.Toplevel(self.window)
        remove_product_window.title("Remove Product")
        remove_product_window.geometry("350x200")
        remove_product_window.resizable(False, False)

        item_values = tree_menu.item(selected_item)["values"]
        item_id = item_values[0]
        item_type = item_values[1]
        name = item_values[2]
        price = item_values[3]

        remove_product_label = ttk.Label(remove_product_window, text=f'''
        The product you selected to remove is:
                Product ID: {item_id}
                Product Type: {item_type}
                Product Name: {name}
                Product Price: {price}
        ''')
        remove_product_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=PADX, pady=PADY)

        @handle_errors
        def removing_product():
            if messagebox.askyesno(title="Remove Product", message="Are you sure to remove this product?"):
                if item_type == "Pizza":
                    self.pizzas.remove_product(item_id)
                    messagebox.showinfo(title="Success!", message="Product removed successfully!")
                    remove_product_window.destroy()
                elif item_type == "Snack":
                    self.snacks.remove_product(item_id)
                    messagebox.showinfo(title="Success!", message="Product removed successfully!")
                    remove_product_window.destroy()
                elif item_type == "Drink":
                    self.drinks.remove_product(item_id)
                    messagebox.showinfo(title="Success!", message="Product removed successfully!")
                    remove_product_window.destroy()

        remove_product_button = ttk.Button(remove_product_window, text="Remove Product", command=removing_product)
        remove_product_button.grid(row=1, column=0, padx=PADX, pady=PADY*2)

        cancel_button = ttk.Button(remove_product_window, text="Cancel", command=remove_product_window.destroy)
        cancel_button.grid(row=1, column=1, padx=PADX, pady=PADY*2)

    def show_menu(self):
        self.pizzas.list_products()

    def cleaning_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def waiter_menu(self):
        # Waiter Window Setup
        waiter_window = tk.Toplevel(self.window)
        waiter_window.title("Crazy Pizza Order Services")

        self.left = int(self.display_width / 2 - (WINDOW_WIDTH / 2))
        self.top = int(self.display_height / 2 - (WINDOW_HEIGHT / 2))
        waiter_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{self.left}+{self.top}")
        waiter_window.config(padx=PADX, pady=PADY)
        waiter_window.minsize(int(WINDOW_WIDTH / 1.25), int(WINDOW_HEIGHT / 1.25))

        # Multiple tabs for the waiter window
        notebook = ttk.Notebook(waiter_window)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        notebook.add(tab1, text="Restaurant Menu")
        notebook.add(tab2, text="Orders")
        notebook.pack(fill=tk.BOTH)

        left_frame1 = ttk.Frame(tab1, width=280, height=self.display_height, relief=tk.GROOVE)
        left_frame1.pack(side="left", fill=tk.Y, expand=True, padx=PADX)
        right_frame1 = ttk.Frame(tab1, width=self.display_width, height=self.display_height, relief=tk.GROOVE)
        right_frame1.pack(side="left", fill=tk.BOTH, expand=True)

        self.logo_in_waiter(left_frame1, "crazy_waiter_logo.png")

        pizzas_button = ttk.Button(left_frame1, text="Pizzas", command=lambda: print("Pizzas"))
        pizzas_button.pack(pady=PADY*2)
        snacks_button = ttk.Button(left_frame1, text="Snacks", command=lambda: print("Snacks"))
        snacks_button.pack(pady=PADY*2)
        drinks_button = ttk.Button(left_frame1, text="Drinks", command=lambda: print("Drinks"))
        drinks_button.pack(pady=PADY*2)

        # Placing grip at the corner
        grip = ttk.Sizegrip(waiter_window)
        grip.place(relx=1.0, rely=1.0, anchor="se")

    def chef_menu(self):
        # Chef Window Setup
        chef_window = tk.Toplevel(self.window)
        chef_window.title("Crazy Pizza Cooking Services")

        self.left = int(self.display_width / 2 - (WINDOW_WIDTH / 2))
        self.top = int(self.display_height / 2 - (WINDOW_HEIGHT / 2))
        chef_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{self.left}+{self.top}")
        chef_window.config(padx=PADX, pady=PADY)
        chef_window.minsize(int(WINDOW_WIDTH / 1.25), int(WINDOW_HEIGHT / 1.25))

        # Multiple tabs for the chef window
        notebook = ttk.Notebook(chef_window)
        tab1 = ttk.Frame(notebook)
        tab2 = ttk.Frame(notebook)
        notebook.add(tab1, text="Restaurant Menu")
        notebook.add(tab2, text="Orders")
        notebook.pack(fill=tk.BOTH)

        left_frame1 = ttk.Frame(tab1, width=280, height=self.display_height, relief=tk.GROOVE)
        left_frame1.pack(side="left", fill=tk.Y, expand=True, padx=PADX)
        right_frame1 = ttk.Frame(tab1, width=self.display_width, height=self.display_height, relief=tk.GROOVE)
        right_frame1.pack(side="left", fill=tk.BOTH, expand=True)

        self.logo_in_chef(left_frame1, "crazy_chef_logo.png")

        pizzas_button = ttk.Button(left_frame1, text="Pizzas", command=lambda: print("Pizzas"))
        pizzas_button.pack(pady=PADY*2)
        snacks_button = ttk.Button(left_frame1, text="Snacks", command=lambda: print("Snacks"))
        snacks_button.pack(pady=PADY*2)
        drinks_button = ttk.Button(left_frame1, text="Drinks", command=lambda: print("Drinks"))
        drinks_button.pack(pady=PADY*2)

        # Placing grip at the corner
        grip = ttk.Sizegrip(chef_window)
        grip.place(relx=1.0, rely=1.0, anchor="se")

    def logo_in_manager(self, frame, logo):
        logo_canvas = tk.Canvas(frame, width=374, height=275)
        logo_canvas.pack(padx=PADX, pady=PADY*2)
        self.manager_image = tk.PhotoImage(file=f"{logo}")
        logo_canvas.create_image(187, 138, image=self.manager_image)

    def logo_in_waiter(self, frame, logo):
        logo_canvas = tk.Canvas(frame, width=374, height=275)
        logo_canvas.pack(padx=PADX, pady=PADY*2)
        self.waiter_image = tk.PhotoImage(file=f"{logo}")
        logo_canvas.create_image(187, 138, image=self.waiter_image)

    def logo_in_chef(self, frame, logo):
        logo_canvas = tk.Canvas(frame, width=374, height=275)
        logo_canvas.pack(padx=PADX, pady=PADY*2)
        self.chef_image = tk.PhotoImage(file=f"{logo}")
        logo_canvas.create_image(187, 138, image=self.chef_image)


def main():
    window = tk.Tk()
    app = GUI(window)
    app.window.mainloop()


if __name__ == "__main__":
    main()


