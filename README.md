# Moringa Theater Audition Management System

## Overview
This project is a database-driven application for managing auditions at the Moringa Theater Company. It allows actors to audition for roles, with functionality to store and retrieve audition details, assign roles, and track hired actors.

## Features
- Create and manage **Roles**
- Create and manage **Auditions**
- Retrieve lists of roles, actors, and audition locations
- Determine the lead and understudy for a role
- Call back actors by changing their hired status

## Technologies Used
- **Python 3**
- **SQLAlchemy** (ORM for database interaction)
- **SQLite** (Database)
- **Alembic** (For database migrations, optional)

## Installation
### Prerequisites
Ensure you have Python and Pipenv installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-actual-username]/moringa-theater.git
   cd moringa-theater
   ```

2. Install dependencies:
   ```sh
   pipenv install
   ```

3. Activate the virtual environment:
   ```sh
   pipenv shell
   ```


   ```

## Project Structure
```
├── migrations/         # Alembic migrations (if used)
├── models.py           # SQLAlchemy models for Role and Audition
├── database.py         # Database connection setup
├── crud.py             # Functions for CRUD operations
├── main.py             # Entry point for running/testing the application
├── Pipfile             # Pipenv dependencies file
├── README.md           # Project documentation
```

## Usage
### Running the Application
To test and interact with the database, run:
```sh
python main.py
```

### Adding a Role
```python
from models import Role
from crud import add_role

# Example of adding a role
role = add_role("Hamlet")
print(f"Added role: {role.name}")
```

### Adding an Audition
```python
from models import Audition
from crud import add_audition

# Example of adding an audition
audition = add_audition(
    actor_name="John Doe",
    location="New York",
    phone=1234567890,
    role_id=1
)
print(f"Added audition for: {audition.actor_name}")
```

### Fetching All Roles
```python
from crud import get_roles
roles = get_roles()
print(roles)
```

### Testing
To run the test suite:
```bash
python3 main.py```

## Migrations (Optional)
If using **Alembic** for database migrations:
```sh
pipenv install alembic
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, contact [jeyceejeyka635@gmail.com]

