from django.urls import path

from . import views

urlpatterns = [
    path('', views.main),
    path('solution/<int:id>', views.solution),
    path('question/<int:question_number>', views.question),
    path('new-sol', views.new_sol),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('sign_up', views.sign_up),
    path('like', views.like),
    path('reply', views.reply),



]