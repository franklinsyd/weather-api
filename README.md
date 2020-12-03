# weather-api
weather api example using https://www.weatherapi.com/


#Instructions to follow
1. The operating System used for this project is Ubuntu 18.04 ( But if you can run Django on Windows, the projects will work just fine).
2. The application was build using Django==2.2.17  on Python 3.6.9. Please use the requirements.txt file for the required dependencies. There are most probably more than required. 
3. The project runs on the built-in db.sqlite3  that comes with Django
4. Steps to run the project:
  
  - Copy the content of the repository into your a project folder (Name it how you like).
  - All the magi happens in the following files:
  
    - your_project_folder/clients/weather_api_calls.py
    - your_project_folder/core/views.py
    - your_project_folder/core/tests.py
    
  - In the following file:  your_project_folder/weather_api/settings.py , change the ALLOWED_HOSTS = ['192.168.5.5', 'localhost'] to your own domain.
  - cd into your_project_folder/ (Make sure you can see a file called manage.py) and run the following commands:
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py runserver <YOUR_SERVER_IP>:8000
  - Check your teminal to ensure that you see something like below:
      
      Performing system checks...
      System check identified no issues (0 silenced).
      December 18, 1999 - 13:23:57
      Django version 2.2.17, using settings 'weather_api.settings'
      Starting development server at http://192.168.5.5:8000/
      Quit the server with CONTROL-C.
    
    VOILLLLLLA, C'EST MAGNIFIQUE!   You are ready to test. Open up your browswer and try out some locations and periods (In this project, the period is in days... The API allows     up to 7 days forcasting)
    
    The general API call is done as follow:  http://<YOUR_SERVER_IP>:8000/core/forecast/<Location_name>/<period>/ , you receive back the following for each day:
    maximum temperature, the minimum temperature, the average temperature and humidity.
    
    LIKASI is my  birth down, it is located somewhere in the South of the Democratic Republic of Congo (DRC) - It rains all the time ...Hahaha, try it out:
    
    http://<YOUR_SERVER_IP>:8000/core/forecast/Likasi/3/   (Location: Likasi,  3 days forecast)
    
    Try another town:
    http://<YOUR_SERVER_IP>:8000/core/forecast/Pretoria/5/   (Location: Likasi,  5 days forecast)
    
    Try another town:
    http://<YOUR_SERVER_IP>:8000/core/forecast/Paris/4/   (Location: Likasi,  4 days forecast)  - It should be really cold.
  


