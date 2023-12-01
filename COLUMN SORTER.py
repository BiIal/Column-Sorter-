import tkinter as tk
from tkinter import filedialog
import pandas as pd

class CSVSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV Sorter Utility")

        self.file_path = None

    
        self.label = tk.Label(root, text="Choose a CSV file:")
        self.label.pack(pady=10)

        self.choose_button = tk.Button(root, text="Choose File", command=self.choose_file)
        self.choose_button.pack(pady=10)

        self.sort_button = tk.Button(root, text="Sort File", command=self.sort_file)
        self.sort_button.pack(pady=10)

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.label.config(text=f"File chosen: {self.file_path}")

    def sort_file(self):
        if self.file_path:
            try:
                df = pd.read_csv(self.file_path)
                column_to_sort = input("Enter the column name to sort by: ")
                ascending_order = input("Sort in ascending order? (y/n): ").lower() == 'y'
                df_sorted = df.sort_values(by=column_to_sort, ascending=ascending_order)
                df_sorted.to_csv(self.file_path, index=False)

                print("File sorted and updated successfully!")

            except Exception as e:
                print("Error:", e)
        else:
            print("Please choose a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CSVSorterApp(root)
    root.mainloop()

