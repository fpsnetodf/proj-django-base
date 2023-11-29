from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
	path('entrar/', LoginView.as_view(
		template_name='usuarios/form.html'
	), name='login' ), 
    path('sair/', LogoutView.as_view( 
        template_name='usuarios/formsair.html'                                     
	), name='sair')
]

