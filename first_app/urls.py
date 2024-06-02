from django.urls import path


from first_app.views import greeting

urlpatterns = [
    path('', greeting, name='greeting'),
]
