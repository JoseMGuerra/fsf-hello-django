![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Django TODO app  mini-project

<details>
<summary>Installing and creating a Django project</summary>

- Django 3.2 is the LTS (Long Term Support) version of Django and is therefore preferable to use over the newest Django 4

        pip3 install 'django<4'

- To create new project

        django-admin startproject PROJ_NAME . (ie: django_todo .)

- Create an env.py file and include it into a .gitignore file

        touch env.py

- Set the default environment variables in the env.py file ie:

        import os
        os.environ.setdefault("SECRET_KEY","VALUE")

- Point the SECRET_KEY variable in the setting.py file to our default value in the env.py file

        import os
        if os.path.exists("env.py"):
                import env

        SECRET_KEY = os.environ.get("SECRET_KEY")

</details>

<details>
<summary>Create an App </summary>

- This command creates a directory called "todo" with the app files

        python3 manage.py startapp APP_NAME (ie: todo)

</details>

<details>
<summary>Create templates to render the html files</summary>

- Create a templates directory in the todo directory

        mkdir todo/templates

- Create a todo directory in the templates directory

        mkdir todo/templates/todo

- Create a todo_list.html file within the todo directory inside templates folder.

        touch todo/templates/todo/todo_list.html

</details>

---

Happy coding!
