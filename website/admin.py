from django.contrib import admin
from .models import Depoimento, Foto
from image_cropping import ImageCroppingMixin

# Definição de classes para a costumização dos forms do painel admin
# para adicionar e editar um Depoimento, uma Foto ou um Seminário
class DepoimentoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # Define quais os campos que serão mostrados na lista de Depoimentos
    list_display = ['id', 'nome', 'profissao']

class FotoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # Define quais os campos que serão mostrados na lista de Fotos
    list_display = ['id', 'alt']


# Define o nome do painel admin
admin.site.site_title = 'Painel administrativo do site em Django'

# Registra os models 'Depoimento' e 'Foto' conforme as customizações
admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.register(Foto, FotoAdmin)
