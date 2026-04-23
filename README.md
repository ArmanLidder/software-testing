# Software Testing Portfolio

This repository is a consolidated suite of testing projects, covering both **functional unit/integration testing** of web applications and **non-functional performance/load testing** of REST APIs.

---

## Suite Components

The portfolio is split into two specialized testing suites:

### 1. [Django Web Application Functional Testing](./django-app-testing)
A functional testing workspace validating the business logic of a Python-based web app.
* **Scope**: Tests models, validation forms, URL routes, and view integrations.
* **Assertions**: Focuses on GET/POST view routing, database row creation, form failure states, and view deletions.
* **Framework**: Uses Django's built-in testing framework (built on top of Python's `unittest` library).

### 2. [API Load Testing & Markov User Simulation](./api-load-testing-locust)
A performance testing workspace designed to stress-test a FastAPI backend.
* **Server**: A REST API built with FastAPI and SQLite.
* **Log Parsing**: Parses access logs to calculate a **Markov Chain transition probability matrix** representing actual user click paths.
* **Load Simulation**: Uses **Locust** to simulate concurrent users whose page transition paths dynamically follow the generated Markov probabilities.

---

## Directory Structure

```
portfolio/
├── django-app-testing/          # Functional unit/integration tests (Django)
└── api-load-testing-locust/     # Load and concurrency tests (FastAPI + Locust)
```
*Each directory contains its own source code, configurations, execution instructions, and local documentation.*

---

## Academic Context
These projects were originally written as part of the **LOG3430 (Intégration et test des applications logicielles)** course at **Polytechnique Montréal**. The final load testing performance report is available at [api-load-testing-locust/docs/report.pdf](api-load-testing-locust/docs/report.pdf).
