# Hackathon Registration Site

## Overview

The Hackathon Registration Site is a web application built with Django and React that allows users to register, form teams, and submit solutions to various problem statements. This platform provides a structured environment for managing hackathons, including user authentication, team formation, problem statement management, solution submission, and leaderboard ranking.

## Features

- **User Authentication**: Signup and login functionality for users.
- **Team Management**: Users can create or join teams.
- **Problem Statements**: A dedicated page to view challenges users can solve.
- **Submission Portal**: Teams can submit their solutions for evaluation.
- **Leaderboard**: Ranks teams based on submission evaluations.
- **Admin Panel**: Manage users, teams, problem statements, and view submissions and leaderboard metrics.

## Technologies Used

- **Backend**: Django Framework, MySQL (with optional MongoDB)
- **Frontend**: React, HTML, CSS, JavaScript (with Bootstrap for styling)
- **Libraries**: Django REST Framework (for APIs if required)

## Installation

### Prerequisites

- Python 3.x
- Django
- MySQL
- Node.js and npm

### Setting Up Python Environment

1. **Create a Virtual Environment**:
   It's good practice to create a virtual environment for your Python projects to manage dependencies.

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Required Python Packages**:

   Navigate to the backend directory (if applicable) and install the required packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up npm Environment

1. **Navigate to the Frontend Directory**:

   ```bash
   cd frontend/frontend-react
   ```

2. **Install Required npm Packages**:

   Use `npm` to install the packages listed in `package.json`:

   ```bash
   npm install
   ```

3. **Build the React App**:

   After installing the packages, build the React app:

   ```bash
   npm run build
   ```

### Database Setup

1. **Create a MySQL Database**:

   You will need to create a database in MySQL. Open your MySQL shell and execute:

   ```sql
   CREATE DATABASE hackathon_db;
   ```

2. **Migrate the Database**:

   In the backend directory, run the migrations to set up your database schema:

   ```bash
   python manage.py migrate
   ```

3. **Create a Superuser (Optional)**:

   You can create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

### Running the Application

1. **Start the Django Server**:

   In the backend directory, start the Django server:

   ```bash
   python manage.py runserver
   ```

2. **Access the Application**:

   Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [React](https://reactjs.org/)
- [Bootstrap](https://getbootstrap.com/)
