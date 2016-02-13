from django.conf.urls import patterns, url
from budget.categories.views import (
        category_list,
        category_add,
        category_edit,
        category_delete
)

urlpatterns = [
    url(r'^$', category_list, name='budget_category_list'),
    url(r'^add/$', category_add, name='budget_category_add'),
    url(r'^edit/(?P<slug>[\w_-]+)/$', category_edit, name='budget_category_edit'),
    url(r'^delete/(?P<slug>[\w_-]+)/$', category_delete, name='budget_category_delete'),
]
