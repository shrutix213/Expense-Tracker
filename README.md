💰 Expense Tracker

A simple web-based expense tracking application built using Python and Flask. This project helps users record expenses, view transactions, calculate total spending, and delete expense entries through a clean dashboard.

🌐 Live Demo

"Open Expense Tracker" (https://expense-tracker-32s5.onrender.com/)

✨ Features

- Add Expenses: Record expenses with a category and amount.
- View Transactions: Display recorded expenses in a list.
- Automatic Total: Calculate total spending automatically.
- Delete Expenses: Remove individual expense records.
- Input Validation: Reject empty categories and invalid, zero, or negative amounts.
- JSON Storage: Save expense records locally in a JSON file.
- Responsive Design: Use the dashboard on desktop and mobile screens.

🛠️ Tech Stack

Technology| Purpose
Python| Application logic
Flask| Web framework
HTML5| Page structure
CSS3| Styling and layout
JSON| Local data storage
Git & GitHub| Version control
Render| Web hosting

📸 Screenshots

<!-- Add a screenshot after saving it to screenshots/dashboard.png --><!-- ![Expense Tracker Dashboard](screenshots/dashboard.png) -->📁 Project Structure

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

Note: "expenses.json" is created locally when needed and is excluded from the GitHub repository.

🚀 Run Locally

Prerequisites

- Python installed
- pip package installer

1. Clone the repository

git clone https://github.com/shrutx213/Expense-Tracker.git

2. Navigate to the project folder

cd Expense-Tracker

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open the application

Visit "http://127.0.0.1:5000/" (http://127.0.0.1:5000/) in your browser.

⚠️ Storage Limitation

The application uses a local JSON file to store expenses. The hosted demo may not retain changes after a service restart or redeployment because the hosting filesystem may be temporary. Persistent storage or a database would be needed for more reliable hosted storage.

🎯 Learning Objectives

This project was built to practise:

- Python programming and functions
- Flask routes and form handling
- HTML templates and CSS styling
- Input validation and exception handling
- Reading and writing JSON files
- Git, GitHub, and web deployment

👩‍💻 Author

Shruti Bute

"GitHub Profile" (https://github.com/shrutx213)

---

Built as a beginner project to practise Python and web development.