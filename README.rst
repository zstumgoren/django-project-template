Overview
========

Base project template for use with Django >= 1.4's 
`custom template feature
<https://docs.djangoproject.com/en/dev/releases/1.4-alpha-1/#custom-project-and-app-templates>`_.

Much of the layout and default settings cribbed from Andrew McCloud's `django-project-skel <https://github.com/amccloud/django-project-skel>`_.

Usage
------
Create a virtual environment

    mkvirtualenv --no-site-packages {{ project_name }}

Activate virtual environment and install django
 
    pip install django

Create project template

    django-admin.py startproject --template=django-project-template {{ project_name }}

Add {{ project_name }} and {{ project_name }}/apps to virtualenv's PYTHONPATH

Configure settings for dev and prod environments
