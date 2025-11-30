# GitHub Actions Workflows Documentation

This directory contains automated workflows for the CyberMobilePenTest repository.

## Configured Workflows

### 1. Python Application CI (python-app.yml)
- **Purpose**: Continuous Integration for Python code
- **Triggers**: Push and PR to main branch
- **Actions**: Installs dependencies, runs flake8 linting, executes pytest tests
- **Benefits**: Ensures code quality and catches errors early

### 2. CodeQL Security Scanning (codeql.yml)
- **Purpose**: Advanced security vulnerability detection
- **Triggers**: Push, PR to main, weekly schedule (Wed 1:24 AM UTC)
- **Actions**: Analyzes code for security issues across multiple languages
- **Benefits**: Proactive security scanning and compliance

### 3. Dependency Review (dependency-review.yml)
- **Purpose**: Supply chain security
- **Triggers**: Pull requests to main branch
- **Actions**: Scans dependencies for known vulnerabilities
- **Benefits**: Blocks PRs with vulnerable dependencies

### 4. Docker Image Build (docker-image.yml)
- **Purpose**: Container deployment automation
- **Triggers**: Push and PR to main branch
- **Actions**: Builds and tags Docker images
- **Benefits**: Automated containerization for deployment

### 5. File Overflow Protection (file-overflow.yml)
- **Purpose**: Prevent file handling errors and overflow issues
- **Triggers**: Push and PR to main branch
- **Actions**: Validates file sizes and handles edge cases
- **Benefits**: Prevents crashes from malformed or oversized files

## Essential Commands for Running CyberMobilePenTest

### Setup and Installation
```bash
# Clone the repository
git clone https://github.com/Shanmukhasrisai/CyberMobilePenTest.git
cd CyberMobilePenTest

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Tools
```bash
# Run the main penetration testing suite
python mobile_pentest_suite.py

# Run the advanced framework
python advanced_mobile_pentest_framework.py

# Run automated vulnerability scanner
python automated_vulnerability_scanner.py

# Launch the dashboard interface
python dashboard_interface.py
```

### Security Scanning Commands
```bash
# Run Bandit security scanner (identifies security issues in Python code)
pip install bandit
bandit -r . -f json -o bandit_report.json
bandit -r . -ll  # Show only medium and high severity issues

# Run Safety check (checks dependencies for known vulnerabilities)
pip install safety
safety check --json --output safety_report.json
safety check --full-report

# Run code linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### Testing and Coverage
```bash
# Run tests with pytest
pytest tests/ -v

# Run tests with coverage report
pip install pytest-cov
pytest --cov=. --cov-report=html --cov-report=term
pytest --cov=. --cov-report=xml --cov-report=term-missing

# View coverage report
open htmlcov/index.html  # On macOS
xdg-open htmlcov/index.html  # On Linux
start htmlcov/index.html  # On Windows
```

### Cleanup and Maintenance
```bash
# Remove Python cache files
find . -type d -name '__pycache__' -exec rm -rf {} +
find . -type f -name '*.pyc' -delete
find . -type f -name '*.pyo' -delete

# Remove test and coverage artifacts
rm -rf .pytest_cache/ htmlcov/ .coverage coverage.xml

# Clean up temporary files
rm -rf *.log *.tmp tmp/ temp/

# Remove build artifacts
rm -rf build/ dist/ *.egg-info/
```

### Docker Operations
```bash
# Build Docker image
docker build -t cybermobilepentest:latest .

# Run container
docker run -it --rm cybermobilepentest:latest

# Run with volume mount for persistent data
docker run -it --rm -v $(pwd)/data:/app/data cybermobilepentest:latest
```

## Best Practices for GitHub Actions

### Security Best Practices
1. **Pin Action Versions**: Always use specific commit SHAs or version tags
   ```yaml
   - uses: actions/checkout@v4.1.0  # Good
   - uses: actions/checkout@abc123  # Better (commit SHA)
   ```

2. **Minimize Permissions**: Use least privilege principle
   ```yaml
   permissions:
     contents: read
     security-events: write
   ```

