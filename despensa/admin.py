from django.contrib import admin


from .models import (
    Categoria,
    Produto,
    Despensa,
    Mercado,
    Marca,
    Item,
    ListaCompra,
    ProdutoQuantidade,
    QuantidadePadrao
)


admin.site.register(Categoria,admin.ModelAdmin)
admin.site.register(Produto, admin.ModelAdmin)
admin.site.register(Despensa, admin.ModelAdmin)
admin.site.register(Mercado, admin.ModelAdmin)
admin.site.register(Marca, admin.ModelAdmin)
admin.site.register(Item, admin.ModelAdmin)
admin.site.register(ListaCompra, admin.ModelAdmin)
admin.site.register(ProdutoQuantidade, admin.ModelAdmin)
admin.site.register(QuantidadePadrao, admin.ModelAdmin)