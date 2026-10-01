
Expense Tracker 💰

A simple and user-friendly expense tracking web application built with Python and Flask. It allows users to record expenses, view their spending, and manage transactions through a clean dashboard.

🌐 Live Demo

Try the application: https://expense-tracker-32s5.onrender.com/

✨ Features

- Add Expenses: Record an expense using a category and amount.
- View Expenses: See all recorded expenses in one place.
- Calculate Total Spending: Automatically calculate the total of recorded expenses.
- Delete Expenses: Remove individual expense entries.
- Input Validation: Prevent empty categories, invalid amounts, and zero or negative amounts.
- Data Persistence: Store expense records in a JSON file when running locally.
- Responsive Interface: A clean dashboard designed using HTML and CSS.

🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JSON
- Git and GitHub
- Render

📁 Project Structure

Expense-Tracker/
├── app.py
├── expense_tracker.py
├── requirements.txt
├── .gitignore
├── expenses.json
├── templates/
│   └── index.html
└── static/
    └── style.css

The "expenses.json" file is created locally when needed and is excluded from GitHub to avoid publishing personal expense records.

🚀 Run Locally

1. Clone the repository

git clone https://github.com/shrutx213/Expense-Tracker.git

2. Open the project folder

cd Expense-Tracker

3. Install dependencies

pip install -r requirements.txt

4. Start the application

python app.py

5. Open the application

Visit http://127.0.0.1:5000/ in your browser.

⚠️ Deployment Note

The application uses a local JSON file for storage. The hosted demo may not retain changes across service restarts or redeployments. Persistent storage or a database would be needed for more reliable hosted data storage.

🎯 Project Objective

This project was created to practise Python programming, Flask web development, HTML and CSS, input validation, file handling, and Git-based version control.

👩‍💻 Author

Shruti Bute

GitHub: https://github.com/shrutx213

---

Built as a learning project to develop practical web development skills.