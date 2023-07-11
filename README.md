# TZ_for_work_without_ROS
 Technical task for a server with docker
# How to run the program?

 First of all, create the VENA folder.
 
 Install all dependencies from requirements.txt.
 
 Then sequentially type "cd node_web_server" "python manage.py runserver".
 
 Then follow the link "http://127.0.0.1:8000/api/log"

Next, a web server is implemented from which you can send data from the endpoint, json of the form {"data":"random data"} is accepted. After that, logging into a file with a filter by error occurs, and the INFO type is written to the file, but if there is an error, it will change to ERROR. Used Docker.
 I have to admit that due to inexperience and some problems, I could not implement ROS. But I'm always ready to learn something new.
