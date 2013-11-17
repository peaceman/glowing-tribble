from django.contrib import admin
from edmmusic.models import MusicBanks, MusicGenre, MusicProgram, MusicPlugins

admin.site.register(MusicBanks)
admin.site.register(MusicGenre)
admin.site.register(MusicProgram)
admin.site.register(MusicPlugins)
