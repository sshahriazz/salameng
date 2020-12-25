from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'user'

    def ready(self):  # menages the signals during creating user
        import user.signals