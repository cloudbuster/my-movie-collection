# Movie Collection Project (Django + uv)

## Critical Workflow Rules
- **Package Manager**: Use `uv`. Always add dependencies with `uv add <package>`.
- **Command Execution**: ALWAYS prefix python commands with `uv run`. 
  - Correct: `uv run python manage.py migrate`
  - Incorrect: `python manage.py migrate`
- **Environment**: The project uses a `.venv` managed by `uv`. Do not use `pip` or `venv` directly.

## Standard Commands
- Install project: `uv sync`
- Database migrations: `uv run python manage.py makemigrations && uv run python manage.py migrate`
- Development server: `uv run python manage.py runserver`
- Create admin user: `uv run python manage.py createsuperuser`
- Run tests: `uv run python manage.py test`

## Project Specifics
- **App Name**: `movie_app`
- **Django Version**: 6.0+ (Latest via uv)
- **Style**: Use functional views with templates initially. Keep `models.py` logic thin.
