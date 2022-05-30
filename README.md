# Blog Project
This is a simple CRUD blog project made with Django, Django templates, HTML, CSS, Bootstrap, Javascript and sqlite3.

## Packages:
- [Django](https://www.djangoproject.com/)
- [Misaka](https://misaka.readthedocs.io/en/latest/)
## Setup
1. Clone this repository
2. Just install django package:

Django:
```bash
pip install Django
```
## Tasks
The following image shows the homepage of the website:
![image](https://user-images.githubusercontent.com/105637508/170981893-d06436d6-81b8-4b94-b74b-cbfa6763692a.png)
The following tasks can be done in this blog:
1. Sign in: The admin can sign in by entering his/her user name and password. To be an admin, you must be a superuser:
```bash
python manage.py createsuperuser
```
2. Posts: After signing in you can create or delete posts. A post contains a title and a text body. A publication date is considered for each post.
3. Comments: For each posts, other users can write comments for that post. Comments are published after the confirmation of the admin. Also admin can delete a comment.
