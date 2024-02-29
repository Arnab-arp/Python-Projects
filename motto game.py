# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 1:33:45 2024

@author: Fahim Afridi
@author: Arnab Pramanik
"""

import hashlib
import sqlite3
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

DB_FILE = "motto_game.db"


def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mottos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            commonuser TEXT,
            motto TEXT,
            timestamp TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            motto TEXT
        )
    ''')
    conn.commit()
    conn.close()


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def motto_submission(common_user, motto):
    timestamp = str(datetime.now())
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mottos (commonuser, motto, timestamp) VALUES (?, ?, ?)",
                   (common_user, motto, timestamp))
    conn.commit()
    conn.close()


def admin_signup(username, admin_pass, motto):
    password_hash = hashlib.sha256(admin_pass.encode()).hexdigest()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO admins (username, password, motto) VALUES (?, ?, ?)", (username, password_hash, motto))
    conn.commit()
    conn.close()


def admin_login(username, admin_pass):
    password_hash = hashlib.sha256(admin_pass.encode()).hexdigest()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admins WHERE username=?", (username,))
    admin = cursor.fetchone()
    conn.close()
    return admin if admin and admin[2] == password_hash else None


def set_motto(admin_id, new_motto):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE admins SET motto=? WHERE id=?", (new_motto, admin_id))
    conn.commit()
    conn.close()


def show_the_graph(admin_motto):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mottos")
    all_mottos = cursor.fetchall()
    cursor.execute("SELECT username, motto FROM admins WHERE motto=?", (admin_motto,))
    admin_entry = cursor.fetchone()
    conn.close()

    leaderboard = sorted(all_mottos, key=lambda x: (levenshtein_distance(x[2], admin_motto), x[3]))
    
    users = [entry[1] for entry in leaderboard if entry[1] != admin_entry[0]]
    edit_distances = [levenshtein_distance(entry[2], admin_motto) for entry in leaderboard if
                      entry[1] != admin_entry[0]]

    plt.figure(figsize=(10, 6))
    plt.bar(users, edit_distances, color='orange')
    plt.xlabel('User')
    plt.ylabel('Edit Distance')
    plt.title('Edit Distances from Admin Motto')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def show_leaderboard(admin_motto):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mottos")
    all_mottos = cursor.fetchall()
    cursor.execute("SELECT username, motto FROM admins WHERE motto=?", (admin_motto,))
    admin_entry = cursor.fetchone()
    conn.close()

    leaderboard = sorted(all_mottos, key=lambda x: (levenshtein_distance(x[2], admin_motto), x[3]))

    leaderboard_window = tk.Toplevel()
    leaderboard_window.geometry('500x500')
    leaderboard_window.configure(bg='Yellow')
    tk.Label(leaderboard_window, text='Leaderboard', font=('Arial', 24), bg='Yellow').pack()

    admin_frame = tk.Frame(leaderboard_window, bg='white', bd=5)
    admin_frame.pack(pady=10)
    tk.Label(admin_frame, text=f'Admin: {admin_entry[0]} - Motto: {admin_entry[1]}', bg='orange', anchor='w').pack(
        fill='x')

    for entry in leaderboard:
        if entry[1] == admin_entry[0]:
            continue
        frame = tk.Frame(leaderboard_window,
                         bg='white', bd=5)
        frame.pack(pady=10)
        tk.Label(frame,
                 text=f'User: {entry[1]} - Motto: {entry[2]} - Edit Distance: {levenshtein_distance(entry[2], admin_motto)} (Time: {entry[3]})',
                 bg='orange', anchor='w').pack(fill='x')


def UI():
    create_database()
    root = tk.Tk()
    root.geometry('350x350')
    root.configure(bg='light yellow')
    root.title('Motto Game')

    def submit_motto():
        root.withdraw()
        new_window = tk.Toplevel(root)
        new_window.geometry('350x350')
        new_window.configure(bg='light green')
        new_window.title('Submit Motto')

        tk.Label(new_window, text='Name:', bg='light green').pack()
        user = tk.StringVar()
        entry1 = tk.Entry(new_window, textvariable=user)
        entry1.pack()

        tk.Label(new_window, text='Your Motto:', bg='light green').pack()
        motto = tk.StringVar()
        entry = tk.Entry(new_window, textvariable=motto)
        entry.pack()

        def submit_and_close():
            if user.get() and motto.get():
                motto_submission(user.get(), motto.get())
                new_window.destroy()
                root.deiconify()
            else:
                messagebox.showwarning("Warning", "Name and Motto cannot be empty!")

        tk.Button(new_window, text='Submit', command=submit_and_close, bg='orange').pack(pady=10)

    def admin_login_or_signup():
        root.withdraw()
        new_window = tk.Toplevel(root)
        new_window.geometry('350x350')
        new_window.configure(bg='light green')
        new_window.title('Admin Login/Signup')

        tk.Label(new_window, text='Admin Username:', bg='light green').pack()
        username = tk.StringVar()
        entry1 = tk.Entry(new_window, textvariable=username)
        entry1.pack()

        tk.Label(new_window, text='Password:', bg='light green').pack()
        password = tk.StringVar()
        entry2 = tk.Entry(new_window, textvariable=password, show="*")
        entry2.pack()

        def login_or_signup_and_close():
            if username.get() and password.get():
                admin = admin_login(username.get(), password.get())
                if admin:
                    admin_dashboard(admin[0])
                else:
                    signup_response = messagebox.askyesno("Admin Not Found",
                                                          "Admin not found. Do you want to create a new admin?")
                    if signup_response:
                        admin_signup(username.get(), password.get(), "Initial Motto")
                    else:
                        messagebox.showerror("Error", "Invalid credentials")
            else:
                messagebox.showwarning("Warning", "Username and Password cannot be empty!")

            new_window.destroy()
            root.deiconify()

        tk.Button(new_window, text='Login/Signup', command=login_or_signup_and_close, bg='orange').pack(pady=10)

    def admin_dashboard(admin_id):
        root.withdraw()
        new_window = tk.Toplevel(root)
        new_window.geometry('350x350')
        new_window.configure(bg='light green')
        new_window.title('Admin Dashboard')

        def set_motto_and_close():
            new_window.withdraw()
            set_motto_window = tk.Toplevel(new_window)
            set_motto_window.geometry('350x350')
            set_motto_window.configure(bg='light green')
            set_motto_window.title('Set Motto')

            tk.Label(set_motto_window, text='Enter a new motto:', bg='light green').pack()
            new_motto = tk.StringVar()
            entry = tk.Entry(set_motto_window, textvariable=new_motto)
            entry.pack()

            def submit_and_close():
                if new_motto.get():
                    set_motto(admin_id, new_motto.get())
                    set_motto_window.destroy()
                    new_window.deiconify()
                else:
                    messagebox.showwarning("Warning", "Motto cannot be empty!")

            tk.Button(set_motto_window, text='Submit', command=submit_and_close, bg='orange').pack(pady=10)

        def show_leaderboard_and_close():
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT motto FROM admins WHERE id=?", (admin_id,))
            admin_motto = cursor.fetchone()[0]
            cursor.execute("SELECT motto FROM mottos WHERE commonuser=?", (admin_id,))
            conn.close()
            show_leaderboard(admin_motto)

        def show_graph_and_close():
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("SELECT motto FROM admins WHERE id=?", (admin_id,))
            admin_motto = cursor.fetchone()[0]
            cursor.execute("SELECT motto FROM mottos WHERE commonuser=?", (admin_id,))
            conn.close()
            show_the_graph(admin_motto)

        def logout_and_close():
            new_window.destroy()
            root.deiconify()

        tk.Button(new_window, text='Set Motto', command=set_motto_and_close, bg='orange').pack(pady=10)
        tk.Button(new_window, text='Show Leaderboard', command=show_leaderboard_and_close, bg='orange').pack(pady=10)
        tk.Button(new_window, text='Show Graph', command=show_graph_and_close, bg='orange').pack(pady=10)
        tk.Button(new_window, text='Logout', command=logout_and_close, bg='orange').pack(pady=10)

    tk.Button(root, text='Submit motto', command=submit_motto, bg='orange').pack(pady=10)
    tk.Button(root, text='Admin login', command=admin_login_or_signup, bg='orange').pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    UI()

   

