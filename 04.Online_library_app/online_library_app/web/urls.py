from django.urls import path
from online_library_app.web.views import home_page, \
    book_add, book_edit, book_details, book_delete, \
    profile_edit, profile_delete, profile_page

urlpatterns = (
    path("", home_page, name="home page"),

    path("book_add/", book_add, name="book add"),
    path("book_delete/<int:pk>/", book_delete, name="book delete"),
    path("book_edit/<int:pk>/", book_edit, name="book edit"),
    path("book_details/<int:pk>/", book_details, name="book details"),

    path("profile_page/", profile_page, name="profile page"),
    path("profile_edit/", profile_edit, name="profile edit"),
    path("profile_delete/", profile_delete, name="profile delete"),
)