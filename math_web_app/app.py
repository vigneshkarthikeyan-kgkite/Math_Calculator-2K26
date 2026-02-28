from flask import Flask, render_template, request

app = Flask(__name__)

# ===============================
# 1. Newton-Raphson Method
# ===============================
def newton_raphson(x0, tolerance, max_iter):
    def f(x):
        return x**3 - x - 2

    def df(x):
        return 3*x**2 - 1

    steps = []

    for i in range(max_iter):
        if df(x0) == 0:
            return steps, "Derivative became zero. Method failed."

        x1 = x0 - f(x0)/df(x0)
        steps.append(f"Iteration {i+1}: x = {x1}")

        if abs(x1 - x0) < tolerance:
            return steps, f"Root found: {x1}"

        x0 = x1

    return steps, "Method did not converge."


# ===============================
# 2. Newton Forward Interpolation
# ===============================
def newton_forward(x_values, y_values, value):
    n = len(x_values)
    diff = [y_values.copy()]

    for i in range(1, n):
        temp = []
        for j in range(n - i):
            temp.append(diff[i-1][j+1] - diff[i-1][j])
        diff.append(temp)

    h = x_values[1] - x_values[0]
    p = (value - x_values[0]) / h

    result = y_values[0]
    p_term = 1
    factorial = 1

    for i in range(1, n):
        p_term *= (p - i + 1)
        factorial *= i
        result += (p_term * diff[i][0]) / factorial

    return result


# ===============================
# 3. Euler Method
# ===============================
def euler_method(x0, y0, h, xn):
    def f(x, y):
        return x + y

    steps = []
    x = x0
    y = y0

    while x < xn:
        y = y + h * f(x, y)
        x = x + h
        steps.append(f"x = {x}, y = {y}")

    return steps, y


# ===============================
# Main Route
# ===============================
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    steps = []
    error = None

    if request.method == "POST":
        method = request.form.get("method")

        try:
            # Newton-Raphson
            if method == "newton":
                x0 = float(request.form["x0"])
                tolerance = float(request.form["tolerance"])
                max_iter = int(request.form["max_iter"])
                steps, result = newton_raphson(x0, tolerance, max_iter)

            # Interpolation
            elif method == "interpolation":
                x_values = list(map(float, request.form["x_values"].split(",")))
                y_values = list(map(float, request.form["y_values"].split(",")))
                value = float(request.form["value"])
                result = newton_forward(x_values, y_values, value)

            # Euler
            elif method == "euler":
                x0 = float(request.form["x0"])
                y0 = float(request.form["y0"])
                h = float(request.form["h"])
                xn = float(request.form["xn"])
                steps, result = euler_method(x0, y0, h, xn)

        except:
            error = "Invalid input. Please check values."

    return render_template("index.html",
                           result=result,
                           steps=steps,
                           error=error)


if __name__ == "__main__":
    app.run(debug=True)