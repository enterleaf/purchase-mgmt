## Purchase Management Backend

### Description:


### Features:
- Django 3.x
- PostgreSQL database setup
- Custom user model
- Django REST Framework integration
- Basic user authentication and authorization
- Environment variable configuration
- Poetry for dependency management
- Makefile for common development tasks automation
- Flake8 for linting code
- EditorConfig for consistent coding styles
- Pre-commit hooks for automatic checks before committing code changes

### Installation:
Clone the repository:
```bash
git clone 
```

Navigate to the project directory:
```
cd 
```
Install the requirements using poetry (if not already installed{install globally}):
```bash
poetry install
```
Install Flake8 globally (optional but recommended):
```bash
pip install flake8
```
Install EditorConfig plugin for your preferred code editor to enforce consistent coding styles.

Install pre-commit hooks:
```bash
poetry run pre-commit install
```
Create virtual environment (or poetry will build its own):
```bash
python -m venv venv
```
Run the project:
```
make runserver
```
Run Migrations:
```bash
make migrate
```

Run pre-commit tests mannually:
```bash
make pre-commit
```





### License:
This project is licensed under the MIT License.