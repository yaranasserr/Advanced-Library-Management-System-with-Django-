# Advanced-Library-Management-System-with-Django-


## Project Idea: Advanced Library Management System
This project aims to build a comprehensive library management system that manages libraries, books, authors, and categories. The system includes features such as user registration, login, password recovery, and allows users to borrow and return multiple books in one transaction. It also provides notifications and real-time updates for book availability.

## Key Features:
- **Library Management:**
  - List all libraries
  - Filter libraries by book categories and authors
  - Calculate distances between users and nearby libraries
- **Authors:**
  - List authors with book counts
  - Filter authors by library and book category (book counts should update accordingly)
- **Books:**
  - List all books
  - Filter books by category, library, and author
  - Return author and category names
- **Loaded Authors Endpoint:**
  - List authors with all their books
  - Each book includes its category object
  - Filter by category and library

## Task Details:

### 1. Notifications:
- **Email Notifications:**
  - Send confirmation emails upon borrowing. 
  - Test locally with Mailhog (no actual email service required like AWS SES or Sendmail).
  - Send daily reminders for the last 3 days of the borrowing period using Celery (or an alternative) for email sending.

### 2. Business Logic:
- **Borrowing Rules:**
  - Allow users to borrow up to 3 books; to borrow a 4th, they must return one.
  - Users must specify a return date (max 1 month). Late returns incur a daily penalty.
  
- **Penalty Calculation:**
  - Calculate penalties based on overdue days.

## Project Structure:
The project is divided into 6 different apps, each handling a specific function:
- **authors:** Manages authors and their books
- **books:** Manages books and their details
- **borrow:** Manages borrowing transactions and rules
- **library:** Manages library information and locations
- **notifications:** Handles email notifications and reminders
- **users:** Handles user authentication, registration, and password recovery

## Database Schema

![Database Schema](https://github.com/yaranasserr/Advanced-Library-Management-System-with-Django-/blob/main/QuickDBD-export.png?raw=true)


### Implementation Steps:
1. **Started with the following apps:**
   - **Users:** Implemented user authentication (login, registration, password recovery)
   - **Books and Authors:** Created models and views to list books and authors
2. **User Dashboard:** Developed the dashboard for users to manage their borrowed books
3. **Borrowing Logic:** Implemented business logic to allow borrowing up to 3 books, return logic, and penalty calculation for overdue books
4. **Password Recovery:** Implemented a system for users to recover their passwords
5. **Confirmation Email:** Set up email notifications for borrowing confirmations using Mailhog
6. **Daily Reminders:** Integrated Celery for sending daily reminders about overdue books
7. **Availability Notifications:** Set up notifications for book availability
8. **Distance Calculation:** Used `geopy.distance` for calculating distances between users and libraries
9. **Swagger:** Integrated Swagger for API documentation
10. **Dockerization:** Containerized the app using Docker for easy deployment

ment

## How to Run This Project:

### 1. Activate the virtual environment:

Make sure your virtual environment is activated:

- **On Windows:**

  

```

  venv\Scripts\activate
```

- On macOS/Linux:

  ```
  source venv/bin/activate
  ```


### 2. Start the Django development server:

Run the Django server:

```
python manage.py runserver
```

### 3. Use Mailhog for email testing:

Run Mailhog locally using Docker:

```
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
```

### 4. Start Redis for Celery:

Run Redis locally in Docker:

```
docker run -d -p 6379:6379 redis
```

### 5. Start Celery workers:

In the first terminal, run Celery's beat scheduler:

```
celery -A librarysystem beat --loglevel=info
```

In a second terminal, run the Celery worker:
```
celery -A librarysystem worker --loglevel=info
```
Dependencies:
Django
Celery
Redis
Mailhog
geopy
Swagger
Docker
## Demo

