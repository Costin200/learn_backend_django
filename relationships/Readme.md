# 

After this last lesson, we're going to build the main project.

## How we created this file?

1. Started a new project `django-admin startproject relationships`
2. Manually copied settings from previous lessons
3. Manually copied the environment file `.env`
4. Started the app we build `python manage.py startapp shop`
5. Added URLConf settings to `relationships/urls.py`
6. Added URLConf for shop (`shop/urls.py`):
    ```
    urlpatterns = [
        path('product', views.ProductList.as_view()),
        path('product/<int:pk>', views.ProductDetail.as_view()),
        path('orderline', views.OrderLineList.as_view()),
        path('orderline/<int:pk>', views.OrderLineDetail.as_view()),
        path('order', views.OrderList.as_view()),
        path('order/<int:pk>', views.OrderDetail.as_view()),
    ]
    ```

- [ ] 7  build models using the next relationships:
  - [ ] a. product and orderline represent a one-to-many relationship
  - [ ] b. orderline and order represent a one-to-many relationship
- [ ] 8  implement the views mentioned/used in urls.py, according to previous lessons
- [ ] 9  add test data :)