3. **Use Secrets Securely**: Never hardcode credentials
   ```yaml
   - name: Deploy
     env:
       API_KEY: ${{ secrets.API_KEY }}
   ```

4. **Enable Dependabot**: Keep actions and dependencies up-to-date
   - Create `.github/dependabot.yml`
   - Configure automatic security updates

5. **Scan for Vulnerabilities**: Integrate security tools in CI/CD
   - CodeQL for code analysis
   - Bandit for Python security issues
   - Safety for dependency vulnerabilities
   - Trivy for container scanning

### Performance Optimization
1. **Cache Dependencies**: Speed up workflow runs
   ```yaml
   - name: Cache pip packages
     uses: actions/cache@v3
     with:
       path: ~/.cache/pip
       key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
   ```

2. **Parallel Jobs**: Run independent tasks concurrently
   ```yaml
   jobs:
     lint:
       runs-on: ubuntu-latest
     test:
       runs-on: ubuntu-latest
   ```

3. **Conditional Execution**: Skip unnecessary steps
   ```yaml
   - name: Deploy
     if: github.ref == 'refs/heads/main' && github.event_name == 'push'
   ```

### Error Handling and Reliability
1. **Timeout Protection**: Prevent hung workflows
   ```yaml
   jobs:
     build:
       timeout-minutes: 30
   ```

2. **Retry on Failure**: Handle transient issues
   ```yaml
   - name: Flaky test
     uses: nick-invision/retry@v2
     with:
       timeout_minutes: 10
       max_attempts: 3
   ```

3. **Continue on Error**: Don't fail entire workflow for non-critical steps
   ```yaml
   - name: Optional step
     continue-on-error: true
   ```

### Artifact Management
1. **Upload Test Results**: Preserve important data
   ```yaml
   - name: Upload coverage reports
     uses: actions/upload-artifact@v3
     with:
       name: coverage-report
       path: htmlcov/
       retention-days: 30
   ```

2. **Download Artifacts**: Use results from previous jobs
   ```yaml
   - name: Download artifacts
     uses: actions/download-artifact@v3
     with:
       name: coverage-report
   ```

## Workflow Troubleshooting

### Common Issues and Solutions

1. **Workflow not triggering**
   - Check trigger conditions (branches, paths)
   - Verify workflow file syntax
   - Ensure workflow is enabled in repository settings

2. **Permission errors**
   - Add required permissions to workflow
   - Check repository settings for action permissions
   - Verify secrets are properly configured

3. **Dependency installation failures**
   - Pin dependency versions in requirements.txt
   - Use caching to speed up and stabilize builds
   - Check for conflicting dependencies

4. **Test failures**
   - Review test logs in Actions tab
   - Run tests locally to reproduce
   - Check for environment-specific issues

5. **Timeout issues**
   - Increase timeout limits if justified
   - Optimize slow tests
   - Use matrix strategy to parallelize

## Monitoring and Maintenance

### Regular Tasks
- **Weekly**: Review failed workflows and fix issues
- **Monthly**: Check security alerts and update dependencies
- **Quarterly**: Update action versions and review workflow efficiency
- **Annually**: Audit permissions and security configurations

### Metrics to Monitor
- Workflow success rate
- Average execution time
- Security vulnerabilities detected
- Code coverage trends
- Dependency freshness

## Integration with CI/CD Pipeline

### Pre-commit Hooks
Consider adding pre-commit hooks for local validation:
```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
pre-commit install

# Run manually
pre-commit run --all-files
```

### Branch Protection Rules
Recommended settings:
- Require status checks to pass before merging
- Require branches to be up to date before merging
- Require review from code owners
- Dismiss stale pull request approvals
- Restrict who can push to matching branches

## Additional Resources
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Security Hardening Guide](https://docs.github.com/actions/security-guides/security-hardening-for-github-actions)
- [Workflow Syntax Reference](https://docs.github.com/actions/reference/workflow-syntax-for-github-actions)
- [OWASP Mobile Security Testing Guide](https://owasp.org/www-project-mobile-security-testing-guide/)

## Support
For issues or questions:
- Open an issue in the repository
- Check existing documentation
- Review workflow logs in Actions tab
