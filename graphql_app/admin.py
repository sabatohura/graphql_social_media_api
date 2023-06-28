from django.contrib import admin

from graphql_app.models import User
# Register your models here.

# admin.sites.register 

admin.site.register([
    User
])