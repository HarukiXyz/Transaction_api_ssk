# Transaction Management System

**Developer: SAKKARIN**

A comprehensive financial transaction management system built with Django REST Framework and Flutter, featuring secure JWT authentication and wallet management capabilities.

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [Django REST API Documentation](#django-rest-api-documentation)
3. [JWT Authentication Implementation](#jwt-authentication-implementation)
4. [Flutter Client Integration](#flutter-client-integration)
5. [Installation & Setup](#installation--setup)
6. [API Usage Examples](#api-usage-examples)
7. [Security Considerations](#security-considerations)
8. [Troubleshooting](#troubleshooting)

## 🎯 System Overview

This transaction management system consists of three main components:

- **User Management**: User registration, authentication, and profile management
- **Wallet Management**: Digital wallet creation and management
- **Transaction Management**: Financial transaction recording and tracking

### Key Features

- ✅ Secure JWT-based authentication
- ✅ RESTful API architecture
- ✅ Automatic wallet creation on user registration
- ✅ Transaction categorization (Income/Expense)
- ✅ Pagination support for transaction lists
- ✅ Secure password hashing with Argon2
- ✅ UUID-based entity identification
- ✅ Cross-platform Flutter client support

## 🚀 Django REST API Documentation

### Technology Stack

- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL/SQLite
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Argon2
- **API Documentation**: Built-in browsable API

### Data Models

#### User Model
```python
{
  "uuid": "string",           # Unique identifier
  "name": "string",           # Username (unique)
  "first_name": "string",     # User's first name
  "last_name": "string",      # User's last name
  "password": "string",       # Hashed password (Argon2)
  "createdAt": "datetime",    # Creation timestamp
  "updatedAt": "datetime"     # Last update timestamp
}
```

#### Wallet Model
```python
{
  "uuid": "string",           # Unique identifier
  "owner": "string",          # User UUID (foreign key)
  "name": "string",           # Wallet name
  "desc": "string",           # Optional description
  "createdAt": "datetime",    # Creation timestamp
  "updatedAt": "datetime"     # Last update timestamp
}
```

#### Transaction Model
```python
{
  "uuid": "string",           # Unique identifier
  "wallet": "string",         # Wallet UUID (foreign key)
  "name": "string",           # Transaction name
  "desc": "string",           # Optional description
  "amount": "decimal",        # Amount (non-negative)
  "type": "integer",          # -1 (expense) or 1 (income)
  "date": "datetime",         # Transaction date (optional)
  "createdAt": "datetime",    # Creation timestamp
  "updatedAt": "datetime"     # Last update timestamp
}
```

### API Endpoints

#### Authentication Endpoints

##### Register New User
```http
POST /api/auth/register
Content-Type: application/json

{
  "name": "username",
  "first_name": "John",
  "last_name": "Doe",
  "password": "password123"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Create user successfully!"
}
```

**Response (409 Conflict):**
```json
{
  "success": false,
  "message": "Name already exists"
}
```

##### User Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "name": "username",
  "password": "password123"
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "login successfully!",
  "data": {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "auth": {
      "uuid": "user-uuid",
      "name": "username",
      "first_name": "John",
      "last_name": "Doe"
    }
  }
}
```

#### Transaction Endpoints

##### Create Transaction
```http
POST /api/transaction
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
  "name": "Grocery Shopping",
  "desc": "Weekly groceries",
  "amount": 1500,
  "type": -1,
  "date": "2024-01-15"
}
```

**Response (201 Created):**
```json
{
  "success": true,
  "message": "Transaction created successfully",
  "data": {
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "wallet": "550e8400-e29b-41d4-a716-446655440001",
    "name": "Grocery Shopping",
    "desc": "Weekly groceries",
    "amount": 1500,
    "type": -1,
    "date": "2024-01-15T00:00:00.000Z",
    "createdAt": "2024-01-15T10:30:00.000Z",
    "updatedAt": "2024-01-15T10:30:00.000Z"
  }
}
```

##### Get All Transactions
```http
GET /api/transaction?page=1&limit=10
Authorization: Bearer <jwt_token>
```

**Response (200 OK):**
```json
{
  "success": true,
  "message": "Transactions retrieved successfully",
  "data": [
    {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "wallet": "550e8400-e29b-41d4-a716-446655440001",
      "name": "Salary",
      "desc": "Monthly salary",
      "amount": 50000,
      "type": 1,
      "date": "2024-01-15T00:00:00.000Z",
      "createdAt": "2024-01-15T10:30:00.000Z",
      "updatedAt": "2024-01-15T10:30:00.000Z"
    }
  ],
  "meta": {
    "page": 1,
    "limit": 10,
    "total": 25,
    "totalPages": 3
  }
}
```

##### Get Transaction by ID
```http
GET /api/transaction/<transaction-uuid>
Authorization: Bearer <jwt_token>
```

##### Update Transaction
```http
PUT /api/transaction/<transaction-uuid>
Authorization: Bearer <jwt_token>
Content-Type: application/json

{
  "name": "Updated Transaction Name",
  "amount": 2000,
  "type": -1
}
```

##### Delete Transaction
```http
DELETE /api/transaction/<transaction-uuid>
Authorization: Bearer <jwt_token>
```

### HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid or incomplete data |
| 401 | Unauthorized | Authentication required or token expired |
| 404 | Not Found | Resource not found |
| 409 | Conflict | Resource already exists |
| 500 | Internal Server Error | Server error |

## 🔐 JWT Authentication Implementation

### JWT Token Structure

The system uses JWT tokens for stateless authentication with the following structure:

```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "user_id": "user-uuid",
    "username": "username",
    "exp": 1642680000,
    "iat": 1642593600
  }
}
```

### Token Security Features

- **Argon2 Password Hashing**: Industry-standard password hashing
- **Token Expiration**: Configurable token lifetime
- **Secure Headers**: Proper CORS and security headers
- **UUID-based Identification**: Non-guessable entity IDs

### Authentication Flow

1. **Registration**: User creates account → Automatic wallet creation
2. **Login**: Credentials validation → JWT token generation
3. **API Access**: Token validation on each protected endpoint
4. **Token Expiration**: Automatic logout and redirect to login

### Django JWT Settings

```python
# settings.py
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'uuid',
    'USER_ID_CLAIM': 'user_id',
}
```

## 📱 Flutter Client Integration

### Required Dependencies

```yaml
dependencies:
  flutter_secure_storage: ^9.0.0
  get: ^4.6.6
  http: ^1.1.0
```

### JWT Storage Implementation

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class JwtStorage {
  static const _storage = FlutterSecureStorage();
  static const String _tokenKey = 'jwt_token';

  static Future<void> saveToken(String token) async {
    try {
      await _storage.write(key: _tokenKey, value: token);
    } catch (e) {
      print('Error saving token: $e');
    }
  }

  static Future<String?> getToken() async {
    try {
      return await _storage.read(key: _tokenKey);
    } catch (e) {
      print('Error reading token: $e');
      return null;
    }
  }

  static Future<void> deleteToken() async {
    try {
      await _storage.delete(key: _tokenKey);
    } catch (e) {
      print('Error deleting token: $e');
    }
  }
}
```

### API Service Implementation

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:get/get.dart';

class ApiService extends GetxController {
  String get version => "1.2.0";

  Future<http.Response> _handleResponse(
      Future<http.Response> Function() apiCall) async {
    try {
      final response = await apiCall();
      if (response.statusCode == 403) {
        await logout();
        throw Exception('Token expired. User logged out.');
      }
      return response;
    } catch (e) {
      rethrow;
    }
  }

  Future<http.Response> get(String endpoint) async {
    return _handleResponse(() async {
      final token = await JwtStorage.getToken();
      return await http.get(
        Uri.parse(endpoint),
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
          'app_version': version,
        },
      );
    });
  }

  Future<http.Response> post(String endpoint, dynamic data) async {
    return _handleResponse(() async {
      final token = await JwtStorage.getToken();
      return await http.post(
        Uri.parse(endpoint),
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
          'app_version': version,
        },
        body: json.encode(data),
      );
    });
  }

  Future<bool> logout() async {
    try {
      await JwtStorage.deleteToken();
      Get.offAllNamed('/login');
      return true;
    } catch (e) {
      print('Error during logout: $e');
      return false;
    }
  }
}
```

## ⚙️ Installation & Setup

### Backend Setup (Django)

1. **Clone the repository:**
```bash
git clone <repository-url>
cd transaction-management-system
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure database:**
```bash
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Run development server:**
```bash
python manage.py runserver
```

### Frontend Setup (Flutter)

1. **Navigate to Flutter directory:**
```bash
cd flutter_client
```

2. **Install dependencies:**
```bash
flutter pub get
```

3. **Configure API endpoints:**
```dart
// lib/config/api_config.dart
class ApiConfig {
  static const String baseUrl = 'http://your-api-domain.com';
  static const String apiVersion = 'v1';
}
```

4. **Run the app:**
```bash
flutter run
```

## 🔧 API Usage Examples

### Using cURL

```bash
# Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"name":"testuser","password":"password123"}'

