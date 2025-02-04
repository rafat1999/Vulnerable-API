# Vulnerable API for Learning

## Introduction
This project is a **deliberately vulnerable API** designed for students to learn about common web vulnerabilities such as:
- **NoSQL Injection**
- **Insecure Direct Object References (IDOR)**
- **Cross-Site Scripting (XSS)**
- **Cross-Site Request Forgery (CSRF)**
- **Code Injection**
- **Server-Side Template Injection (SSTI)**

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/vulnerable-api.git
cd vulnerable-api
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

## API Endpoints
| Endpoint       | Vulnerability Type |
|---------------|-------------------|
| `/nosql`      | NoSQL Injection   |
| `/idor`       | IDOR              |
| `/xss`        | XSS               |
| `/csrf`       | CSRF              |
| `/code_injection` | Code Injection |
| `/ssti`       | SSTI              |

## Warning
This project is **for educational purposes only**. Do **not** deploy it in a production environment.

## License
MIT License. Feel free to use and modify for learning purposes.
