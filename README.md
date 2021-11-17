# Introduction
This is my chatbot for Nott-A-Code competition. I made it by using Python,HTML,CSS,JavaScript and Chatterbot (a python library) and Django(Python web framework).Here is the picture of final result:

![ww](https://user-images.githubusercontent.com/89083229/141963097-a0c37e24-30ec-4579-b66d-52f6124bbf40.PNG)


# How to run 
## Step 1:
Download and install python from this website<br>
https://www.python.org/downloads/<br>
I am using Python 3.9.7. Make sure to check the add python to path option when you install python.
![254001694_319886339637381_5738224357551564660_n](https://user-images.githubusercontent.com/89083229/142131890-cd73d164-ac6c-4445-a925-ee895d2cae68.jpg)
## Step 2: Clone the project:
Click on the "Code" button and select "Download Zip"
## Step 3: Install libraries
You can use command prompt on windows or terminal on Mac or any IDE(ex: Visual Studio Code)
Make sure you are in the path of the project folder and type : <br>
pip install -r requirements.txt<br>
It will install all the files you need.
## Step 4: Fix 2 setting problems (Important)
### 4.1 Set Django to path(if you haven't done it yet)
Go to this link change [UserName] with your username <br>
C:\Users\[UserName]\AppData\Roaming\Python\Python39\Scripts  <br>
Open Edit Environment Variables for your account <br>
![image](https://user-images.githubusercontent.com/89083229/142130964-51cef241-69b6-407e-84e3-4d7e516e2a77.png) <br>
Choose the path and click edit and then add the C:\Users\[UserName]\AppData\Roaming\Python\Python39\Scripts <br>
Click OK 2 times => And then you finished.
### 4.2 :  Module 'time' has no attribute 'clock'
If you are using python 3.x you will have this problem.Because they changed the name <br>
Here is the picture of the problem.
![253989589_315021017128754_7650931696018456001_n](https://user-images.githubusercontent.com/89083229/142133290-1c116630-6c77-4503-87d2-a4bfd1282449.jpg)
Now how to fix this just go to that file(compat.py) line 264 and change from: <br>
time_func = time.clock() to time_func = time.time()
Here is an answer from StackOverflow and you can follow it too: <br>
https://stackoverflow.com/questions/58569361/attributeerror-module-time-has-no-attribute-clock-in-python-3-8
![image](https://user-images.githubusercontent.com/89083229/142133607-765082f9-9fbb-422a-a736-21258659943e.png)
Now we are ready to run the project 

## Step 5: Run the project
Type in your terminal:<br> python manage.py runserver <br>
It will load for a while and said: <br>
Starting development server at http://127.0.0.1:8000/ <br>
Go to that link and it will display a page like this<br>
![image](https://user-images.githubusercontent.com/89083229/141965894-5f58d8ce-5f6d-4f3b-8d95-43817a1e309e.png)
Now you change the link to: http://127.0.0.1:8000/bot/ <br>
And it will get into my chat bot:

![ww](https://user-images.githubusercontent.com/89083229/141966330-dfb7f1f2-11b6-4e1b-ac3b-67e20943d3bb.PNG)






