# Create a Django Rest Framework API


API = Application Programming Interface

- [ ] 1 Install python 3.10 from https://www.python.org/downloads/release/python-3100/
- [ ] 2 Open a terminal and type `pip install django`
- [ ] 3 Inside the main project, create a folder named homeworks/homework1
  - [ ] 4 Open the IDE terminal and type `cd homeworks/homework1` and then  `django-admin startproject users`
- [ ] 5 Use the IDE to open the side project (File -> Open -> select `homeworks/homework1`)
- [ ] 6 SETTING UP THE PROJECT - Inside the new project we'll add a venv (virtual environment), a .gitignore,
      install `djangorestframework` and add a requirements.txt file
  1. Use `Ctrl+Shift+A` to look up `Switch Python Interpreter`, and create a new environment
  2. Look up on the internet `Python Django gitignore file` and copy the contents inside a new .gitignore file inside the project
  3. Install Django REST Framework (`pip install djangorestframework`)
  4. Run `pip freeze > requirements.txt`. What do you find inside the file created?
  5. EXTRA - you may need to restart the terminal after creating the Python Interpreter
  6. create the project by using django-`admin startproject users`
- [ ] 7 Add a django app to the project(`python manage.py startapp users_app`), and add it to the INSTALLED_APPS
- [ ] 8 Inside the new apps add a views.py file 
- [ ] 9 Connect the views to the project url `/users`
  - 1 inside users_app/urls create the urlpatterns file
  - 2 inside users/urls add `path('users/', include('users_app.urls'))` to the urlpattern list
- [ ] 10 start using the tutorial