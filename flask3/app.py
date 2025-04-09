from flask import Flask
from admin import admin_bp

app = Flask(__name__)

# Регистрируем Blueprint в приложении
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return "Главная страница сайта"

if __name__ == '__main__':
    app.run(debug=True)
