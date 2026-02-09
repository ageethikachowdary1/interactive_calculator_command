# Interactive Command-Line Calculator

## 📌 Project Overview
This project is a clean **Python command-line calculator** demonstrating:

- Git version control  
- Virtual environments  
- REPL-based interaction  
- Unit testing with **pytest**  
- **100% test coverage**  
- Continuous Integration using **GitHub Actions**

---

## 🔁 REPL Interface
The calculator runs in a **Read-Eval-Print Loop**.

### Available Operations
- `+` → Addition  
- `-` → Subtraction  
- `*` → Multiplication  
- `/` → Division  

Type **`q`** anytime to exit.

Project Structure
interactive_calculator_command/
│
├── src/calculator/ Core calculator logic and REPL interface
├── tests/ Unit and parameterized pytest tests
├── .github/workflows/ GitHub Actions CI configuration
├── requirements.txt Python dependencies
├── pytest.ini Pytest configuration with coverage enforcement
├── .coveragerc Coverage configuration
└── README.md Project documentation
Setup Instructions
Clone the repository
git clone <repository-url>
cd interactive_calculator_command
Install Python 3.10 or higher
Download from: https://www.python.org/downloads/
Check installation:
python3 --version
Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate (Mac/Linux)
Install dependencies:
pip install -r requirements.txt
Running the Calculator
PYTHONPATH=src python3 src/calculator/repl.py
Running Tests
pytest
Check coverage report
pytest --cov=calculator --cov-report=term-missing
The project enforces 100% test coverage.
CI will fail automatically if coverage drops below 100%.
Continuous Integration
GitHub Actions automatically installs dependencies, runs tests, and verifies full coverage on every push and pull request.
This ensures the project always remains stable and fully tested.
Useful Commands Cheat Sheet
Create virtual environment
python3 -m venv .venv
Activate environment
source .venv/bin/activate
Install dependencies
pip install -r requirements.txt
Run calculator
PYTHONPATH=src python3 src/calculator/repl.py
Run tests
pytest
Check coverage
pytest --cov=calculator --cov-report=term-missing
Push code
git add . && git commit -m "message" && git push
Key Learning Outcomes
This project demonstrates:
Command-line Python application design
REPL implementation
Input validation and error handling
Unit and parameterized testing with pytest
Achieving complete test coverage
Automated CI testing with GitHub Actions
Clean project organization and documentation
Useful Resources
Python Downloads: https://www.python.org/downloads/
Git Documentation: https://git-scm.com/doc
Pytest Documentation: https://docs.pytest.org/
GitHub Actions: https://docs.github.com/actions
GitHub SSH Guide: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
Author
Geethika
Technology Stack
Language: Python
Testing: pytest
Coverage: pytest-cov
CI/CD: GitHub Actions
License
This project is created for educational purposes as part of coursework.
