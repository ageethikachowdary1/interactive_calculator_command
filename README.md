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
The calculator runs in a **Read–Eval–Print Loop (REPL)**.

### Available Operations
- `+` → Addition  
- `-` → Subtraction  
- `*` → Multiplication  
- `/` → Division  

Type **`q`** anytime to exit.

---

## 📁 Project Structure
```
interactive_calculator_command/
│
├── src/calculator/        # Core calculator logic and REPL
├── tests/                 # Unit + parameterized tests
├── .github/workflows/     # GitHub Actions CI
├── requirements.txt       # Dependencies
├── pytest.ini             # Pytest + coverage config
├── .coveragerc            # Coverage rules
└── README.md              # Documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone <repository-url>
cd interactive_calculator_command
```

### 2️⃣ Install Python (3.10+)
Download: https://www.python.org/downloads/

Verify:
```bash
python3 --version
```

### 3️⃣ Create virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Calculator
```bash
PYTHONPATH=src python3 src/calculator/repl.py
```

---

## 🧪 Run Tests
```bash
pytest
```

### Coverage report
```bash
pytest --cov=calculator --cov-report=term-missing
```

✔ CI enforces **100% coverage**.

---

## 🤖 Continuous Integration
GitHub Actions automatically:

- installs dependencies  
- runs tests  
- verifies coverage  

on **every push and pull request**.

---

## 🔥 Useful Commands

| Task | Command |
|------|---------|
| Create venv | `python3 -m venv .venv` |
| Activate venv | `source .venv/bin/activate` |
| Install deps | `pip install -r requirements.txt` |
| Run app | `PYTHONPATH=src python3 src/calculator/repl.py` |
| Run tests | `pytest` |
| Coverage | `pytest --cov=calculator --cov-report=term-missing` |
| Push code | `git add . && git commit -m "msg" && git push` |

---

## 📚 Learning Outcomes
This project demonstrates:

- REPL-based CLI design  
- Input validation & error handling  
- Unit + parameterized testing  
- **Full test coverage**  
- CI automation with GitHub Actions  
- Clean project organization  

---

## 🔗 Resources
- Python → https://www.python.org/downloads/  
- Git → https://git-scm.com/doc  
- Pytest → https://docs.pytest.org/  
- GitHub Actions → https://docs.github.com/actions  

---

## 🧰 Tech Stack
- Python  
- pytest  
- pytest-cov  
- GitHub Actions  

---

## 📜 License
Created for **educational purposes**.
