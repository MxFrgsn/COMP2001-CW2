
# COMP2001 CW2 - Trail App Micro-Service

## Project Description:
The **Trail App** is a well-being trail application designed to enhance outdoor experiences and promote exploration. This application aims to provide users with trail management capabilities, allowing them to create, view, and interact with trails, ensuring a seamless experience for outdoor enthusiasts.

## Installation Instructions: 
Run theses commands:
- docker pull mxfrgsn/comp2001_cw2
- docker run -p 8000:8000 mxfrgsn/comp2001_cw2

## Usage Instructions:

The application provides RESTful API endpoints for trail management.
You can interact with these endpoints via tools such as Postman, cURL, or Swagger UI.

Endpoints:

- **GET /trails**  
  **Description**: Retrieve a list of all trails.  
  **Method**: `GET`  

- **POST /trails**  
  **Description**: Create a new trail.  
  **Method**: `POST`  

- **GET /trails/{trail_id}**  
  **Description**: View a specific trail by ID.  
  **Method**: `GET`  

- **PUT /trails/{trail_id}**  
  **Description**: Update an existing trail.  
  **Method**: `PATCH`  

- **DELETE /trails/{trail_id}**  
  **Description**: Delete a trail. 
  **Method**: `DELETE`  

### Users Endpoints

- **GET /users**  
  **Description**: Retrieve a list of all users.  
  **Method**: `GET`  

- **POST /users**  
  **Description**: Create a new user.  
  **Method**: `POST`  

- **GET /users/{user_id}**  
  **Description**: View a specific user by ID.  
  **Method**: `GET`  

- **DELETE /users/{user_id}**  
  **Description**: Delete a user by ID.  
  **Method**: `DELETE`  

- **PATCH /users/{user_id}**  
  **Description**: Update a user by ID.  
  **Method**: `PATCH`  

- **POST /authenicate**  
  **Description**: Logins the 3 users using univeristy auth API
  **Method**: `POST`  

### Trail Attractions Endpoints

- **GET /trail_attraction**  
  **Description**: Retrieve a list of all trail attractions.  
  **Method**: `GET`  

- **POST /trail_attraction**  
  **Description**: Create a new trail attraction.  
  **Method**: `POST`  

- **DELETE /trail_attraction/{trail_id}/{attraction_id}**  
  **Description**: Delete one attraction tied to a trail.  
  **Method**: `DELETE`  


- **DELETE /trail_attraction/{trail_id}/all**  
  **Description**: Delete all attractions tied to a trail.  
  **Method**: `DELETE`  

### Attractions Endpoints

- **GET /attractions**  
  **Description**: Retrieve a list of all attractions.  
  **Method**: `GET`  

- **POST /attractions**  
  **Description**: Create a new attraction.  
  **Method**: `POST`  

- **GET /attractions/{attraction_id}**  
  **Description**: View a specific attraction by ID.  
  **Method**: `GET`   

- **PATCH /attractions/{attraction_id}**  
  **Description**: Update an attraction by ID.  
  **Method**: `PATCH`  


- **DELETE /attractions/{attraction_id}**  
  **Description**: Delete an attraction by ID.  
  **Method**: `DELETE`  

### Location Points Endpoints

- **GET /location_point**  
  **Description**: Retrieve a list of all location points.  
  **Method**: `GET`  

- **POST /location_point**  
  **Description**: Create a new location point.  
  **Method**: `POST`  

- **GET /location_point/{location_point_id}**  
  **Description**: View a specific location point by ID.  
  **Method**: `GET`  


- **PATCH /location_point/{location_point_id}**  
  **Description**: Update a location point by ID.  
  **Method**: `PATCH`  

- **DELETE /location_point/{location_point_id}**  
  **Description**: Delete a location point by ID.  
  **Method**: `DELETE`  

## Swagger Documentation:

You can access the Swagger UI and use the API endpoints yourself at:
http://localhost:8000/api/ui

This provides a clear interface for API documentation, listing all available endpoints and request/response formats.

## User Authentication:

Use the following credentials for accessing the API:
- Grace Hopper: grace@plymouth.ac.uk, password: ISAD123!
- Tim Berners-Lee: tim@plymouth.ac.uk, password: COMP2001!
- Ada Lovelace: ada@plymouth.ac.uk, password: insecurePassword

Contact Information: 
- https://github.com/MxFrgsn
- 16max.ferguson@students.plymouth.ac.uk