

from django.conf.urls import url,include
from django.contrib import admin
from apps.mascota.views import home
# funciones necesarias para loguearse,desloguearse y para enviar correos a los usuario
from django.contrib.auth.views import login,logout_then_login,password_reset,password_reset_done,password_reset_confirm,password_reset_complete
# decorador para restringir las URLs a los usuarios no logueados
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # incluimos las URLs de las apps a las URL globales del proyecto
    url(r'^usuario/',include('apps.usuario.urls')),
    url(r'^mascota/',include('apps.mascota.urls')),
    url(r'^adopcion/',include('apps.adopcion.urls')),
    # vistas basadas en funcion para loguearse y desloguearse
    url(r'^$', login, {'template_name': 'index.html'}, name='login'),
    url(r'^accounts/login/', login, {'template_name': 'index.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    # vista para el  home del sistema
    url(r'^home/$', login_required(home), name='home'),

    url(r'^admin/', admin.site.urls),

#   vistas basadas en funcion que nos permite enviar los correos a los usuarios
    url(r'^reset/password_reset/$',password_reset,{'template_name':'reset_pass/reset_password_form.html'
        ,'email_template_name':'reset_pass/reset_password_email.html'},name='password_reset'),

    url(r'^reset/password_reset_done/$',password_reset_done,{'template_name':'reset_pass/reset_password_done.html'},name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',password_reset_confirm,{'template_name':'reset_pass/reset_password_confirm.html'},name='password_reset_confirm'),

    url(r'^reset/done$',password_reset_complete,{'template_name':'reset_pass/reset_password_complete.html'},name='password_reset_complete'),



]

