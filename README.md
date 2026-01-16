# Family Finance Tracker API

A RESTful API built with Django REST Framework for families to manage and track shared and individual finances. Users can belong to a family group, log income and expenses, set budgets, and view comprehensive financial reports.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Models](#models)
- [Usage Examples](#usage-examples)
- [Testing](#testing)
- [Deployment](#deployment)
- [Project Timeline](#project-timeline)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Family Finance Tracker API enables families to collaboratively manage their finances through a centralized platform. Family members can track individual and shared expenses, set budgets, and generate detailed financial reports.

## Features

### Core Features

#### 1. User & Family Management
- Full CRUD operations for user accounts
- Create and manage family groups
- Invite users to join families
- Assign roles within family groups

#### 2. Transaction Management
- Add income or expense transactions
- Categorize transactions by type
- Assign transactions to individuals or shared family accounts
- Update or delete existing transactions
- Track transaction history with dates and descriptions

#### 3. Budgets & Reports
- Set monthly budgets per category or family member
- Generate family-wide spending summaries
- View individual spending reports
- Optional graphical summaries and budget alerts

### Optional Advanced Features
- Track allowances for children
- Budget overage alerts
- Recurring transactions (subscriptions, bills)
- Currency conversion integration

## Technology Stack

- **Backend Framework**: Django & Django REST Framework (DRF)
- **Database**: MySQL
- **Authentication**: JWT/Token-based authentication
- **API Documentation**: Swagger/DRF-YASG
- **Deployment**: Heroku/PythonAnywhere

## Project Structure
```
family-finance-tracker/
├── manage.py
├── requirements.txt
├── README.md
├── finance_tracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── families/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── transactions/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
└── budgets/
    ├── models.py
    ├── views.py
    ├── serializers.py
    └── urls.py
```

## Installation

### Prerequisites

- Python 3.8+
- MySQL 5.7+
- pip
- virtualenv (recommended)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/family-finance-tracker.git
cd family-finance-tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### Users
- `GET /users/` - List all users
- `POST /users/` - Create a new user
- `GET /users/{id}/` - Retrieve user details
- `PUT /users/{id}/` - Update user information
- `DELETE /users/{id}/` - Delete a user

### Families
- `GET /families/` - List all families
- `POST /families/` - Create a new family
- `GET /families/{id}/` - Retrieve family details
- `PUT /families/{id}/` - Update family information
- `DELETE /families/{id}/` - Delete a family

### Transactions
- `GET /transactions/` - List all transactions
- `POST /transactions/` - Create a new transaction
- `GET /transactions/{id}/` - Retrieve transaction details
- `PUT /transactions/{id}/` - Update transaction
- `DELETE /transactions/{id}/` - Delete transaction

### Budgets
- `GET /budgets/` - List all budgets
- `POST /budgets/` - Create a new budget
- `GET /budgets/{id}/` - Retrieve budget details
- `PUT /budgets/{id}/` - Update budget
- `DELETE /budgets/{id}/` - Delete budget

### Reports
- `GET /reports/family/{family_id}/` - Generate family-wide financial report
- `GET /reports/user/{user_id}/` - Generate individual user financial report

## Authentication

The API uses token-based authentication via Django REST Framework.

### Obtaining a Token
```bash
POST /api/token/
{
    "email": "user@example.com",
    "password": "your_password"
}
```

### Using the Token

Include the token in the Authorization header:
```
Authorization: Token your_token_here
```

## Models

### User
- `id` - Primary key
- `name` - User's full name
- `email` - User's email address (unique)
- `password` - Hashed password
- `date_joined` - Account creation timestamp

### Family
- `id` - Primary key
- `name` - Family group name
- `owner` - ForeignKey to User (family creator)
- `members` - ManyToMany relationship with User
- `created_at` - Family creation timestamp

### Transaction
- `id` - Primary key
- `user` - ForeignKey to User
- `family` - ForeignKey to Family
- `type` - Choice field (income/expense)
- `category` - Transaction category
- `amount` - Decimal field for transaction amount
- `date` - Transaction date
- `description` - Optional text description

### Budget
- `id` - Primary key
- `family` - ForeignKey to Family
- `user` - Optional ForeignKey to User (for individual budgets)
- `category` - Budget category
- `amount` - Decimal field for budget limit
- `month` - Integer field (1-12)
- `year` - Integer field

## Usage Examples

### Create a Family
```bash
POST /families/
{
    "name": "Smith Family",
    "owner": 1
}
```

### Add a Transaction
```bash
POST /transactions/
{
    "user": 1,
    "family": 1,
    "type": "expense",
    "category": "Groceries",
    "amount": 150.50,
    "date": "2024-12-07",
    "description": "Weekly grocery shopping"
}
```

### Set a Budget
```bash
POST /budgets/
{
    "family": 1,
    "category": "Groceries",
    "amount": 500.00,
    "month": 12,
    "year": 2024
}
```

## Testing

Run tests using Django's test framework:
```bash
python manage.py test
```

## Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Create a new Heroku app:
```bash
heroku create family-finance-tracker
```
3. Add MySQL addon:
```bash
heroku addons:create cleardb:ignite
```
4. Deploy:
```bash
git push heroku main
```

### PythonAnywhere Deployment

Follow PythonAnywhere's Django deployment guide at: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/

## Project Timeline

### Week 1: Foundation
- Project setup and environment configuration
- Django project initialization
- Database model design and implementation

### Week 2: User Management
- User and Family CRUD operations
- Authentication setup and testing
- User invitation system

### Week 3: Transactions
- Transaction management endpoints
- Category management
- Basic CRUD operations

### Week 4: Budgets & Reports
- Budget management system
- Reporting endpoints
- Summary calculations and analytics

### Week 5: Finalization
- Comprehensive testing
- API documentation with Swagger
- Deployment to production
- Final polishing and bug fixes

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Project Maintainer - [Your Name]
Email: your.email@example.com
GitHub: [@yourusername](https://github.com/yourusername)

---

**Note**: This is a capstone project developed as part of a learning curriculum. For production use, additional security measures and optimizations should be implemented.
