from flask import Blueprint

# Создаем Blueprint с префиксом /admin
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_panel():
    return "Админ-панель: Главная страница"

@admin_bp.route('/users')
def manage_users():
    return "Админ-панель: Управление пользователями"

@admin_bp.route('/stats')
def statistics():
    return "Админ-панель: Статистика системы"
