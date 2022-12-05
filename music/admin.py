from django.contrib import admin
from music.models import Artist, Album, Track, Playlist
from django.utils.translation import gettext_lazy as _

class ArtistAdmin(admin.ModelAdmin):

    model = Artist
    list_display = ['id', 'name', 'artist_type', 'spotify_url']
    search_fields = ['name']

class AlbumAdmin(admin.ModelAdmin):

    model = Album
    list_display = ['id', 'name', 'album_type', 'release_date', 'spotify_url']
    search_fields = ['name']

class TrackAdmin(admin.ModelAdmin):

    class SimpleDurationFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
        title = _('duration')

        # Parameter for the filter that will be used in the URL query.
        parameter_name = 'duration'

        def lookups(self, request, model_admin):

            return (
                ('short', _('Tracks under 3 minutes long')),
                ('avg', _('Tracks over 3 minutes long')),
                ('long', _('Tracks over 4 minutes long'))
            )

        def queryset(self, request, queryset):

            if self.value() == 'short':
                return queryset.filter(
                    duration__lt=180000
                )
            if self.value() == 'avg':
                return queryset.filter(
                    duration__gte=180000,
                    duration__lt=240000
                )
            if self.value() == 'long':
                return queryset.filter(
                    duration__gte=240000
                )

    model = Track
    list_display = ['id', 'name', 'album', 'preview_url', 'explicit_content', 'get_duration', 'spotify_url', 'get_playlist']
    list_filter = ['explicit_content', SimpleDurationFilter]
    search_fields = ['name']

    def get_playlist(self, obj):
        return [playlist.name for playlist in obj.playlist.all()]

class PlaylistAdmin(admin.ModelAdmin):

    model = Playlist
    list_display = ['id', 'name', 'spotify_url', 'image_url']
    search_fields = ['name']

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Playlist, PlaylistAdmin)