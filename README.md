# Pytest API Testing Examples

A Python project containing Pytest examples and API test suites. It covers core Pytest concepts alongside tests for a local Flask API and public HTTP APIs.

## What is included

| Location | Purpose |
| --- | --- |
| `tests/` | Introductory Pytest examples: assertions, fixtures, parameterization, markers, and logging. |
| `APIFlaskAppTests/` | Tests for a locally running Flask API: registration, login, authentication, user retrieval, response status handling, and CSV-driven tests. |
| `APIPetstoreTests/` | Tests for Swagger Petstore plus an HTTP digest-auth example using httpbin. |
| `utils/` | Shared HTTP, configuration, and JSON/CSV test-data helpers. |
| `TestData/` | JSON request bodies and CSV datasets used by the Flask API tests. |
| `config/` | Target API endpoints and Flask host/port settings. |
| `py_modules/` | Small standalone examples for file, CSV, JSON, and requests operations. |

## Requirements

- Python 3.9 or newer
- `pytest`
- `requests` (used throughout the API helpers and tests)
- A local Flask API listening at `http://127.0.0.1:5000/api/` for `APIFlaskAppTests/`
- Internet access for the Petstore and httpbin tests

Install dependencies in a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install requests
```

> `requests` is imported by the project but is not currently listed in `requirements.txt`, so it is installed explicitly above.

## Configuration

The API targets are configured in the `config/` directory:

- `config/qa.ini` configures the local Flask API host and port. The default creates the base URL `http://127.0.0.1:5000/api/`.
- `config/petsqa.ini` configures Swagger Petstore endpoints.

Change these files to point the tests at a different environment. Do not commit credentials or production-only secrets to them.

## Running tests

Run all tests:

```powershell
python -m pytest
```

Run a specific suite:

```powershell
python -m pytest tests
python -m pytest APIFlaskAppTests
python -m pytest APIPetstoreTests
```

Run tests by marker:

```powershell
python -m pytest -m sanity
python -m pytest -m smoke
```

Use verbose output while learning or debugging:

```powershell
python -m pytest -v -s
```

## Test data and side effects

`APIFlaskAppTests` uses the JSON and CSV files in `TestData/`. Some of these tests create users; `test_loginAPIWithSetupTeardown.py` also removes its generated user during fixture teardown. `APIPetstoreTests` updates and deletes Petstore ID `151` and creates ID `152`. Use a disposable test environment or update those identifiers before running against a shared service.

## Logging and Pytest settings

`pytest.ini` defines the project markers and writes DEBUG-level test logs to `log/pytesting.log`. Console logging is enabled at the WARN level.

## Notes

- API helper functions currently send requests with TLS verification disabled (`verify=False`) in several places. Enable certificate verification before using the suite for production-facing environments.
- The Flask API implementation itself is not included in this repository; start a compatible service before running its tests.
