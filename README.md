# Customer Support AI

A backend customer support sample built with FastAPI, SQLAlchemy, and Pydantic AI.

## Prerequisites

Before running the project, ensure you have:

1. **OpenAI API Key** set up in your system environment(for example .zshrc in macos or .bashrc in linux)
2. **PostgreSQL Database**:
   - `customers`: Store customer information
   - `loans`: Manage loan details
   - `loan_payments`: Track payment transactions
   - `payment_schedule`: Store scheduled payments
   - `loan_documents`: Manage loan-related documents

> Note: SQL scripts for table creation and sample data are available in:
> - `util/tables.sql`: Database schema definitions
> - `util/dml.sql`: Sample data insertion scripts

## Project Structure

The project follows a modular structure with the following main components:

- `app/`: Main application directory
  - `agents/`: AI agents for different functionalities
  - `api/`: API routes and endpoints
  - `core/`: Core configurations and database setup
  - `dependencies/`: Dependency injection classes
  - `models/`: Data models and schemas
  - `repositories/`: Database interaction layer
- `util/`: Utility files
  - `tables.sql`: Database schema definitions
  - `dml.sql`: Sample data insertion scripts


## Setup and Installation

1. Clone the repository
2. Install dependencies using Poetry:
   ```bash
   poetry install --no-root
   ```
3. Activate the Poetry virtual environment:
   ```bash
   poetry shell
   ```
4. Set up environment variables in `.env` file (refer to `.env.example`)
5. Run the application:
   ```bash
   uvicorn app.main:app --reload --port 8080
   ```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`