# Create Transaction
curl -X POST http://localhost:8000/api/transaction \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "Coffee Purchase",
    "desc": "Morning coffee",
    "amount": 150,
    "type": -1
  }'

# Get Transactions
curl -X GET "http://localhost:8000/api/transaction?page=1&limit=10" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### Using JavaScript/Fetch

```javascript
// Login function
async function login(username, password) {
  const response = await fetch('/api/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: username,
      password: password
    })
  });
  
  const data = await response.json();
  if (data.success) {
    localStorage.setItem('token', data.data.access);
    return data.data.access;
  }
  throw new Error(data.message);
}

// Create transaction function
async function createTransaction(transactionData) {
  const token = localStorage.getItem('token');
  const response = await fetch('/api/transaction', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(transactionData)
  });
  
  return await response.json();
}
```

## 🛡️ Security Considerations

### Backend Security
- ✅ **Password Security**: Argon2 hashing algorithm
- ✅ **Token Security**: JWT with proper expiration
- ✅ **CORS Configuration**: Properly configured cross-origin requests
- ✅ **Input Validation**: Comprehensive request validation
- ✅ **SQL Injection Protection**: Django ORM protection

### Client Security
- ✅ **Secure Storage**: Flutter Secure Storage for tokens
- ✅ **HTTPS Only**: All API calls over HTTPS in production
- ✅ **Token Validation**: Automatic token expiration handling
- ✅ **Input Sanitization**: Proper input validation on client side

