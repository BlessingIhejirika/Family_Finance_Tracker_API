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
- Create and manage family members
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

The API will be available at `https://capstonefinancialapp-103f06625006.herokuapp.com/ `


## API Endpoints

### Authentication

#### Register
```bash
POST /api/accounts/register/
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe"
}
```

#### Login
```bash
POST /api/accounts/login/
{
    "username": "john_doe",
    "password": "securepassword123"
}
```

**Response (200 OK):**
```json
{
    "token": "your_auth_token_here",
    "user_id": 1,
    "username": "john_doe"
}
```

### Family Management

#### Create Family (Admin)
```bash
POST /api/family-members/create-family-admin/
Headers: Authorization: Token your_auth_token_here
{
    "family_name": "Smith Family"
}
```

**Response (201 Created):**
```json
{
    "family_id": 1,
    "family_name": "Smith Family",
    "admin_id": 1,
    "message": "Family created successfully"
}
```

#### Invite Family Member
```bash
POST /api/family-members/invite/
Headers: Authorization: Token your_auth_token_here
{
    "family_id": 1,
    "email": "jane@example.com",
    "role": "member"
}
```

**Response (200 OK):**
```json
{
    "message": "Invitation sent successfully",
    "invited_email": "jane@example.com"
}
```

#### Accept Family Invitation
```bash
POST /api/family-members/accept-invite/
Headers: Authorization: Token your_auth_token_here
{
    "invitation_token": "token_from_invite_email"
}
```

**Response (200 OK):**
```json
{
    "message": "Invitation accepted",
    "family_id": 1,
    "family_name": "Smith Family"
}
```

#### Get Family Member Details
```bash
GET /api/family-members/member/{member_id}/
Headers: Authorization: Token your_auth_token_here
```

**Response (200 OK):**
```json
{
    "id": 2,
    "user": {
        "id": 2,
        "username": "jane_doe",
        "email": "jane@example.com"
    },
    "family": 1,
    "role": "member",
    "joined_at": "2024-12-07T10:30:00Z"
}
```

### Family Accounts

#### Create Family Account
```bash
POST /api/family-accounts/create-family-account/
Headers: Authorization: Token your_auth_token_here
{
    "family_id": 1,
    "account_name": "Family Savings",
    "account_type": "savings",
    "initial_balance": 5000.00
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "family": 1,
    "account_name": "Family Savings",
    "account_type": "savings",
    "balance": 5000.00,
    "created_at": "2024-12-07T10:30:00Z"
}
```

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

## Testing the API Endpoints

### Using cURL (Command Line)

#### 1. Register a New User
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
  }'
```

#### 2. Login to Get Auth Token
```bash
curl -X POST http://127.0.0.1:8000/api/accounts/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepassword123"
  }'
```
Save the returned `token` for authenticated requests.

#### 3. Create a Family (Authenticated)
```bash
curl -X POST http://127.0.0.1:8000/api/family-members/create-family-admin/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "family_name": "Smith Family"
  }'
```

#### 4. Invite a Family Member
```bash
curl -X POST http://127.0.0.1:8000/api/family-members/invite/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "family_id": 1,
    "email": "jane@example.com",
    "role": "member"
  }'
```

#### 5. Get Family Member Details
```bash
curl -X GET http://127.0.0.1:8000/api/family-members/member/2/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

#### 6. Create Family Account
```bash
curl -X POST http://127.0.0.1:8000/api/family-accounts/create-family-account/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -d '{
    "family_id": 1,
    "account_name": "Family Savings",
    "account_type": "savings",
    "initial_balance": 5000.00
  }'
```

### Using Postman

1. **Import Collection**: Create a new Postman collection
2. **Add Variables**: 
   - Set `base_url` = `http://127.0.0.1:8000`
   - Set `token` = (leave blank, will be updated after login)

3. **Create Requests** for each endpoint above

4. **In the Login request**, go to Tests tab and add:
```javascript
if (pm.response.code === 200) {
    pm.environment.set("token", pm.response.json().token);
}
```

5. **Use token in headers** for authenticated endpoints:
   - Key: `Authorization`
   - Value: `Token {{token}}`

### Using Python Requests

```python
import requests

BASE_URL = "http://127.0.0.1:8000/api"

# 1. Register
response = requests.post(f"{BASE_URL}/accounts/register/", json={
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
})
print(response.json())

# 2. Login
response = requests.post(f"{BASE_URL}/accounts/login/", json={
    "username": "john_doe",
    "password": "securepassword123"
})
token = response.json()["token"]

# 3. Create Family (with auth)
headers = {"Authorization": f"Token {token}"}
response = requests.post(f"{BASE_URL}/family-members/create-family-admin/", 
    headers=headers,
    json={"family_name": "Smith Family"}
)
print(response.json())
```

## Status Codes Reference

| Code | Meaning |
|------|---------|
| 200 | OK - Request successful |
| 201 | Created - Resource created successfully |
| 400 | Bad Request - Invalid input data |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource not found |
| 500 | Server Error - Internal server error |



## General API Endpoint Sample

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
    "username": "username",
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


## Contact

Project Maintainer - [Blessing Ihejirika]
Email: onyinyechukwumblessing@gmail.com
GitHub: https://github.com/BlessingIhejirika

---

**Note**: This is a capstone project developed as part of a learning curriculum. For production use, additional security measures and optimizations should be implemented.
