
# Graphical Analysis Project

A Python Tkinter application for visualizing and managing student performance data, 
with MySQL database integration and Matplotlib graph generation.

## Features
- GUI interface using Tkinter
- MySQL database storage
- Automatic bar/line graph generation with Matplotlib
- Export to Excel with embedded graphs

## Requirements
- Python 3.x
- MySQL Server
- Packages: `tkinter`, `matplotlib`, `numpy`, `mysql-connector-python`, `pandas`, `openpyxl`, `Pillow`, `python-dotenv`

## Setup
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=Project
   ```
4. Run the application:
   ```bash
   python graphical_analysis.py
   ```

## Notes
- Keep `.env` private and **never commit it** to GitHub.
- Generated `.xlsx`, `.csv`, and `.png` files are ignored via `.gitignore`.