### Best Practices
- Always use HTTPS in production
- Implement proper token refresh mechanism
- Regular security updates for dependencies
- Monitor for suspicious activities
- Implement rate limiting for API endpoints

## 🔍 Troubleshooting

### Common Issues

#### 1. Token Expired Error
```json
{
  "success": false,
  "message": "Unauthorized"
}
```
**Solution**: Re-authenticate by calling the login endpoint

#### 2. Validation Errors
```json
{
  "success": false,
  "message": "Invalid transaction data",
  "errors": {
    "amount": ["Amount must be non-negative"]
  }
}
```
**Solution**: Check request data format and validation rules

#### 3. Wallet Not Found
```json
{
  "success": false,
  "message": "Wallet not found"
}
```
**Solution**: Ensure user has a wallet (should be auto-created on registration)

### Debug Mode

Enable debug mode in Django settings for development:
```python
DEBUG = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
    },
}
```

### Flutter Debug

Use Flutter Inspector and console logs:
```dart
print('API Response: ${response.body}');
print('Token: ${await JwtStorage.getToken()}');
```

## 📞 Support

For questions or issues, please contact:
- **Developer**: SAKKARIN
- **Email**: [your-email@example.com]
- **GitHub**: [your-github-profile]

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Created by SAKKARIN** - Transaction Management System with Django REST API and JWT Authentication