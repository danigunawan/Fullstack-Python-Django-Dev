# apps.py ini berfungsi untuk menempatkan konfigurasi aplikasi pada django python yang spesifik
# contoh dibawah ini mengimport AppConfig
# dan membuat object / kelas FirstAppConfig beserta parameter AppConfig
from django.apps import AppConfig


class FirstAppConfig(AppConfig):
    name = 'first_app'
