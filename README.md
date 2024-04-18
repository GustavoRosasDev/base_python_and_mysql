<!-- Logo -->
<p align="center">
  <img width="45" align="center" src="src/images/python.png">
    <b> + </b>
  <img width="90" align="center" src="src/images/mysql.png">
</p>

<!-- Title -->
<h1 align="center">
  Base: Python and MySQL
</h1>

<!-- Subtitle -->
<p align="center">
  Initial base for creating fully modularized Python projects with MySQL connection.<br>Start off on the right foot!
</p>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Open-Source-brightgreen" alt="Source Code">
  <img src="https://img.shields.io/badge/Fully-Modularized-brightgreen" alt="Fully Modularized">
  <img src="https://img.shields.io/badge/Python-3.11-yellow" alt="Python">
  <img src="https://img.shields.io/badge/MySQLWorkbench-8.0-orange" alt="MySQL">
</p>

## Basic instructions 

1 - Open and initialize the MySQL Workbench software in your localhost.

2 - Create a file named .env in the root directory, and populate it with your chosen database credentials as follows:
```
user='your_database_username'
password='your_database_password'
database='your_database_name'
```

3 - Create Virtual Environment
```
python -m venv venv
```

4 - Navigate to Virtual Environment
```
cd venv\Scripts
```

5 - Activate Virtual Environment
```
.\activate
```

6 - Return to main folder (write this twice)
```
cd ..
```

7 - Install requirements
```
pip install -r requirements.txt
```

8 - Run project
```
python main.py
```

## Now, create your own custom functions 😉
###### Basic structure for using MySQL in Python:
    1. Write the SQL command.
    2. Execute the command.
    3. TIP: If it is...
        3.1 An editing command (e.g., Create, Update, or Delete), use: connection.commit().
        3.2 A reading command (e.g., Read), use connection.fetchall().

## References
Obs: All videos below are in portuguese.
###### (Playlist) Basic course of SQL: https://www.youtube.com/playlist?list=PLpdAy0tYrnKw_F8v6kkEXTeyE33Navv-K
###### (Video) CRUD in Python: https://www.youtube.com/watch?v=_q3j25ACmQ4

<!-- SVG Typing -->
<p align="center"><br /><br />
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=4285F4&center=true&random=false&width=435&lines=Keep+Learning.+Keep+Developing!" alt="Typing SVG">
</p><br /><br />