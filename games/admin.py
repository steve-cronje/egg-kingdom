from django.contrib import admin
from games.models import Game, Genre, Company, Screenshot
from django.utils.translation import gettext_lazy as _
# Register your models here.


class GameAdmin(admin.ModelAdmin):

    class SimpleDescriptionFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
        title = _('description empty')

        # Parameter for the filter that will be used in the URL query.
        parameter_name = 'my_description'

        def lookups(self, request, model_admin):
            """
            Returns a list of tuples. The first element in each
            tuple is the coded value for the option that will
            appear in the URL query. The second element is the
            human-readable name for the option that will appear
            in the right sidebar.
            """
            return (
                ('empty', _('My description is empty')),
                ('not empty', _('My description is not empty')),
            )

        def queryset(self, request, queryset):
            """
            Returns the filtered queryset based on the value
            provided in the query string and retrievable via
            `self.value()`.
            """
            # Compare the requested value (either '80s' or '90s')
            # to decide how to filter the queryset.
            if self.value() == 'empty':
                return queryset.filter(
                    my_description__lt=5
                )
            if self.value() == 'not empty':
                return queryset.filter(
                    my_description__gte=5
                )


    model = Game
    list_display = ['name', 'release_date', 'favourite']
    list_filter = ['favourite', SimpleDescriptionFilter]



class GenreAdmin(admin.ModelAdmin):

    model = Genre

class CompanyAdmin(admin.ModelAdmin):

    model = Company

class ScreenshotAdmin(admin.ModelAdmin):

    model = Screenshot


admin.site.register(Game, GameAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Screenshot, ScreenshotAdmin)


