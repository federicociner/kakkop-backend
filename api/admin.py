from django.contrib import admin


from api.models import Game


class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = (
        "id",
        "creator",
        "status",
    )
    list_filter = (
        "id",
        "creator",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "creator",
                    "num_rounds",
                    "num_players",
                    "status",
                    "game_type",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "creator",
                    "num_rounds",
                    "num_players",
                    "status",
                    "game_type",
                ),
            },
        ),
    )
    search_fields = ("id",)
    ordering = ("id",)


admin.site.register(Game, GameAdmin)
