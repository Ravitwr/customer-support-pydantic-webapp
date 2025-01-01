# Customer Support AI

A backend customer support sample built with FastAPI, SQLAlchemy, and Pydantic AI.

## Project Structure

The project follows a modular structure with the following main components:

- `app/`: Main application directory
  - `agents/`: AI agents for different functionalities
  - `api/`: API routes and endpoints
  - `core/`: Core configurations and database setup
  - `dependencies/`: Dependency injection classes
  - `models/`: Data models and schemas
  - `repositories/`: Database interaction layer


## Setup and Installation

1. Clone the repository
2. Install dependencies using Poetry:
   ```bash
   poetry install --no-root
   ```
3. Set up environment variables in `.env` file (refer to `.env.example`):

4. Run the application:
   ```bash
   uvicorn app.main:app --reload --port 8080
   ```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`
