# 📚 Library Manager 

A simple library management system that runs in the terminal.  
Built with pure Python (no external libraries) to practice:

- File handling with JSON
- CRUD operations (Create, Read, Update, Delete)
- Date handling and fine calculation
- Menu‑driven user interface

## 🚀 Features

| Option | Description |
|--------|-------------|
| 1 | Add a new book (title, author, quantity) |
| 2 | View all books (with total & available copies) |
| 3 | Search books by title or author |
| 4 | Register a new library member |
| 5 | Borrow a book (sets due date = today + 14 days) |
| 6 | Return a book (calculates late fine: $1/day) |
| 7 | View all borrowing records |
| 8 | Exit |

## 📂 How Data Is Stored

All data is stored inside a `data/` folder as JSON files:

- `data/books.json` – book information (id, title, author, quantity, available)
- `data/members.json` – member information (id, name, email, joined date)
- `data/borrowings.json` – borrowing records (member, book, borrow date, due date, returned flag, fine)

## ▶️ How to Run

1. Make sure you have **Python 3.6+** installed.
2. Open a terminal in the project folder.
3. Run the command:
   ```bash
   python library.py
