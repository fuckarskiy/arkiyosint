from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    links = []

    if request.method == "POST":
        phone = request.form.get("phone", "").strip()
        username = request.form.get("username", "").strip()

        if phone:
            links.extend([
                f"https://www.google.com/search?q={phone}",
                f"https://yandex.ru/search/?text={phone}",
                f"https://www.truecaller.com/search/{phone}"
            ])

        if username:
            links.extend([
                f"https://t.me/{username}",
                f"https://www.tiktok.com/@{username}",
                f"https://www.instagram.com/{username}",
                f"https://github.com/{username}",
                f"https://www.google.com/search?q={username}"
            ])

    return render_template("index.html", links=links)

if name == "__main__":
    app.run(host="0.0.0.0", port=5000)
