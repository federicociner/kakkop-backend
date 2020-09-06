from django.contrib import admin

from .models.game import Game


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
                    "number_of_rounds",
                    "number_of_players",
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
                    "number_of_rounds",
                    "number_of_players",
                    "status",
                    "game_type",
                ),
            },
        ),
    )
    search_fields = ("id",)
    ordering = ("id",)


admin.site.register(Game, GameAdmin)
