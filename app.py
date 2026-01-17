from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    links = []

    if request.method == "POST":
        phone = request.form.get("phone", "").strip()
        username = request.form.get("username", "").strip()

        # -------- PHONE OSINT (расширенный) --------
        if phone:
            clean_phone = phone.replace("+", "").replace(" ", "")

            links.extend([
                # Search engines
                f"https://www.google.com/search?q={phone}",
                f"https://yandex.ru/search/?text={phone}",

                # Telegram
                f"https://t.me/{clean_phone}",
                f"https://www.google.com/search?q=site:t.me+{clean_phone}",

                # VK
                f"https://vk.com/search?c[q]={clean_phone}&c[section]=people",
                f"https://www.google.com/search?q=site:vk.com+{clean_phone}",

                # WhatsApp
                f"https://wa.me/{clean_phone}",
                f"https://www.google.com/search?q=site:wa.me+{clean_phone}",

                # Facebook
                f"https://www.facebook.com/search/top/?q={clean_phone}",
                f"https://www.google.com/search?q=site:facebook.com+{clean_phone}",

                # Marketplaces
                f"https://www.google.com/search?q=site:avito.ru+{clean_phone}",
                f"https://www.google.com/search?q=site:olx.ua+{clean_phone}",

                # Caller info
                f"https://www.truecaller.com/search/{clean_phone}",
                f"https://www.google.com/search?q=site:getcontact.com+{clean_phone}"
            ])

        # -------- USERNAME OSINT (БЕЗ ИЗМЕНЕНИЙ) --------
        if username:
            links.extend([
                f"https://t.me/{username}",
                f"https://www.tiktok.com/@{username}",
                f"https://www.instagram.com/{username}",
                f"https://github.com/{username}",
                f"https://www.google.com/search?q={username}"
            ])

    return render_template("index.html", links=links)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
