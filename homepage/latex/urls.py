from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^question/', views.question, name='question'),
        #url(r'^$', views.latex.index, name='index'),
        #url(r'form/$', views.latex.form, name='form'),
        #url(r'list/$', views.latex.list, name='list'),
        
        #url(r'^$', views.index, name='index'),
        #url(r'createquestion/$', views.CreateQuest, name='createquestion'),
        #url(r'chaining/', include('smart_selects.urls')),

        url(r'^$', views.InsQuestionListView.as_view(), name='question_changelist'),
        url(r'add/$', views.InsQuestionCreateView.as_view(), name='question_add'),
        url(r'<int:pk>/', views.InsQuestionUpdateView.as_view(), name='question_change'),
]
