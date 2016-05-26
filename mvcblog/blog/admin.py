from django.contrib import admin                                                #imports admin site

from blog.models import Post                                                    #from<app(folder)>.<pythonfile> import <class>

class PostModelAdmin(admin.ModelAdmin):                                         #see docs about ModelAdmin
    list_display  = ["title", "updated", "timestamp"]                           #what admin sees
    list_display_links = ["updated"]                                            #links
    list_filter = ["updated", "timestamp"]                                      #date filter (on the right in page)
    list_editable = ["title"]                                                   #can modify the title
    search_field = ["title", "text"]                                            #search function for posts
    class Meta:                                                                 #python wierdness
        model = Post                                                            #connecting Post model inside admin site

admin.site.register(Post, PostModelAdmin)                                       #register models to see in admin site
