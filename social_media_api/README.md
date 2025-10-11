# Social Media API

This is a Django-based REST API for a social media application, featuring a custom user model and token-based authentication.

## Features

*   **Custom User Model:** Extends the default Django user to include a bio, profile picture, and followers.
*   **Token Authentication:** Uses Django Rest Framework's Token Authentication for securing endpoints.
*   **User Registration:** Endpoint to create new users.
*   **User Login:** Endpoint to authenticate users and retrieve an auth token.
*   **Profile Management:** Endpoint for authenticated users to view and update their own profiles.

## Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/blaizre/Alx_DjangoLearnLab
    cd social_media_api
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    Django
    djangorestframework
    ```
    Then install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations:**
    Run the following command to create the necessary database tables, including the `CustomUser` model.
    ```bash
    python3 manage.py migrate
    ```

5.  **Run the Development Server:**
    ```bash
    python3 manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

All endpoints are prefixed with `/api/accounts/`.

### User Registration

*   **Endpoint:** `POST /api/accounts/register/`
*   **Description:** Creates a new user and returns their data along with an authentication token.
*   **Authentication:** None required.
*   **Request Body:**
    ```json
    {
        "username": "newuser",
        "password": "yoursecurepassword",
        "email": "user@example.com",
        "bio": "A little about me.",
        "profile_picture": "(optional, form-data)"
    }
    ```
*   **Success Response (201 CREATED):**
    ```json
    {
        "user": {
            "id": 1,
            "username": "newuser",
            "email": "user@example.com",
            "bio": "A little about me.",
            "profile_picture": null
        },
        "token": "your_auth_token_string"
    }
    ```

### User Login

*   **Endpoint:** `POST /api/accounts/login/`
*   **Description:** Authenticates a user with their username and password and returns an auth token.
*   **Authentication:** None required.
*   **Request Body:**
    ```json
    {
        "username": "newuser",
        "password": "yoursecurepassword"
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "token": "your_auth_token_string"
    }
    ```

### View & Update User Profile

*   **Endpoint:** `GET, PUT, PATCH /api/accounts/profile/`
*   **Description:** Allows an authenticated user to retrieve, fully update (`PUT`), or partially update (`PATCH`) their own profile.
*   **Authentication:** **Required**. The request must include the `Authorization` header:
    ```
    Authorization: Token your_auth_token_string
    ```
*   **Request Body (for PUT/PATCH):**
    ```json
    {
        "bio": "An updated bio.",
        "email": "newemail@example.com"
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "id": 1,
        "username": "newuser",
        "email": "newemail@example.com",
        "bio": "An updated bio.",
        "profile_picture": null
    }
    ```

## User Model (`CustomUser`)

The `CustomUser` model is the core of the user system and includes the following key fields:

*   `username`: The user's unique username.
*   `email`: The user's unique email address.
*   `bio`: A text field for the user's biography.
*   `profile_picture`: An image field for the user's profile picture.
*   `followers`: A many-to-many relationship allowing users to follow each other.
# Social Media API

This is a Django-based REST API for a social media application, featuring a custom user model and token-based authentication.

## Features

*   **Custom User Model:** Extends the default Django user to include a bio, profile picture, and followers.
*   **Token Authentication:** Uses Django Rest Framework's Token Authentication for securing endpoints.
*   **User Registration:** Endpoint to create new users.
*   **User Login:** Endpoint to authenticate users and retrieve an auth token.
*   **Profile Management:** Endpoint for authenticated users to view and update their own profiles.

## Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd social_media_api
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    Install the project dependencies from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations:**
    Run the following command to create the necessary database tables, including the `CustomUser` model.
    ```bash
    python3 manage.py migrate
    ```

5.  **Run the Development Server:**
    ```bash
    python3 manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

All endpoints are prefixed with `/api/accounts/`.

### User Registration

*   **Endpoint:** `POST /api/accounts/register/`
*   **Description:** Creates a new user and returns their data along with an authentication token.
*   **Authentication:** None required.
*   **Request Body:**
    ```json
    {
        "username": "newuser",
        "password": "yoursecurepassword",
        "email": "user@example.com",
        "bio": "A little about me.",
        "profile_picture": "(optional, form-data)"
    }
    ```
*   **Success Response (201 CREATED):**
    ```json
    {
        "user": {
            "id": 1,
            "username": "newuser",
            "email": "user@example.com",
            "bio": "A little about me.",
            "profile_picture": null
        },
        "token": "your_auth_token_string"
    }
    ```

### User Login

*   **Endpoint:** `POST /api/accounts/login/`
*   **Description:** Authenticates a user with their username and password and and returns an auth token.
*   **Authentication:** None required.
*   **Request Body:**
    ```json
    {
        "username": "newuser",
        "password": "yoursecurepassword"
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "token": "your_auth_token_string"
    }
    ```

### View & Update User Profile

*   **Endpoint:** `GET, PUT, PATCH /api/accounts/profile/`
*   **Description:** Allows an authenticated user to retrieve, fully update (`PUT`), or partially update (`PATCH`) their own profile.
*   **Authentication:** **Required**. The request must include the `Authorization` header:
    ```
    Authorization: Token your_auth_token_string
    ```
*   **Request Body (for PUT/PATCH):**
    ```json
    {
        "bio": "An updated bio.",
        "email": "newemail@example.com"
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "id": 1,
        "username": "newuser",
        "email": "newemail@example.com",
        "bio": "An updated bio.",
        "profile_picture": null
    }
    ```

## User Model (`CustomUser`)

The `CustomUser` model is the core of the user system and includes the following key fields:

*   `username`: The user's unique username.
*   `email`: The user's unique email address.
*   `bio`: A text field for the user's biography.
*   `profile_picture`: An image field for the user's profile picture.
*   `followers`: A many-to-many relationship allowing users to follow each other.
