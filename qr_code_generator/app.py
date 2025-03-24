from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)

# Путь для временного хранения QR-кода
QR_CODE_PATH = "static/qr_code.png"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные из формы
        url = request.form.get("url")
        fill_color = request.form.get("fill_color", "black")  # Цвет переднего плана
        back_color = request.form.get("back_color", "white")  # Цвет фона

        if url:
            # Генерируем QR-код
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)

            img = qr.make_image(fill_color=fill_color, back_color=back_color)

            # Сохраняем QR-код во временную папку
            img.save(QR_CODE_PATH)

            # Передаем путь к QR-коду и выбранные цвета в шаблон
            return render_template("index.html", qr_code_path=QR_CODE_PATH, fill_color=fill_color,
                                   back_color=back_color)

    # Если метод GET или форма пустая, показываем форму
    return render_template("index.html")


if __name__ == "__main__":
    # Создаем папку static, если её нет
    if not os.path.exists("static"):
        os.makedirs("static")

    app.run(debug=True)