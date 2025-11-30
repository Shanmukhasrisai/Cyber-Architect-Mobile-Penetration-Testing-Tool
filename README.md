# CyberMobilePenTest
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OWASP Compliant](https://img.shields.io/badge/OWASP-Compliant-green.svg)](https://owasp.org/)
[![Security Testing](https://img.shields.io/badge/Security-Tested-brightgreen.svg)](https://owasp.org/www-project-mobile-security-testing-guide/)

## Overview

CyberMobilePenTest is an enterprise-grade mobile penetration testing suite designed for security professionals, architects, and DevSecOps teams. It provides automated vulnerability scanning, comprehensive API testing, and detailed reporting capabilities aligned with industry standards including OWASP, GDPR, and PCI-DSS.

This tool is built for scalability, modularity, and integration into modern DevSecOps pipelines, with features suitable for both on-premise and cloud-based deployments.

## Key Features

### Core Capabilities

- **Automated Vulnerability Scanning**: Comprehensive detection of common mobile security vulnerabilities
- **API Penetration Testing**: In-depth REST/GraphQL API security assessment
- **Mobile Security Testing**: OWASP Mobile Top 10 and MASVS framework compliance
- **CVE Correlation**: Real-time database integration for vulnerability identification
- **Enterprise Reporting**: Detailed, compliance-ready security reports

### Professional Features

- **Modular Architecture**: Extensible plugin system for custom security tests
- **DevSecOps Integration**: CI/CD pipeline integration support
- **Compliance Frameworks**: OWASP, GDPR, PCI-DSS, and ISO 27001 compliance checks
- **Multi-tenant Support**: Suitable for MSP and enterprise deployments

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space
- Internet connection for CVE database updates

## Installation

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/Shanmukhasrisai/CyberMobilePenTest.git

# Navigate to the project directory
cd CyberMobilePenTest

# Install dependencies
pip install -r requirements.txt

# Verify installation
python cyber_mobile_pentest.py --version
```

### Docker Installation (Recommended for Production)

```bash
# Pull the Docker image
docker pull shanmukhasrisai/cybermobilepentest:latest

# Run the container
docker run -v $(pwd)/reports:/app/reports shanmukhasrisai/cybermobilepentest:latest
```

## Quick Start

### Basic Scan

```bash
python cyber_mobile_pentest.py --scan --target your_app.apk
```

### API Security Testing

```bash
python cyber_mobile_pentest.py --api-test --url https://api.example.com --endpoints config/endpoints.json
```

### Generate Report

```bash
python cyber_mobile_pentest.py --report --format pdf --output-dir ./reports
```

### Accessing and Downloading Reports

After running scans, CyberMobilePenTest automatically generates comprehensive security reports that can be accessed and downloaded in multiple ways:

#### Report Locations

**Default Location**: All reports are saved to the `./reports` directory in your project root by default.

**Custom Location**: Specify a custom output directory using the `--output-dir` flag:
```bash
python cyber_mobile_pentest.py --report --format pdf --output-dir /path/to/custom/reports
```

#### Report Formats and File Names

Reports are generated in your chosen format with timestamped filenames for easy identification:

- **PDF Reports**: `scan_report_YYYY-MM-DD_HH-MM-SS.pdf`
- **HTML Reports**: `scan_report_YYYY-MM-DD_HH-MM-SS.html`
- **JSON Reports**: `scan_report_YYYY-MM-DD_HH-MM-SS.json`
- **XML Reports**: `scan_report_YYYY-MM-DD_HH-MM-SS.xml`

#### How to Download Reports

**Local Installation**:
1. Navigate to the reports directory: `cd reports`
2. List available reports: `ls -la`
3. Copy or move reports to your desired location: `cp scan_report_*.pdf ~/Documents/`

**Docker Installation**:
Reports are automatically mounted to your host machine via volume mapping:
```bash
# Reports are available in the current directory's reports folder
ls -la ./reports/
```

**CI/CD Pipeline Integration**:
Use the `--output-dir` flag to specify your CI/CD artifact directory:
```bash
python cyber_mobile_pentest.py --report --format pdf --output-dir $CI_ARTIFACTS_DIR
```

#### Report Contents

Each report includes:
- Executive summary with risk ratings
- Detailed vulnerability findings with CVE mappings
- OWASP Mobile Top 10 compliance matrix
- Remediation recommendations
- Technical details and proof of concepts
- Compliance framework mappings (GDPR, PCI-DSS, ISO 27001)

#### Accessing Reports Programmatically

You can also access report data programmatically using the API:

```python
from cyber_mobile_pentest import ReportManager

# Initialize report manager
report_mgr = ReportManager()

# List all available reports
reports = report_mgr.list_reports('./reports')

# Load a specific report
report_data = report_mgr.load_report('scan_report_2025-11-30_14-30-00.json')

# Export to different format
report_mgr.export(report_data, format='pdf', output='custom_report.pdf')
```

#### Report Retention and Management

- Reports are stored indefinitely unless manually deleted
- Implement automated cleanup for old reports:
  ```bash
  # Delete reports older than 30 days
  find ./reports -name "scan_report_*.pdf" -mtime +30 -delete
  ```
- Archive important reports to a secure location
- Use version control for report tracking in enterprise environments

## Configuration

### Configuration File

Create a `config.yaml` file in the project root:

```yaml
scan_settings:
  depth: deep
  timeout: 300
  threads: 4
  
reporting:
  default_format: pdf
  output_directory: ./reports
  include_screenshots: true
  
api_testing:
  rate_limit: 10
  authentication:
    type: bearer
    token_file: ./tokens/api_token.txt
```

## Advanced Usage

### Custom Security Tests

```python
from cyber_mobile_pentest.plugins import SecurityTestPlugin

class CustomTest(SecurityTestPlugin):
    def run(self, target):
        # Your custom test logic
        pass
```

### Integration with CI/CD

#### GitHub Actions Example

```yaml
name: Mobile Security Scan
on: [push]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run CyberMobilePenTest
        run: |
          python cyber_mobile_pentest.py --scan --target app.apk
          python cyber_mobile_pentest.py --report --format json
```

## Compliance and Standards

### Supported Frameworks

- **OWASP Mobile Top 10**: Complete coverage of mobile security risks
- **MASVS**: Mobile Application Security Verification Standard
- **GDPR**: Data protection and privacy compliance checks
- **PCI-DSS**: Payment card industry security requirements
- **ISO 27001**: Information security management

## Troubleshooting

### Common Issues

**Issue**: Module not found error
```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Issue**: Permission denied on report generation
```bash
# Solution: Check directory permissions
chmod 755 ./reports
```

## Roadmap

- [ ] Machine learning-based vulnerability prediction
- [ ] Cloud platform integration (AWS, Azure, GCP)
- [ ] Real-time collaborative testing dashboard
- [ ] Mobile device farm integration
- [ ] Enhanced SAST/DAST capabilities

⚠️ **IMPORTANT**: This tool is intended for authorized security testing only.

- Only use on applications and systems you own or have explicit written permission to test
- Unauthorized testing may be illegal in your jurisdiction
- Users are responsible for complying with all applicable laws and regulations
- The authors assume no liability for misuse or damage caused by this tool

## Contributing

We welcome contributions from security researchers and developers. Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/Shanmukhasrisai/CyberMobilePenTest.git
cd CyberMobilePenTest
pip install -r requirements-dev.txt
python -m pytest tests/
```

## License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

## Support & Contact

- **Issues**: [GitHub Issues](https://github.com/Shanmukhasrisai/CyberMobilePenTest/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Shanmukhasrisai/CyberMobilePenTest/discussions)
- **Documentation**: [Wiki](https://github.com/Shanmukhasrisai/CyberMobilePenTest/wiki)

## Acknowledgments

- OWASP Mobile Security Testing Guide
- NIST Mobile Application Security
- Security research community
