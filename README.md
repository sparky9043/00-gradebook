# 00-gradebook
This is a gradebook application that I made using Python and Django

To run this app, please take the following steps:
1. Make sure that you're in the `00-gradebook` root folder
2. Initialize and activate virtual environment:
  a. Type `python -m venv venv` to create a virtual environment
  b. Activate virtual environment.
    Windows:
      - Git bash: `source venv/Scripts/activate`
  c. Upgrade pip using `pip install --upgrade pip`
3. Install django using `pip install django`
4. Migrate database using `python manage.py migrate`
5. Run server using `python manage.py runserver`
