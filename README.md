# Mahider-Back-End
Dont Forget to install the Requirements Inside of Your Virtual Enviroment(and also name it as 'venv')


Routes GuideBook:

For Creating Users
    POST: /api/user/create/
        Items: {
                "username": "", -- mandatory
                "email": "",
                "password": "", -- mandatory
                "first_name": "",
                "last_name": "",
                "bio": "",
                "birthday": null,
                "profile_picture": ""
            }

To Get Token For Authentication
    POST: /api/user/token/
        Items: {
                "username": "",
                "password": ""
            }

To Refresh Tokens
    POST: /api/user/token/refresh/
        Items: {
                "refresh": ""
            }