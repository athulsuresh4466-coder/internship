from django.urls import path
from.import views

urlpatterns=[
    path('page1/',views.page1,name='page1'),
]

urlpatterns=[
    path('page2/',views.page2,name='page2'),
]

urlpatterns=[
    path('page3/',views.page3,name='page3'),
]