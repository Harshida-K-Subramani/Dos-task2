
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""

    if request.method == "POST":
        a = float(request.form["num1"])
        b = float(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = "Cannot divide by zero" if b == 0 else a / b

    return render_template_string("""
    <html>
    <head>
    <title>Calculator</title>
    <style>
    body { background:#dce6f5; font-family:Arial; text-align:center; }
    .box { background:white; width:350px; margin:100px auto;
           padding:30px; border-radius:15px; }
    input,select,button { padding:12px; margin:10px; width:80%; }
    button { background:#263b65; color:white; border:0; cursor:pointer; }
    h2 { color:#263b65; }
    </style>
    </head>
    <body>
    <div class="box">
    <h2>Simple Calculator</h2>
    <form method="POST">
    <input type="number" step="any" name="num1" placeholder="First Number" required>
    <input type="number" step="any" name="num2" placeholder="Second Number" required>
    <select name="operation">
    <option value="add">Addition (+)</option>
    <option value="sub">Subtraction (-)</option>
    <option value="mul">Multiplication (*)</option>
    <option value="div">Division (/)</option>
    </select>
    <button type="submit">Calculate</button>
    </form>
    <h3>Result: {{ result }}</h3>
    </div>
    </body>
    </html>
    """, result=result)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
