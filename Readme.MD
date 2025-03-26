# Expense Tracker

This is a Django-based Expense Tracker application that helps users manage their expenses efficiently. It provides a user-friendly interface for adding, editing, and categorizing expenses while storing data securely in a PostgreSQL database.

## Features

- User authentication (Sign up & Login)
- Add, edit, and delete expenses
- Categorization of expenses
- Monthly and yearly expense summaries
- Database integration with PostgreSQL
- Responsive web interface
- Secure session handling

## Installation

### Prerequisites

- Python 3.x installed
- PostgreSQL installed and configured
- Virtual environment setup (recommended)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Expense Tracker
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use: env\Scripts\activate
   ```
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   Create a `.env` file in the root directory and add your database credentials:
   ```
   DATABASE_NAME=your_db_name
   DATABASE_USER=your_db_user
   DATABASE_PASSWORD=your_db_password
   DATABASE_HOST=localhost
   DATABASE_PORT=5432
   SECRET_KEY=your_django_secret_key
   ```
5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- Register or log in to start tracking expenses.
- Add expenses with descriptions and categories.
- View and manage past expenses.

## Folder Structure

```
Expense Tracker/
│-- env/                  # Virtual environment (not committed to Git)
│-- expense_tracker/      # Django project directory
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configurations
│   ├── models.py         # Database models
│   ├── views.py          # Business logic
│   ├── templates/        # HTML templates
│-- static/               # Static files (CSS, JS, Images)
│-- manage.py             # Django management script
│-- requirements.txt      # Project dependencies
│-- .gitignore            # Files to ignore in Git
│-- README.md             # Project documentation
```

## License

This project is open-source under the MIT License.

## Contribution

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
