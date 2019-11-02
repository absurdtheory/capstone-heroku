from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'backend.posts'

    def ready(self):
        import backend.posts.signals
