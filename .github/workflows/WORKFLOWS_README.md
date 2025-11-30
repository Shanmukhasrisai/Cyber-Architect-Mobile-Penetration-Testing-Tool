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

## Usage

All workflows run automatically on relevant triggers. View status in the Actions tab.

## Maintenance

- Review security alerts monthly
- Update action versions quarterly
- Monitor workflow performance regularly
