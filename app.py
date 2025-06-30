
from flask import Flask, render_template, request, redirect, url_for, session
import os
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "defaultsecret")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        code = request.form.get("invite_code")
        if code == "TRIAL-2025-1234":
            session["user"] = "invited"
            return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if session.get("user") == "invited":
        return render_template("dashboard.html")
    return redirect(url_for("login"))

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        message = request.form.get("message")
        print(f"Feedback: {message}")
        return redirect(url_for("dashboard"))
    return render_template("feedback.html")


@app.route("/prices")
def prices():
    prices = [1000, 1200, 900, 1500, 1300]
    plt.figure()
    plt.plot(prices, marker="o")
    plt.title("Mercari Prices")
    plt.xlabel("Item")
    plt.ylabel("Price (yen)")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()
    return render_template("prices.html", graph=img_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
