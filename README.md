# Technical Test for Data Gran's Job Application
---

### To-Do List Application with User engine 
### Developed by: [Juan Sebastian Pinto](https://www.linkedin.com/in/jsebastianpinto85/)

## Built using :

* Flask : Python Based mini-Webframework
* MongoDB : Database Server
* mongoengine : Database  Document-Object Mapper( For creating connectiong between MongoDB and Flask )
* Bootstrap v4 and Jquery: For Front-end

## Features:
* MVC Architecture

### Home Page:
* Responsive
* Navigation bar

### Register Page:
* Responsive
* User can register with email and password
* If the email if already registered, shows an alert
* If password and confirm password inputs dont match, shows an alert
* If registration succed, redirects to login page

### Login Page:
* Responsive
* Checks if email exists, if not, shows an alert
* Check if## password is correct, if not, shows an alert
* If login succed, creates a session, and redirects to to-do list page

### List Page:
* Responsive
* Each user have a different list
* User can Add, Delete and Update a task.
* All actions are performed with ajax so, no refresh needed