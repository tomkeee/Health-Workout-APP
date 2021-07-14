from django.apps import AppConfig


class ExerciseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exercise'

    def ready(self):
        import exercise.signals
