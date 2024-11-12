from django.contrib import admin
from django.contrib.auth import get_user_model

from .forms import UsuarioAdminChangeForm, UsuarioAdminCreationForm

Usuario = get_user_model()

#admin.site.register(Usuario, UsuarioAdmin)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['email']
    form = UsuarioAdminChangeForm
    add_form = UsuarioAdminCreationForm



