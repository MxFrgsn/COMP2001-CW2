
# COMP2001 CW2 - Trail App - Trail Microservice

## Project Description:
The **Trail Microservice** is a well-being-focused outdoor trail application designed to enhance user exploration and outdoor experiences. The service allows users to manage trails by creating, viewing, and interacting with all trail information, ensuring a seamless and efficient experience for outdoor enthusiasts.

This GitHub repository contains the backend implementation of the service, developed using Python and documented with Swagger using Mircosoft SQL for data management.

## Installation Instructions: 

Connect to the Univerisity of Plymouth WIFI (UOP-Connect/Eduroam/UOP-Visitor) or make a digital connection to the University through the FortiClient VPN.

### **Docker Installation**:
1. Install Docker:
   - [Download Docker Desktop](https://www.docker.com/products/docker-desktop/) and follow the installation instructions.
2. Start Docker and ensure it’s running.
3. Run the following commands:
   ```bash
   docker pull mxfrgsn/comp2001_cw2
   docker run -p 8000:8000 mxfrgsn/comp2001_cw2
4. Access the API. 
    - Open your web browser and navigate to: [localhost:8000](localhost:8000)
    - Or use Postman, Curl, or similar tools to interact with the endpoints.

### **Alternative Python Installation**:
1. Clone/download the GitHub folder containing the application.
2. Install Python:
   - [Download Python](https://www.python.org/downloads/) and follow the installation instructions.
3. Install ODBC Driver:
   - [Download ODBC Driver 17](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16) and follow the installation instructions.
4. Set up a Python environment using your preferred IDE (e.g., Python IDE, Visual Studio Code).
5. Navigate to the folder where the `app.py` file is located.
6. Install required packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
7. Run `app.py` using your Python environment.
    ```bash
    python -m app
8. Access the API. 
    - Open your web browser and navigate to: [localhost:8000](localhost:8000)
    - Or use Postman, Curl, or similar tools to interact with the endpoints.

## Swagger Documentation:

You can access the Swagger UI and use the API endpoints yourself at:
http://localhost:8000/api/ui

## Usage Instructions:

The application provides RESTful API endpoints for trail management.
You can interact with these endpoints via tools such as Postman, cURL, or Swagger UI.

Endpoints:

- **Path**: /trails  
  **Description**: Retrieve a list of all trails.  
  **Method**: `GET`  

- **Path**: /trails  
  **Description**: Create a new trail.  
  **Method**: `POST`  

- **Path**: /trails/{trail_id}  
  **Description**: View a specific trail by ID.  
  **Method**: `GET`  

- **Path**: /trails/{trail_id}  
  **Description**: Update an existing trail.  
  **Method**: `PATCH`  

- **Path**: /trails/{trail_id}  
  **Description**: Delete a trail.  
  **Method**: `DELETE`  

### Users Endpoints

- **Path**: /users  
  **Description**: Retrieve a list of all users.  
  **Method**: `GET`  

- **Path**: /users  
  **Description**: Create a new user.  
  **Method**: `POST`  

- **Path**: /users/{user_id}  
  **Description**: View a specific user by ID.  
  **Method**: `GET`  

- **Path**: /users/{user_id}  
  **Description**: Delete a user by ID.  
  **Method**: `DELETE`  

- **Path**: /users/{user_id}  
  **Description**: Update a user by ID.  
  **Method**: `PATCH`  

- **Path**: /authenicate  
  **Description**: Logins the 3 users using univeristy auth API  
  **Method**: `POST`   

### Trail Attractions Endpoints

- **Path**: /trail_attraction  
  **Description**: Retrieve a list of all trail attractions.  
  **Method**: `GET`  

- **Path**: /trail_attraction  
  **Description**: Create a new trail attraction.  
  **Method**: `POST`  

- **Path**: /trail_attraction/{trail_id}/{attraction_id}  
  **Description**: Delete one attraction tied to a trail.  
  **Method**: `DELETE`  

- **Path**: /trail_attraction/{trail_id}/all  
  **Description**: Delete all attractions tied to a trail.  
  **Method**: `DELETE`  

### Attractions Endpoints

- **Path**: /attractions  
  **Description**: Retrieve a list of all attractions.  
  **Method**: `GET`  

- **Path**: /attractions  
  **Description**: Create a new attraction.  
  **Method**: `POST`  

- **Path**: /attractions/{attraction_id}  
  **Description**: View a specific attraction by ID.  
  **Method**: `GET`  

- **Path**: /attractions/{attraction_id}  
  **Description**: Update an attraction by ID.  
  **Method**: `PATCH`  

- **Path**: /attractions/{attraction_id}  
  **Description**: Delete an attraction by ID.  
  **Method**: `DELETE`  

### Location Points Endpoints

- **Path**: /location_point  
  **Description**: Retrieve a list of all location points.  
  **Method**: `GET`  

- **Path**: /location_point  
  **Description**: Create a new location point.  
  **Method**: `POST`  

- **Path**: /location_point/{location_point_id}  
  **Description**: View a specific location point by ID.  
  **Method**: `GET`  

- **Path**: /location_point/{location_point_id}  
  **Description**: Update a location point by ID.  
  **Method**: `PATCH`  

- **Path**: /location_point/{location_point_id}  
  **Description**: Delete a location point by ID.  
  **Method**: `DELETE`  

### Trail Location Points Endpoints
- **Path**: /trail_locationpt/{trail_id}/{location_point_id}  
  **Description**: Delete one location point tied to a trail.  
  **Method**: `DELETE`  

- **Path**: /trail_locationpt/{trail_id}/all  
  **Description**: Delete all location points tied to a trail.  
  **Method**: `DELETE`  

- **Path**: /trail_locationpt/{id}  
  **Description**: Get all location points or trails tied to a trail or location point.  
  **Method**: `GET`  

- **Path**: /trail_locationpt  
  **Description**: Get all location points that are tied to a trail.  
  **Method**: `GET`  

- **Path**: /trail_locationpt/{trail_id}/{location_point_id}  
  **Description**: Update a trail location point order number.  
  **Method**: `PATCH`


## User Authentication:

Use the following credentials to test the user authentication API:
- Grace Hopper: 
  - email: grace@plymouth.ac.uk, 
  - password: ISAD123!
- Tim Berners-Lee: 
  - tim@plymouth.ac.uk, 
  - password: COMP2001!
- Ada Lovelace: 
  - email: ada@plymouth.ac.uk,
  - password: insecurePassword

Contact Information: 
- https://github.com/MxFrgsn
- 16max.ferguson@students.plymouth.ac.uk
