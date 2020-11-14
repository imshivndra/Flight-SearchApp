# Flight Search App
This is a flight search app that finds best flights which will take minimum time to reach from departure city to arrival city
### Tech Stack
* **Frontend**-ReactJs,HTML,CSS
* **Backend**-Python,Django
* **Database**-PostgreSQL

# Setting Up Project Locally 
* clone the code from [Flight-SearchApp](https://github.com/imshivndra/Flight-SearchApp)
**Frontend**
* Go to client directory and run **npm install**
* Run **npm start**
* Now you can see your frontend live at localhost:3000 
**Backend**
* Go to server directory and run pip3 install to install dependencies
* configure **Database** ,we are using postgresql. make sure your system has postgresql installed 
 **Connecting database to our Django project**
 * create a database in postgre using PgAdmin
 * Go to settings.py folder and make sure credentials of database are correct
 * **Migration**
 * Run **python3 manage.py run migration** to create schema in your DB
 * Make your backend server live on localhost Run **python3 manage.py runserver**
 
 ### Now your Frontend and Backend is is live
 You can insert and update Flight data in your database using create-flight  and update-flight API
  ## Your Search result will look like : 
  ![Front end view](/Flight-SearchApp/FlightAppSS.png)
  
 



