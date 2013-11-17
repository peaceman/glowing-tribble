from django.contrib import admin
from edmmusic.models import MusicBank, MusicGenre, MusicProgram, MusicPlugin

admin.site.register(MusicBank)
admin.site.register(MusicGenre)
admin.site.register(MusicProgram)
admin.site.register(MusicPlugin)
