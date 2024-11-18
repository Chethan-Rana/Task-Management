#Task Management App

Definition: Manages the users and the tasks assigned to individual users. Track task progress.

Implementation:

Created with database named task_db
Has two different tables users and tasks.
Has CRUD operations implemented for both users and tasks
How to run:

copy the code to your local repo
create a 'virtual environment'
navigate to the app and run poetry install -r requirements.txt
once the installation is done, run poetry run python main.py which will host the app at port 8000
naviagate to the url http://localhost:8000/docs, you will be able to see swagger docs where you can perform operations.
Note: The changes to run the app in docker is still under development.
