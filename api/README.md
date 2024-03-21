# API Design Documentation

## Users
Endpoints for managing users

### GET /users
response: [user_id] - array of all user id's in the database

### GET /users/{user_id}
response: User - user data for the user identified by user_id

## Authentication
Endpoints for authenticating and creating user accounts

### POST /auth/register
Body: User - Registration data
Response: int - user_id

### POST /auth/login
Body: Formdata(username, password) - The login information
Response: JWToken - JWT Token containing user information

## Games
Endpoints for creating and playing games

### GET /games/{game_id}
Response: GameState - the state of the game identified by the game id

### POST /games/{game_id}
Body: MoveInfo - The information about the move being made.
Response: Boolean - If the move was succesfully performed or not.
