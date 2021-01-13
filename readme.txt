Project Description:

env: crms_env

1. It has a simple CRUD functionality of a Student
2. It database is hosted remotely in the cloud. (remotemysql.com)
3. Install heroku in the ubuntu. & login to the heroku account through the terminal by executing "heroku login" command.
4. Install gunicorn in the system by executing "pip install gunicorn" command.
5. Align the requirements.txt file as needed.   (Not completed)
6. Create a .git file using "git init" in the root directory.
7. Copy the raw text of .gitignore from "https://github.com/github/gitignore/blob/master/Python.gitignore".
8. Run the command "git add -A" to add all of the changes. We can check using "git status" command.
9. To commit all of these changes execute the command 'git commit -m "Initial Commit"'
10. Create a Heroku app using the command 'heroku create "mySampleApp"'. It will create a domain in the terminal. Copy and paste that on a browser to run the site/execute the command "heroku open"
11. Setting a buildpack on an application: use the command "heroku buildpacks:set heroku/php"
11. Add a Procfile in the project root directory to define process types and explicitly declare what command should be executed to start your app. Use the command "touch Procfile"
12. Open the Procfile and add the line below. "web: gunicorn YourAppProject.wsgi --log-file -". In my case it is "djangoConMySQL"
13. Run the following commands: 
    i) pip install dj-database-url
    ii) pip install whitenoise
    iii) pip install gunicorn
14. Make sure to have ("Procfile", "readme.txt", "requirements.txt", "runtime.txt") these files inside the root directory of the project, where the "db.sqlite3", "manage.py" files are located.
15. Follow the article written in the following URL:
    https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4
