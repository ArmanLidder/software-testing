# Django Web Application Functional Testing

This sub-project demonstrates functional unit and integration testing of a Django web application (a simple budgeting tool). It uses Django's native testing framework (built on Python's `unittest` library) to test models, forms, URL routing, and view behaviors.

---

## Test Coverage

The test suite covers:

1. **Models (`test_models.py`)**:
   - Verifies that projects are created with correct default parameters.
   - Verifies category creation and associations.
   - Validates model relationships (Project -> Category -> Expense).

2. **Forms (`test_forms.py`)**:
   - Tests form validations when fields are missing or invalid (e.g. testing `ExpenseForm` with empty fields).

3. **URL Routing (`test_urls.py`)**:
   - Asserts that Django named URL routes (e.g., `list`, `detail`, `add`) resolve to the correct view functions.

4. **Views & Integration (`test_views.py`)**:
   - **GET Requests**: Asserts that `list` and `detail` pages return HTTP 200 and render the correct HTML templates (`project-list.html`, `project-detail.html`).
   - **POST Requests**: Tests adding a new expense, verifying it redirects (HTTP 302) and inserts the row into the database.
   - **Edge Cases**: Verifies view behavior when POST requests are sent with missing or empty form payloads.
   - **DELETE Requests**: Tests deleting expenses, checking status codes (HTTP 204 for success, HTTP 404 for missing IDs).

---

## Setup & Running the Tests

### Prerequisites
- Python 3.8+
- Django 3.2+

### Running Tests
To run the Django test suite, navigate to the Django root directory (`src/`) and run the standard manage script:

```bash
cd src/
python manage.py test
```

This will run all test classes in the `budget/tests/` module, outputting details of passing/failing assertions.
