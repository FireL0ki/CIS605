# Project:          Module 9 - Example 1
# Description:      GUI to test food item class
# Depends on:       food_item
# Developed By:     LV
# Date:             November 2025

from food_item import  Food_Item as fi

# import tkinter package

import tkinter as tki
import tkinter.messagebox as mb
import re

class Food_Item_GUI:

    def __init__(self):

        #initialize main window and widgets

        self.main_window = tki.Tk()
        self.main_window.option_add("*Font", "Helvetica 12")

        self.top_frame = tki.Frame(self.main_window)
        self.left_frame = tki.LabelFrame(self.main_window)
        self.right_frame = tki.Frame(self.main_window)

        self.header_label = tki.Label(self.top_frame)

        self.name_label = tki.Label(self.left_frame)
        self.name_entry = tki.Entry(self.left_frame)
        self.name_var = tki.StringVar()  # "var" variables are used to establish two-way binding between the variables and the widgets linked to them

        self.fat_label = tki.Label(self.left_frame)
        self.fat_spin = tki.Spinbox(self.left_frame)
        self.fat_var = tki.IntVar()
        
        self.carbs_label = tki.Label(self.left_frame)
        self.carbs_spin = tki.Spinbox(self.left_frame)
        self.carbs_var = tki.IntVar()
        
        self.protein_label = tki.Label(self.left_frame)
        self.protein_spin = tki.Spinbox(self.left_frame)
        self.protein_var = tki.IntVar()
        
        self.calories_label = tki.Label(self.left_frame)
        self.calories_label1 = tki.Label(self.left_frame)
        self.calories_var = tki.StringVar()

        self.create_button = tki.Button(self.right_frame)
        self.summary_button = tki.Button(self.right_frame)
        self.reset_button = tki.Button(self.right_frame)
        self.quit_button = tki.Button(self.right_frame)

        # call the __configure_widgets method

        self.__configure_widgets()

        # call the __create_layout method
        
        self.__create_layout()

    # method to configure the widgets
    
    def __configure_widgets(self):

        self.main_window.title("Food Item GUI")
        self.main_window.geometry("600x300+800+500")
        
        self.left_frame.configure(text="Food Info:")

        self.header_label.configure(text="UI to Test Food Item Class")

        self.name_label.configure(text="Food Name:")

        self.name_entry.configure(textvariable=self.name_var, width=21)
                
        self.fat_label.configure(text="Fat Grams:")
        self.fat_spin.configure(from_=0, to=500, increment=1, justify="right", textvariable=self.fat_var)
        
        self.carbs_label.configure(text="Carbs Grams:")
        self.carbs_spin.configure(from_=0, to=500, increment=1, justify="right", textvariable=self.carbs_var)
        
        self.protein_label.configure(text="Protein Grams:")
        self.protein_spin.configure(from_=0, to=500, increment=1, justify="right", textvariable=self.protein_var)

        self.calories_label.configure(text="Calories:")
        self.calories_label1.configure(textvariable=self.calories_var, font=("Arial", 12, "bold"), relief="sunken", width=10)
        
        self.create_button.configure(text="Initialize Food Item Object", command=self.__validate_input)
        self.summary_button.configure(text="Display Summary", state="disabled", command=self.__summary)
        self.reset_button.configure(text="Reset", command=self.__reset)
        self.quit_button.configure(text="Quit", command=self.main_window.destroy)

    def __create_layout(self):

        # from Gemini 

        # The Tkinter grid geometry manager provides a powerful and flexible way to arrange widgets in a two-dimensional table of rows and columns.  
        # Key Concepts:
        # Rows and Columns: Widgets are placed in specific cells defined by their row and column indices. These indices are zero-based, meaning the top-left cell is (0, 0).
        # Cells: The intersection of a row and a column forms a cell, where a single widget or a container (like a Frame) holding multiple widgets can be placed.
        # Spanning: Widgets can occupy multiple rows (rowspan) or columns (columnspan), similar to merging cells in a spreadsheet.
        # Sticky: The sticky option controls how a widget expands or aligns within its cell. It takes a string combining compass directions (N, S, E, W) to specify alignment (e.g., N for top, NSEW to fill the entire cell).
        # Padding: padx and pady add horizontal and vertical padding around the widget within its cell.
        # Weight: rowconfigure() and columnconfigure() with the weight option determine how extra space is distributed among rows and columns when the window is resized. A higher weight means that row or column will receive a larger share of the available extra space.
        
        self.main_window.columnconfigure(0, weight=1)
        self.main_window.columnconfigure(1, weight=1)
        self.main_window.rowconfigure(0,weight=1)
        self.main_window.rowconfigure(1,weight=1)
       
        self.top_frame.grid(row=0, columnspan=2, padx=10, pady=10)
        
        self.header_label.grid(row=0, column=0)

        self.left_frame.grid(row=1, column=0, padx=10, pady=10)

        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry.grid(row=0,column=1, padx=10, pady=10)
        self.fat_label.grid(row=1, column=0, padx=10, pady=10)
        self.fat_spin.grid(row=1, column=1, padx=10, pady=10)
        self.carbs_label.grid(row=2, column=0, padx=10, pady=10)
        self.carbs_spin.grid(row=2, column=1, padx=10, pady=10)
        self.protein_label.grid(row=3, column=0, padx=10, pady=10)
        self.protein_spin.grid(row=3, column=1, padx=10, pady=10)
        self.calories_label.grid(row=4, column=0, padx=10, pady=10)
        self.calories_label1.grid(row=4, column=1, padx=10, pady=10)

        self.name_entry.focus_set()
        
        self.right_frame.grid(row=1, column=1, padx=10, pady=10)

        self.create_button.grid(row=0,column=0,padx=10, pady=10)
        self.summary_button.grid(row=1,column=0,padx=10, pady=10)
        self.reset_button.grid(row=2,column=0,padx=10, pady=10)
        self.quit_button.grid(row=3,column=0,padx=10, pady=10)

    # event handler to validate input prior to initializing food item object
    
    def __validate_input(self):
        try:
            while True:
                
                food_name = self.name_var.get().strip()
                
                if re.match(r"^[A-Za-z]+([ -][A-Za-z]+)*$", food_name): break
                else: 
                    mb.showerror("Error", "Enter a valid food name")
                    self.name_var.set("")
                    self.name_entry.focus_set()
                    return
            
            while True:

                fat_grams = int(self.fat_var.get())

                if 0 <= fat_grams <= 500: break
                else:
                    mb.showerror("Error", "Fat grams should be between 0 and 500")
                    self.fat_var.set(0)
                    self.fat_spin.focus_set()
                    return

            while True:

                carbs_grams = int(self.carbs_var.get())

                if 0 <= carbs_grams <= 500: break
                else:
                    mb.showerror("Error", "Carbs grams should be between 0 and 500")
                    self.carbs_var.set(0)
                    self.carbs_spin.focus_set()
                    return
                
            while True:

                protein_grams = int(self.protein_var.get())

                if 0 <= protein_grams <= 500: break
                else:
                    mb.showerror("Error", "Protein grams should be between 0 and 500")
                    self.protein_var.set(0)
                    self.protein_spin.focus_set()
                    return
                
        except Exception as e:
            mb.showinfo("Error", f"Something went wrong...{e}")

        else:
            
            # call create food item method

            self.__create_object(food_name, fat_grams, carbs_grams, protein_grams)

    # create food item object

    def __create_object(self, food, fat, carbs, protein):

        self.a_food = fi(food,fat,carbs,protein)
        self.calories_var.set(f"{self.a_food.calories:,}")

        # disable widgets in the food info frame
        
        for child in self.left_frame.winfo_children():
            child.configure(state="disabled")
        
        self.create_button.configure(state="disabled")
        
        self.summary_button.configure(state="normal")
        
    # event handler to reset widgets
    
    def __reset(self):

        self.name_var.set("")
        self.fat_var.set(0)
        self.carbs_var.set(0)
        self.protein_var.set(0)
        self.calories_var.set("")

        self.create_button.configure(state="normal")
        
        for child in self.left_frame.winfo_children():
            child.configure(state="normal")

        self.name_entry.focus_set()

    # event handler to display summary information
    
    def __summary(self):

       mb.showinfo("Summary Information", fi.summary_info())
       
if __name__ == '__main__':
    
    aGUI = Food_Item_GUI()

    tki.mainloop()

        




