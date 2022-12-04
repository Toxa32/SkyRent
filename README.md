## SkyRent
This is the server part of the application for renting real estate abroad. The application includes functions:

 - Displaying all offers in the database
 - Filtering data by country, city and price
 - Displaying detailed information about the offer
---

Team members:
- Nara Mosesyan - CEO of the project
- Irackliy - COO
- Gleb Kushedow - Team-leader
- Angelica - Frontend developer
- Sazonov Dmitry - QA-engineer
- Aleksey Mavrin - Backend developer
 ---
The project's structure: 
 - dao - DAOs to work with different tables
 - tests - a python package with all tests described above
 - services- classes provided a business logic
 - setup - there're SQLAlchemy and Api instances in the folder
 - views - there are CBVs to work with different routes
 - container.py - there're DAO and Service classes' instances
 - configs.py - configuration classes with different settings and manager  automatically selecting the setting
 - constants.py - different constants using in the application
 - .env - environment variables to configure the application
 - .gitignore - files and folders to exclude from the project structure
 - requirements.txt - file with the project's dependencies
 - run.py - a main file to start the application
 - utils.py - different utility functions to create Flask instance, add namespaces, etc.
 - create_db- this file serves to create and fill up the database from JSON file
 - production.db or sky_rent.db - a database with tables to get data from
 - README.md - this file with app info
 ---
 The project was created in 04 December 2022
