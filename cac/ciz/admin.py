from django.contrib import admin
from .models import Law , LegalCase , Quiz , Profile,Language# Register your models here.
admin.site.register(Law)
admin.site.register(LegalCase)
admin.site.register(Quiz)
admin.site.register(Profile)
admin.site.register(Language)