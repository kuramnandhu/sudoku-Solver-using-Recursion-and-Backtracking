from flask import Flask, render_template, request
from solver import solve

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    solved_board = None
    if request.method == "POST":
        # Get user input as 2D array
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = request.form.get(f"cell-{i}-{j}")
                row.append(int(value) if value else 0)
            board.append(row)

        solve(board)
        solved_board = board

    return render_template("index.html", solved_board=solved_board)

if __name__ == "__main__":
    app.run(debug=True)
