# Cyber-Architect Usage Guide

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
git clone https://github.com/Shanmukhasrisai/Cyber-Architect-Mobile-Penetration-Testing-Tool.git
cd Cyber-Architect-Mobile-Penetration-Testing-Tool

# Create virtual environment
python3 -m venv ca-env
source ca-env/bin/activate  # On Windows: ca-env\Scripts\activate

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
- `--platform`: `android`, `ios`, or `auto` (default)

### 2. Standard Security Assessment

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --scan-type standard \
  --output-format json \
  --report-file assessment_2025.json
```

### 3. Comprehensive Penetration Test

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --scan-type comprehensive \
  --deep-analysis true \
  --timeout 600 \
  --output-dir ./reports/
```

## Advanced Scanning

### Custom Vulnerability Scanning

```python
from automated_vulnerability_scanner import VulnerabilityScanner

scanner = VulnerabilityScanner()
results = scanner.scan(
    target='com.example.app',
    plugins=['authentication', 'cryptography', 'storage'],
    severity_threshold='medium'
)

for vulnerability in results.vulnerabilities:
    print(f"{vulnerability.type}: {vulnerability.severity}")
```

### Targeted Testing Modules

#### Storage Vulnerability Testing
```bash
python advanced_mobile_pentest_framework.py \
  --target com.example.app \
  --module storage \
  --check-sqlite true \
  --check-preferences true \
  --check-files true
```

#### Communication Security Testing
```bash
python advanced_mobile_pentest_framework.py \
  --target com.example.app \
  --module communication \
  --intercept-ssl true \
  --check-certificates true \
  --validate-tls-version true
```

#### Cryptography Analysis
```bash
python advanced_mobile_pentest_framework.py \
  --target com.example.app \
  --module cryptography \
  --check-algorithms true \
  --validate-key-strength true \
  --detect-hardcoded-keys true
```

## API Testing

### Basic API Security Assessment

```bash
python advanced_mobile_pentest_framework.py \
  --api-url https://api.example.com \
  --api-type rest \
  --basic-auth username:password
```

### Advanced API Testing

```bash
python advanced_mobile_pentest_framework.py \
  --api-url https://api.example.com \
  --api-type rest \
  --bearer-token <token> \
  --test-authentication true \
  --test-authorization true \
  --test-rate-limiting true \
  --test-injection true \
  --fuzz-parameters true
```

### GraphQL API Testing

```bash
python advanced_mobile_pentest_framework.py \
  --api-url https://api.example.com/graphql \
  --api-type graphql \
  --introspection-check true \
  --query-complexity-check true \
  --depth-limiting-check true
```

### Testing Specific Endpoints

```bash
python advanced_mobile_pentest_framework.py \
  --api-url https://api.example.com \
  --endpoints-file endpoints.json \
  --test-timeout 30 \
  --parallel-requests 10
```

**Sample endpoints.json:**
```json
{
  "endpoints": [
    {
      "method": "GET",
      "path": "/api/v1/users",
      "auth_required": true
    },
    {
      "method": "POST",
      "path": "/api/v1/users",
      "auth_required": false,
      "sensitive": true
    }
  ]
}
```

## Reporting

### Generate Standard Report

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --report-format pdf \
  --output-file assessment_report.pdf
```

### Generate Executive Summary

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --report-type executive \
  --output-format html \
  --branding-logo ./logo.png
```

### Generate Technical Report with Remediation

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --report-type technical \
  --include-remediation true \
  --remediation-priority true \
  --output-format pdf
```

### Multiple Format Export

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --export-formats pdf,html,json,csv \
  --output-dir ./reports/
```

### Webhook Notification

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --webhook-url https://slack.example.com/webhook \
  --webhook-format slack \
  --notify-on-completion true
```

## Compliance Testing

### OWASP Mobile Top 10 Compliance

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance-framework owasp-mobile \
  --report-format pdf \
  --output-file owasp_assessment.pdf
```

### GDPR Compliance Check

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance-framework gdpr \
  --check-data-protection true \
  --check-consent-management true \
  --check-privacy-controls true
```

### PCI-DSS Compliance Assessment

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance-framework pci-dss \
  --check-payment-security true \
  --check-encryption true \
  --check-access-controls true
```

