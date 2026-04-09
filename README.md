# Selenium_Test_Saucedemo
This project is part of my learning journey in Quality Assurance (QA) and automation testing using Selenium with Python. In this project, I created simple automated test scripts to simulate user interactions such as login and basic navigation on a web application.

# 🧪 Selenium Automation Testing Project

This project is part of my learning journey in Quality Assurance (QA) and automation testing using Selenium WebDriver with Python.

The automation script simulates user interactions on a web application, including login, validation, and logout processes. This project focuses on building a basic understanding of automation testing and QA workflows.

---

## 🚀 Tech Stack
- Python
- Selenium WebDriver
- ChromeDriver

---

## 📌 Features
- Automated login testing
- Multiple user login scenarios
- Login validation (success & failure handling)
- Logout functionality testing
- Handling dynamic elements using explicit waits (WebDriverWait)
- Browser configuration to disable password pop-ups

---

## 🧠 What I Learned
- Basic automation testing using Selenium
- Writing reusable functions for test steps
- Handling web elements (ID, class, etc.)
- Using explicit wait for dynamic UI
- Simulating real user interactions
- Understanding basic QA workflow

---

## 🧪 Test Scenarios

### Login Testing
- ✅ Valid login with standard user
- ⚠️ Login with different user types:
  - problem_user
  - performance_glitch_user
  - error_user
  - visual_user

### Logout Testing
- Verify user can logout successfully after login

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install selenium
```
2. Download and setup ChromeDriver
Make sure the ChromeDriver version matches your Chrome browser
3. Run the script:
```
python login_saeuce.py
```
