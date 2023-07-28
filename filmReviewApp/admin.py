from django.contrib import admin

# Register your models here.
from filmReviewApp.models import Film, User, Review
admin.site.register(Film)
admin.site.register(User)
admin.site.register(Review)