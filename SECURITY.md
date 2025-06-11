# Security Policy

## Supported Versions

We provide security updates for the following versions of InstaSwarm:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

The InstaSwarm team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### How to Report a Security Vulnerability

If you believe you have found a security vulnerability in InstaSwarm, please report it to us through coordinated disclosure.

**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

Instead, please send an email to yashabalam707@gmail.com with the following information:

- Type of issue (e.g. buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

This information will help us triage your report more quickly.

### What to Expect

After you submit a report, we will:

1. Acknowledge receipt of your vulnerability report within 48 hours
2. Provide an estimated timeline for when we expect to resolve the vulnerability
3. Notify you when the vulnerability is fixed

## Security Best Practices for Users

### Account Security
- Use strong, unique passwords for your Instagram accounts
- Enable two-factor authentication on your Instagram accounts
- Regularly rotate account credentials
- Use dedicated test accounts for development and testing

### Proxy Security
- Use reputable proxy services
- Avoid free or untrusted proxy services
- Regularly update proxy credentials
- Monitor proxy usage for suspicious activity

### Environment Security
- Keep your Python environment updated
- Use virtual environments to isolate dependencies
- Regularly update the `instagrapi` library and other dependencies
- Monitor logs for suspicious activity

### Data Protection
- Never commit credentials to version control
- Use environment variables for sensitive configuration
- Secure your `accounts.txt` and log files
- Regularly clean up old log files

## Responsible Disclosure

We appreciate the security research community and believe that responsible disclosure of security vulnerabilities helps us ensure the security and privacy of all our users.

### Guidelines for Security Researchers

- Please give us reasonable time to investigate and mitigate an issue before making any information public
- Do not exploit a vulnerability you discover for any reason
- Do not access accounts or data that does not belong to you
- Do not perform testing on accounts you do not own or have explicit permission to test
- Be respectful to Instagram's infrastructure and other users

## Security Features

InstaSwarm includes several security features:

- **Proxy Support**: Route traffic through proxies to protect IP addresses
- **Rate Limiting**: Built-in delays to prevent triggering Instagram's anti-spam measures
- **Error Handling**: Graceful handling of authentication failures and network issues
- **Logging**: Comprehensive logging for security monitoring and auditing

## Known Security Considerations

### Instagram's Anti-Automation Measures
- Instagram actively detects and prevents automated behavior
- Accounts may be temporarily or permanently restricted for automation
- Use realistic delays and human-like behavior patterns

### Legal and Ethical Considerations
- Ensure compliance with Instagram's Terms of Service
- Respect other users' privacy and content
- Use automation responsibly and ethically

## Security Updates

Security updates will be released as needed and announced through:
- GitHub releases
- Security advisories on GitHub
- ZehraSec social media channels

Stay informed about security updates by watching this repository and following ZehraSec on social media.

## Contact

For security-related questions or concerns, contact:
- Email: yashabalam707@gmail.com
- Website: https://zehrasec.com

For general support:
- GitHub Issues: For non-security related bugs and feature requests
- Social Media: Follow @zehrasec for updates and announcements
