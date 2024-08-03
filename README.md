# Mahider Back-End

## Setup

1. **Install the Requirements**

   Make sure to install the required packages inside your virtual environment. Name your virtual environment `venv` for consistency.

   ```bash
   pip install -r requirements.txt

Routes Guide
Create User

    Endpoint: POST /api/user/create/
    Description: Creates a new user.
    Request Body:

    json

    {
      "username": "",        // Mandatory
      "email": "",
      "password": "",        // Mandatory
      "first_name": "",
      "last_name": "",
      "bio": "",
      "birthday": null,
      "profile_picture": ""
    }

Get Token for Authentication

    Endpoint: POST /api/user/token/
    Description: Retrieves an authentication token for the user.
    Request Body:

    json

    {
      "username": "",
      "password": ""
    }

Refresh Token

    Endpoint: POST /api/user/token/refresh/
    Description: Refreshes an existing authentication token.
    Request Body:

    json

{
  "refresh": ""
}