### Multi-Framework Compliance Report

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --compliance-frameworks owasp-mobile,gdpr,pci-dss,iso-27001 \
  --generate-gap-analysis true \
  --output-format html
```

## DevSecOps Integration

### CI/CD Pipeline Integration

#### GitHub Actions

```yaml
name: Mobile Security Scan
on: [push, pull_request]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Cyber-Architect Scan
        run: |
          python mobile_pentest_suite.py \
            --target ./app.apk \
            --ci-mode true \
            --fail-on-severity critical \
            --output-format sarif \
            --output-file results.sarif
      
      - name: Upload SARIF Report
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: results.sarif
```

#### GitLab CI

```yaml
mobile-security-scan:
  image: python:3.9
  script:
    - pip install -r requirements.txt
    - python mobile_pentest_suite.py \
        --target $CI_PROJECT_DIR/app.apk \
        --ci-mode true \
        --fail-on-severity high \
        --output-format json \
        --output-file scan_results.json
  artifacts:
    reports:
      dependency_scanning: scan_results.json
```

#### Jenkins

```groovy
stage('Security Scan') {
    steps {
        sh '''
            python mobile_pentest_suite.py \
              --target ./app.apk \
              --ci-mode true \
              --fail-on-severity high \
              --output-format json \
              --output-file ${WORKSPACE}/scan_results.json
        '''
    }
    post {
        always {
            publishHTML([
                reportDir: './',
                reportFiles: 'scan_results.json',
                reportName: 'Security Scan Report'
            ])
        }
    }
}
```

### SAST Integration

```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --ci-mode true \
  --fail-on-severity high,critical \
  --output-format sarif,json \
  --report-file scan_results
```

## Troubleshooting

### Issue: Connection Timeout

**Problem**: Scan fails with connection timeout error.

**Solution**:
```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --timeout 120 \
  --retry-count 3
```

### Issue: Permission Denied

**Problem**: "Permission denied" error during scan.

**Solution**:
```bash
# On Linux/macOS
sudo chmod +x mobile_pentest_suite.py

# Or run with proper permissions
python mobile_pentest_suite.py --target com.example.app
```

### Issue: Memory Issues

**Problem**: "Out of memory" errors during comprehensive scans.

**Solution**:
```bash
# Increase available memory
export PYTHONHASHSEED=0
python -X dev mobile_pentest_suite.py \
  --target com.example.app \
  --memory-limit 4096
```

### Issue: API Connection Failed

**Problem**: Cannot connect to API endpoint.

**Solution**:
```bash
# Verify connectivity
curl -v https://api.example.com/health

# Run scan with verbose logging
python advanced_mobile_pentest_framework.py \
  --api-url https://api.example.com \
  --verbose true \
  --debug true
```

### Viewing Logs

```bash
# Real-time log viewing
tail -f logs/cyber-architect.log

# Search for errors
grep ERROR logs/cyber-architect.log

# Export logs for analysis
cp logs/cyber-architect.log scan_logs_backup.log
```

## Best Practices

1. **Always use isolated test environments** - Never scan production systems without authorization
2. **Maintain updated CVE database** - Run `--update-cve-db` regularly
3. **Document scan parameters** - Keep records of test configurations
4. **Review reports carefully** - Validate findings before remediation
5. **Test remediation** - Verify fixes don't introduce new issues
6. **Schedule regular assessments** - Conduct periodic security reviews
7. **Secure credentials** - Use environment variables or credential managers

## Performance Optimization

### Parallel Scanning
```bash
python mobile_pentest_suite.py \
  --target com.example.app \
  --parallel-workers 4 \
  --scan-type comprehensive
```

### Cache Management
```bash
# Clear cache
python mobile_pentest_suite.py --clear-cache

# Disable caching
python mobile_pentest_suite.py --cache-disabled true
```

## Support & Resources

- **Documentation**: [Full Docs](https://github.com/Shanmukhasrisai/Cyber-Architect-Mobile-Penetration-Testing-Tool/wiki)
- **Issues**: [Report Problems](https://github.com/Shanmukhasrisai/Cyber-Architect-Mobile-Penetration-Testing-Tool/issues)
- **Security**: [Report Vulnerabilities](./SECURITY.md)

---

For additional support and examples, visit the [GitHub Wiki](https://github.com/Shanmukhasrisai/Cyber-Architect-Mobile-Penetration-Testing-Tool/wiki).
