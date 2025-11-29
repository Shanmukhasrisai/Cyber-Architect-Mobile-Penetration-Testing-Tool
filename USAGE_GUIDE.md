# CyberMobilePenTest Usage Guide

## Table of Contents

1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Advanced Scanning](#advanced-scanning)
4. [API Testing](#api-testing)
5. [Reporting](#reporting)
6. [Compliance Testing](#compliance-testing)
7. [DevSecOps Integration](#devsecops-integration)
8. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment support

### Step-by-Step Installation

```bash
# Clone the repository
git clone https://github.com/Shanmukhasrisai/CyberMobilePenTest.git
cd CyberMobilePenTest

# Create virtual environment
python3 -m venv cmp-env
source cmp-env/bin/activate  # On Windows: cmp-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the tool
python mobile_pentest_suite.py --init
```

## Basic Usage

### 1. Quick Vulnerability Scan

Perform a basic security scan on a mobile application:

```bash
python mobile_pentest_suite.py --target com.example.app --scan-type quick
```

**Options:**

- `--target`: Application package name or path to APK/IPA
- `--scan-type`: `quick`, `standard`, or `comprehensive`

### 2. Basic API Test

Test a mobile application API endpoint:

```bash
python mobile_pentest_suite.py --api-target https://api.example.com --test-endpoints
```

### 3. Generate a Quick Report

Create a security report after a scan:

```bash
python mobile_pentest_suite.py --target com.example.app --report pdf
```

## Advanced Scanning

### Run Comprehensive Scan

```bash
python advanced_mobile_pentest_framework.py \
  --target com.example.app \
  --scan-level comprehensive \
  --enable-sast \
  --enable-dast \
  --enable-api-testing
```

### Specify Compliance Frameworks

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance "OWASP,GDPR,PCI-DSS"
```

### Use Custom Configuration

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --config custom_config.yaml
```

## API Testing

### Test REST API Endpoints

```bash
python mobile_pentest_suite.py \
  --api-target https://api.example.com \
  --auth-token YOUR_BEARER_TOKEN \
  --test-endpoints \
  --output json
```

### Advanced API Testing with Custom Headers

```bash
python advanced_mobile_pentest_framework.py \
  --api-target https://api.example.com \
  --headers "Authorization: Bearer TOKEN" \
  --test-injection-attacks \
  --test-rate-limiting
```

### Test GraphQL Endpoints

```bash
python mobile_pentest_suite.py \
  --graphql-endpoint https://api.example.com/graphql \
  --introspection-test \
  --query-test
```

## Reporting

### Generate PDF Report

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --report pdf \
  --output-dir ./reports
```

### Generate HTML Report

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --report html \
  --output-dir ./reports
```

### Export JSON for CI/CD Integration

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --output json \
  --output-file scan_results.json
```

## Compliance Testing

### OWASP Mobile Top 10 Compliance Check

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance OWASP_MOBILE_TOP_10
```

### GDPR Compliance Assessment

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance GDPR \
  --privacy-check
```

### PCI-DSS Compliance Validation

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance PCI_DSS \
  --payment-check
```

## DevSecOps Integration

### Jenkins Pipeline Integration

```bash
#!/bin/bash
# Run CyberMobilePenTest in CI pipeline
python mobile_pentest_suite.py \
  --target $APP_PACKAGE_NAME \
  --output json \
  --output-file results.json

# Check results and fail if critical vulnerabilities found
python -c "import json; results=json.load(open('results.json')); \
  exit(1 if any(v['severity']=='critical' for v in results['vulnerabilities']) else 0)"
```

### GitHub Actions Integration

```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run CyberMobilePenTest
        run: |
          python mobile_pentest_suite.py \
            --target com.example.app \
            --output json \
            --output-file results.json
      - name: Upload results
        uses: actions/upload-artifact@v2
        with:
          name: security-reports
          path: results.json
```

### GitLab CI Integration

```yaml
security_scan:
  stage: test
  script:
    - python mobile_pentest_suite.py --target $APP_NAME --output json
  artifacts:
    reports:
      security: scan_results.json
```

## Dashboard Interface

### Launch Web Dashboard

```bash
python dashboard_interface.py --port 5000
```

Access the dashboard at: `http://localhost:5000`

### Dashboard Features

- Real-time scan monitoring
- Vulnerability analytics
- Compliance status overview
- Historical trend analysis
- Custom report generation

## Logging and Debugging

### Check Scan Logs

```bash
tail -f logs/cybermobilepentest.log
```

### Enable Debug Mode

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --debug \
  --log-level DEBUG
```

### View Application Logs

```bash
cat logs/cybermobilepentest.log | grep ERROR
```

## Troubleshooting

### Issue: Module not found error

**Solution:**

```bash
# Ensure you're in the correct virtual environment
source cmp-env/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: Permission denied error

**Solution:**

```bash
# Grant execute permissions
chmod +x mobile_pentest_suite.py
chmod +x advanced_mobile_pentest_framework.py
```

### Issue: Port already in use (for dashboard)

**Solution:**

```bash
# Use a different port
python dashboard_interface.py --port 5001
```

### Issue: API authentication fails

**Solution:**

```bash
# Verify your authentication token
python mobile_pentest_suite.py \
  --api-target https://api.example.com \
  --auth-type bearer \
  --auth-token YOUR_TOKEN \
  --verify-auth
```

### Issue: Scan timeout

**Solution:**

```bash
# Increase timeout and adjust scan parameters
python mobile_pentest_suite.py \
  --target com.example.app \
  --timeout 300 \
  --scan-type quick
```

## Common Commands

```bash
# List available scan types
python mobile_pentest_suite.py --help

# Run scan and save results
python mobile_pentest_suite.py --target com.example.app --output json

# View scan results
cat results.json | jq

# Generate multiple report formats
python mobile_pentest_suite.py --target com.example.app --report pdf,html,json
```

## Getting Help

- **Documentation:** [CyberMobilePenTest Docs](./docs/)
- **Issues:** [GitHub Issues](https://github.com/Shanmukhasrisai/CyberMobilePenTest/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Shanmukhasrisai/CyberMobilePenTest/discussions)
- **Email:** security@cybermobilepentest.dev

---

**CyberMobilePenTest** - Enterprise Mobile Penetration Testing Suite
