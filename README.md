# weather-api
weather api example using https://www.weatherapi.com/


#Instructions to follow
1. The operating System used for this project is Ubuntu 18.04 ( But if you can run Django on Windows, the projects will work just fine).
2. The application was build using Django==2.2.17  on Python 3.6.9. Please use the requirements.txt file for the required dependencies. There are most probably more than required. 
3. The project runs the built-in db.sqlite3  that comes with Django
4. Steps to run the project:

  - Create virtual environment and install all the dependencies in the requirements.txt file.
  - Copy the content of the repository into your a project folder (Name it how you like).
  - In the following file:  your_project_folder/weather_api/settings.py , change the ALLOWED_HOSTS = ['192.168.5.5', 'localhost'] to your own domain.
  - cd into your_project_folder/ (Make sure you can see a file called manage.py) and run the following commands:
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver <YOUR_SERVER_IP>:8000
  - Check your teminal to ensure that you see something like below:
      Performing system checks...

      System check identified no issues (0 silenced).
      December 03, 2020 - 13:23:57
      Django version 2.2.17, using settings 'weather_api.settings'
      Starting development server at http://192.168.5.5:8000/
      Quit the server with CONTROL-C.
    
    VOILLLLLLA, C'EST MAGNIFIQUE!   You are ready to test. Open up your browswer and try out some location and period (In this project, the period is in days... The API allows up     7 days forcasting.
    
    LIKASI is my  birth down, it is located somewhere in the South of the Democratic Republic of Congo (DRC)
  


