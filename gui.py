from idlelib.configdialog import changes
from tkinter import *
from typing import AnyStr


class Gui:
    def __init__(self, window) -> None:
        '''
        Method used to set up the GUI
        :param window: The window used to set up the GUI
        '''
        self.window = window

        # Labels for the tax and menu header
        self.label_menu = Label(self.window, text='MENU', padx=5, pady=5)
        self.label_tax = Label(self.window, text='Tax rate is 5.5%', padx=5, pady=5)
        self.label_menu.pack()
        self.label_tax.pack()

        # Label for entrees sub header
        self.label_entrees = Label(self.window, text='ENTREES', padx=5, pady=5, fg='green')
        self.label_entrees.pack(anchor='w')

        # Labels for the sandwich option and the quantity, checkbutton for the sandwich option, and entry for the quantity
        self.frame_sandwich = Frame(self.window)
        self.label_sandwich_quantity = Label(self.frame_sandwich, text='Quantity: ', padx=5, pady=5)
        self.entry_sandwich = Entry(self.frame_sandwich, width=5)
        self.sandwich_is_checked = IntVar()
        self.checkbutton_sandwich = Checkbutton(self.frame_sandwich, text='Sandwich', variable=self.sandwich_is_checked, command=self.show)
        self.label_sandwich_price = Label(self.frame_sandwich, text='$2.50', padx=5, pady=5)
        self.label_sandwich_error = Label(self.frame_sandwich, text='', padx=5, pady=5)
        self.checkbutton_sandwich.pack(side='left')
        self.label_sandwich_price.pack(side='left')
        self.label_sandwich_error.pack(side='left')
        self.frame_sandwich.pack(anchor='w')

        # Labels for the hotdog option and the quantity, checkbutton for the hotdog option, and entry for the quantity
        self.frame_hotdog = Frame(self.window)
        self.label_hotdog_quantity = Label(self.frame_hotdog, text='Quantity: ', padx=5, pady=5)
        self.entry_hotdog = Entry(self.frame_hotdog, width=5)
        self.hotdog_is_checked = IntVar()
        self.checkbutton_hotdog = Checkbutton(self.frame_hotdog, text='Hot Dog', variable=self.hotdog_is_checked, command=self.show)
        self.label_hotdog_price = Label(self.frame_hotdog, text='$1.50', padx=5, pady=5)
        self.label_hotdog_quantity = Label(self.frame_hotdog, text='Quantity: ', padx=5, pady=5)
        self.entry_hotdog = Entry(self.frame_hotdog, width=5)
        self.label_hotdog_error = Label(self.frame_hotdog, text='', padx=5, pady=5)
        self.checkbutton_hotdog.pack(side='left')
        self.label_hotdog_price.pack(side='left')
        self.label_hotdog_error.pack(side='left')
        self.frame_hotdog.pack(anchor='w')

        # Labels for the burger option and the quantity, checkbutton for the burger option, and entry for the quantity
        self.frame_burger = Frame(self.window)
        self.label_burger_quantity = Label(self.frame_burger, text='Quantity: ', padx=5, pady=5)
        self.entry_burger = Entry(self.frame_burger, width=5)
        self.burger_is_checked = IntVar()
        self.checkbutton_burger = Checkbutton(self.frame_burger, text='Burger', variable=self.burger_is_checked, command=self.show)
        self.label_burger_price = Label(self.frame_burger, text='$3.00', padx=5, pady=5)
        self.label_burger_error = Label(self.frame_burger, text='', padx=5, pady=5)
        self.checkbutton_burger.pack(side='left')
        self.label_burger_price.pack(side='left')
        self.label_burger_error.pack(side='left')
        self.frame_burger.pack(anchor='w')

        # Label for the sides sub header
        self.label_sides = Label(self.window, text='SIDES', padx=5, pady=5, fg='green')
        self.label_sides.pack(anchor='w')

        # Labels for the fries option and the quantity, checkbutton for the fries option, and entry for the quantity
        self.frame_fries = Frame(self.window)
        self.label_fries_quantity = Label(self.frame_fries, text='Quantity: ', padx=5, pady=5)
        self.entry_fries = Entry(self.frame_fries, width=5)
        self.fries_is_checked = IntVar()
        self.checkbutton_fries = Checkbutton(self.frame_fries, text='Fries', variable= self.fries_is_checked, command= self.show)
        self.label_fries_price = Label(self.frame_fries, text='$1.00', padx=5, pady=5)
        self.label_fries_error = Label(self.frame_fries, text='', padx=5, pady=5)
        self.checkbutton_fries.pack(side='left')
        self.label_fries_price.pack(side='left')
        self.label_fries_error.pack(side='left')
        self.frame_fries.pack(anchor='w')

        # Labels for the onion ring option and the quantity, checkbutton for the onion ring option, and entry for the quantity
        self.frame_onion_rings = Frame(self.window)
        self.label_onion_rings_quantity = Label(self.frame_onion_rings, text='Quantity: ', padx=5, pady=5)
        self.entry_onion_rings = Entry(self.frame_onion_rings, width=5)
        self.onion_rings_is_checked = IntVar()
        self.checkbutton_onion_rings = Checkbutton(self.frame_onion_rings, text='Onion Rings', variable= self.onion_rings_is_checked, command= self.show)
        self.label_onion_rings_price = Label(self.frame_onion_rings, text='$1.75', padx=5, pady=5)
        self.label_onion_rings_error = Label(self.frame_onion_rings, text='', padx=5, pady=5)
        self.checkbutton_onion_rings.pack(side='left')
        self.label_onion_rings_price.pack(side='left')
        self.label_onion_rings_error.pack(side='left')
        self.frame_onion_rings.pack(anchor='w')

        # Labels for the chips option and the quantity, checkbutton for the chips option, and entry for the quantity
        self.frame_chips = Frame(self.window)
        self.label_chips_quantity = Label(self.frame_chips, text='Quantity: ', padx=5, pady=5)
        self.entry_chips = Entry(self.frame_chips, width=5)
        self.chips_is_checked = IntVar()
        self.checkbutton_chips = Checkbutton(self.frame_chips, text='Chips', variable= self.chips_is_checked, command= self.show)
        self.label_chips_price = Label(self.frame_chips, text='$0.75', padx=5, pady=5)
        self.label_chips_error = Label(self.frame_chips, text='', padx=5, pady=5)
        self.checkbutton_chips.pack(side='left')
        self.label_chips_price.pack(side='left')
        self.label_chips_error.pack(side='left')
        self.frame_chips.pack(anchor='w')

        # Label for the drinks sub header
        self.label_drinks = Label(self.window, text='DRINKS', padx=5, pady=5, fg='green')
        self.label_drinks.pack(anchor='w')

        # Labels for the soda option and the quantity, checkbutton for the soda option, and entry for the quantity
        self.frame_soda = Frame(self.window)
        self.label_soda_quantity = Label(self.frame_soda, text='Quantity: ', padx=5, pady=5)
        self.entry_soda = Entry(self.frame_soda, width=5)
        self.soda_is_checked = IntVar()
        self.checkbutton_soda = Checkbutton(self.frame_soda, text='Soda', variable= self.soda_is_checked, command= self.show)
        self.label_soda_price = Label(self.frame_soda, text='$1.00', padx=5, pady=5)
        self.label_soda_error = Label(self.frame_soda, text='', padx=5, pady=5)
        self.checkbutton_soda.pack(side='left')
        self.label_soda_price.pack(side='left')
        self.label_soda_error.pack(side='left')
        self.frame_soda.pack(anchor='w')

        # Labels for the juice option and the quantity, checkbutton for the juice option, and entry for the quantity
        self.frame_juice = Frame(self.window)
        self.label_juice_quantity = Label(self.frame_juice, text='Quantity: ', padx=5, pady=5)
        self.entry_juice = Entry(self.frame_juice, width=5)
        self.juice_is_checked = IntVar()
        self.checkbutton_juice = Checkbutton(self.frame_juice, text='Juice', variable= self.juice_is_checked, command= self.show)
        self.label_juice_price = Label(self.frame_juice, text='$0.75', padx=5, pady=5)
        self.label_juice_error = Label(self.frame_juice, text='', padx=5, pady=5)
        self.checkbutton_juice.pack(side='left')
        self.label_juice_price.pack(side='left')
        self.label_juice_error.pack(side='left')
        self.frame_juice.pack(anchor='w')

        # Submit button and label for the total amount
        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='SUBMIT', command=self.submit, padx=5, pady=5)
        self.label_total = Label(self.frame_submit, text='', padx=5, pady=5)
        self.button_submit.pack(side='top')
        self.label_total.pack(side='bottom')
        self.frame_submit.pack()

        self.button_clear = Button(self.window, text='CLEAR', command=self.clear)
        self.button_clear.pack()

    def submit(self) -> None:
        '''
        Method used to add up the price of all selected items and their quantities plus tax to reach the total price
        '''
        # List containing all error labels for each item
        error_labels = [
            self.label_sandwich_error, self.label_hotdog_error, self.label_burger_error, self.label_fries_error, self.label_onion_rings_error,
            self.label_chips_error, self.label_soda_error, self.label_juice_error
        ]
        # List containing all entry boxes for each item
        quantities = [
            self.entry_sandwich, self.entry_hotdog, self.entry_burger, self.entry_fries, self.entry_onion_rings,
            self.entry_chips, self.entry_soda, self.entry_juice
        ]
        # List containing the checked or unchecked value of each checkbutton
        values = [
            self.sandwich_is_checked, self.hotdog_is_checked, self.burger_is_checked, self.fries_is_checked,
            self.onion_rings_is_checked,
            self.chips_is_checked, self.soda_is_checked, self.juice_is_checked
        ]
        # Prices of each item
        prices = [2.50, 1.50, 3.00, 1.00, 1.75, 0.75, 1.00, 0.75]
        total = 0
        data_is_valid = True

        '''
        Verifies that all information is entered and is valid. If it is not error labels are activated
        and changed accordingly. If the information entered is valid the boolean variable data_is_valid
        will remain true.
        '''
        for quantity in quantities:
            this_data_is_valid = True
            new_quantity = 0
            if quantity.get() == '' and values[quantities.index(quantity)].get():
                error_labels[quantities.index(quantity)].config(text='Please fill in box', fg='red')
                self.label_total.config(text='')
                data_is_valid = False
                this_data_is_valid = False
            elif values[quantities.index(quantity)].get():
                try:
                    new_quantity = int(quantity.get())
                except ValueError:
                    error_labels[quantities.index(quantity)].config(text='Please enter a valid number', fg='red')
                    self.label_total.config(text='')
                    data_is_valid = False
                    this_data_is_valid = False
                    # break
                if this_data_is_valid:
                    error_labels[quantities.index(quantity)].config(text='')
                    total += new_quantity * prices[quantities.index(quantity)]

        # Checking to see if the form is empty. If it is total label tells user to enter information.
        if data_is_valid and total == 0:
            data_is_valid = False
            self.label_total.config(text='Please fill out the form')

        # Checking to see if data is valid. If it is then total is calculated with tax and displayed.
        if data_is_valid:
            self.label_total.config(text=f'Your total is ${round(total + (total * 0.055), 2)}', fg='green')


    def show(self) -> None:
        '''
        Method used to hide or unhide the quantity label and entry box for an item whose checkbutton is checked or
        unchecked.
        '''
        # List containing the checked or unchecked value of each checkbutton
        values = [
            self.sandwich_is_checked, self.hotdog_is_checked, self.burger_is_checked, self.fries_is_checked, self.onion_rings_is_checked,
            self.chips_is_checked, self.soda_is_checked, self.juice_is_checked
        ]
        # List containing all quantity labels for each item
        labels = [
            self.label_sandwich_quantity, self.label_hotdog_quantity, self.label_burger_quantity, self.label_fries_quantity,
            self.label_onion_rings_quantity, self.label_chips_quantity, self.label_soda_quantity, self.label_juice_quantity
        ]
        # List containing all entry boxes for each item
        entries = [
            self.entry_sandwich, self.entry_hotdog, self.entry_burger, self.entry_fries, self.entry_onion_rings, self.entry_chips,
            self.entry_soda, self.entry_juice
        ]
        # List containing all error labels for each item
        error_labels = [
            self.label_sandwich_error, self.label_hotdog_error, self.label_burger_error, self.label_fries_error,
            self.label_onion_rings_error,
            self.label_chips_error, self.label_soda_error, self.label_juice_error
        ]
        # Hides and unhides the entry and quantity label of the item depending on the status of the checkbutton
        for value in values:
            if value.get():
                labels[values.index(value)].pack(side='left')
                entries[values.index(value)].pack(side='left')
            else:
                entries[values.index(value)].delete(0, END)
                error_labels[values.index(value)].config(text='')
                self.label_total.config(text='')
                labels[values.index(value)].pack_forget()
                entries[values.index(value)].pack_forget()

    def clear(self) -> None:
        '''
        Method used to clear all information and reset the menu to its original state
        '''
        # Clears the total label
        self.label_total.config(text='')
        # List of all error labels
        error_labels = [
            self.label_sandwich_error, self.label_hotdog_error, self.label_burger_error, self.label_fries_error,
            self.label_onion_rings_error,
            self.label_chips_error, self.label_soda_error, self.label_juice_error
        ]
        # List of all quantity labels
        labels = [
            self.label_sandwich_quantity, self.label_hotdog_quantity, self.label_burger_quantity,
            self.label_fries_quantity,
            self.label_onion_rings_quantity, self.label_chips_quantity, self.label_soda_quantity,
            self.label_juice_quantity
        ]
        # List of all entries
        entries = [
            self.entry_sandwich, self.entry_hotdog, self.entry_burger, self.entry_fries, self.entry_onion_rings,
            self.entry_chips,
            self.entry_soda, self.entry_juice
        ]
        # List of all check_button values
        values = [
            self.sandwich_is_checked, self.hotdog_is_checked, self.burger_is_checked, self.fries_is_checked,
            self.onion_rings_is_checked,
            self.chips_is_checked, self.soda_is_checked, self.juice_is_checked
        ]
        # Sets all check_buttons to unchecked
        for check_button in values:
            check_button.set(0)
        # Unpacks all labels, error labels, and entries (clears entries as well)
        for label in error_labels:
            label.config(text='')
        for label in labels:
            label.pack_forget()
        for entry in entries:
            entry.delete(0, END)
            entry.pack_forget()

