from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "expenses.json")

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        expenses = json.load(file)
else:
    expenses = []


def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        category = request.form.get("category", "").strip()
        amount_text = request.form.get("amount", "").strip()

        if not category:
            error = "Please enter an expense category."

        else:
            try:
                amount = int(amount_text)

                if amount <= 0:
                    error = "Amount must be greater than zero."
                else:
                    expenses.append({
                        "category": category,
                        "amount": amount
                    })

                    save_expenses()
                    return redirect("/")

            except ValueError:
                error = "Please enter a valid whole-number amount."

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        error=error
    )


@app.route("/delete/<int:index>", methods=["POST"])
def delete_expense(index):
    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_expenses()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=False)