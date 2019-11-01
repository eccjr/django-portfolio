from django.contrib import admin

from .models import Produto
from image_cropping import ImageCroppingMixin

# Definição de classes para a costumização dos forms do painel admin
# para adicionar e editar um Produto
class ProdutoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # Define quais os campos serão mostrados na lista de Produtos
    list_display = ['id', 'nome','detalhes_da_pagina_inicial', 'mostrar_na_pagina_inicial', 'video_em_gravacao']

    # Define o agrupamento e exibição dos campos no form
    fieldsets = (
        ('Detalhes do produto', {
            'fields': ('nome', 'detalhes_da_pagina_inicial'),
        }),
        ('Imagem da página inicial', {
            'fields': ('imagem_da_pagina_inicial', 'cropped'),
        }),
        ('Opções sobre a exibição na página inicial', {
            'fields': ('mostrar_na_pagina_inicial', 'video_em_gravacao',),
        }),
        ('Opções da página do produto', {
            'fields': ('detalhes', 'preco', 'link_video_demo', 'link_botao_de_compra',),
        }),
    )

# Registra o model 'Produto' conforme a customização
admin.site.register(Produto, ProdutoAdmin)