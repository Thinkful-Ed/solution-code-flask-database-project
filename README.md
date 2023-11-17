# Flask-SQLAlchemy Database Project

This repository contains the implementation of a simple database system using Flask and Flask-SQLAlchemy. The project demonstrates the creation, configuration, and operation of a basic database for AI models.

## Installation

1. Clone this repository.
2. Navigate to the project directory:
```bash
   cd databases_project
```
3. Set up a virtual environment (recommended):
   - For macOS and Linux:
```bash
     python -m venv databases_project_env;
     source databases_project_env/bin/activate;
```
   - For Windows:
```bash
     python -m venv databases_project_env
     .\databases_project_env\Scripts\activate
```
4. Install the required packages:
```shell
   pip install -r requirements.txt
```

## Project Structure

The project is structured into different modules for easy management and scalability:

- `app.py`: Initializes the Flask application and configures the database.
- `config.py`: Contains configuration settings for the database.
- `models.py`: Defines the database models (e.g., `AIModel`).
- `run.py`: The entry point of the Flask application, containing routes and logic.
- `requirements.txt`: Lists all Python packages required for the project.

## Running the Application

To start the Flask application:

```bash
python run.py;
```

- The application will be accessible at `http://127.0.0.1:5001`.
- Use the provided endpoints to interact with the database.

## API Endpoints

1. **Add a New AI Model** (`run.py`):
   - Add a new AI model to the database: `POST /models`
   - Request body should include `name` and `description` of the AI model.

2. **Home Page**:
   - Access the welcome message: `GET /`

## Database Model

The `AIModel` class in `models.py` represents the AI models stored in the database. It includes fields for `id`, `name`, and `description`.

## Notes

- Ensure the virtual environment is activated when running the application.
- The database is configured to use SQLite (`sqlite:///site.db`).

Feel free to modify and extend the project as needed for your specific requirements!
