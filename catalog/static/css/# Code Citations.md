# Code Citations

## License: MIT
https://github.com/torresleonel/django_local_library/tree/5998a3c38bff3689a9c260ea20ebc68c3272c1e3/catalog/urls.py

```
django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/
```


## License: unknown
https://github.com/AuriferousAurora/mdn-library/tree/4f31420755778f8a3e2dc35ab9b0a04cbe171a55/catalog/urls.py

```
views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views
```


## License: unknown
https://github.com/Laxmannegi/myfirstpythonproject/tree/31b56155a160f075ffd68cde6d63c9b357a282e7/locallibrary/catalog/urls.py

```
.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='
```


## License: unknown
https://github.com/edulonde/mdn_tutorial_django_biblioteca/tree/cd4c0ef221fe109ecf4f28140837a42e377983a7/catalogo/urls.py

```
'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    #
```


## License: unknown
https://github.com/SourOrange/djLocalLibrary/tree/a3c1cd5f5aff44eb71379a4aa73d480c36c821ca/catalog/templates/catalog/author_list.html

```
extends "base_generic.html" %}
{% block content %}
  <h1>Author List</h1>
  <ul>
    {% for author in author_list %}
      <li>
        <a href="{{ author.get_absolute_url }}">{{ author }
```

