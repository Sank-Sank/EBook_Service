from django.urls import path
from . import views as v

urlpatterns = [
    path('search/', v.search),
    path('chapters/', v.getChapters),
    path('chaptercontent/', v.getChapterContent),
    path('type', v.getType),
    path('mall', v.bookMall),

]

