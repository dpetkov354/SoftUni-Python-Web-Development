from django.urls import path, include

from game_play_app.web.views import home_page,\
    create_game, dashboard, details_game, edit_game, delete_game, \
    details_profile, create_profile, delete_profile, edit_profile

urlpatterns = (
    path("", home_page, name="home page"),
    path("games/", include([
        path("create/", create_game, name='create game'),
        path("dashboard/", dashboard, name='dashboard'),
        path("details/<int:pk>/", details_game, name="details game"),
        path("edit/<int:pk>/", edit_game, name="edit game"),
        path("delete/<int:pk>/", delete_game, name="delete game"),
    ])),
    path("profile/", include([
        path("create/", create_profile, name='create profile'),
        path("details/", details_profile, name='details profile'),
        path("delete/", delete_profile, name='delete profile'),
        path("edit/", edit_profile, name='edit profile'),
    ]))
)
