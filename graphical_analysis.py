
import csv
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import os
import openpyxl
import pandas as pd
from PIL import Image, ImageTk
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "Project")

# Main application window
window = tk.Tk()
window.geometry('450x300')

# Try loading background image if available
try:
    image = Image.open("Image01.jpeg")
    photo = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.grid(row=0, column=0, sticky="nsew")
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
except Exception as e:
    print("Error loading background image:", e)

# Example database connection function
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        if conn.is_connected():
            return conn
        else:
            return None
    except Exception as e:
        print("Database connection error:", e)
        return None

# The rest of your functions (create tables, insert data, generate graphs) go here...
# Make sure to remove any hardcoded credentials or sensitive file paths.

if __name__ == "__main__":
    window.mainloop()
