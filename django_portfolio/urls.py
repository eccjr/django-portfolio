"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importa o método include
from django.urls import include

# Com o 'include' é possível redirecionar uma determinada URL para um 'urls.py' de um app específico.
# No caso, as URLs 'website.com' e 'website.com/produto' estão sendo redirecionadas para o 'urls.py'
# dos apps 'website' e 'produtos'.
urlpatterns = [
    path('', include('website.urls')),
    path('produto/', include('produtos.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# A última linha representa uma configuração do Django que permite que os arquivos que o administrador
# do site fez upload e estão salvos na pasta '/media/' sejam acessados pelo navegador, permitindo assim
# que eles possam ser exibidos no site.