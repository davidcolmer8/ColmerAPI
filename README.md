# ColmerAPI

# flask_api_project

<h2>creating a new repo</h2><br/>
echo "#PROJECT_NAME" >> README.md<br/>
git init<br/>
git add README.md<br/>
git commit -m "first commit"<br/>
git remote add origin https://github.com/username/PROJECT_NAME.git<br/>
git push -u origin master<br/>

<b>…or push an existing repository from the command line</b><br/>
git remote add origin https://github.com/username/PROJECT_NAME.git<br/>
git push -u origin master

Setup 
    install pip / python / flask / click 
    have an ide set up VS Code
    creating / set up a virtial env https://click.palletsprojects.com/en/7.x/quickstart/
    http://www.desmondrivet.com/blog/technical/modular-flask.html  it is all about understanding the strucuture

Exercise 1
    Create a basic flask application that returns a UUID as a JSON object
    Run the app from the command line

Exercise 2   
    next add a parameter to your api and make it a post action 'change the verb'
    e.g. /uuid/XXXX where XXXX is anything that you try to ask for in api and you capture what XXXX is and log it.

Exercise 3
    Run the app from Click --hint
            sudo -H pip install --editable .
            entry point command

Exercise 4
    print the routes 
        had to add export FLASK_APP=simpleApp.app:startApp

Exercise 5
    add pytest

Exercise 6
    create a nice structure for python

Exercise 7
    issues with calling the application from a different folder 
    implement swagger






