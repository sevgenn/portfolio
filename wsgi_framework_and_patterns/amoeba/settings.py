"""Модуль, определяющий расположение шаблонов."""

import os

settings = {
    'DEBUG': True,

    'BASE_DIR': os.path.dirname(os.path.abspath(__file__)),
    'TEMPLATE_DIR': 'templates',
    'STORAGE_DIR': 'storage',
    'LOG_DIR': 'logs'
}
