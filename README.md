# InstaSwarm 🤖

A powerful multi-account Instagram automation bot built by ZehraSec that enables automated interactions across multiple Instagram accounts with advanced proxy support.

```
██╗███╗   ██╗███████╗████████╗ █████╗ ███████╗██╗    ██╗ █████╗ ██████╗ ███╗   ███╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║    ██║██╔══██╗██╔══██╗████╗ ████║
██║██╔██╗ ██║███████╗   ██║   ███████║███████╗██║ █╗ ██║███████║██████╔╝██╔████╔██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║╚════██║██║███╗██║██╔══██║██╔══██╗██║╚██╔╝██║
██║██║ ╚████║███████║   ██║   ██║  ██║███████║╚███╔███╔╝██║  ██║██║  ██║██║ ╚═╝ ██║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
      🤖
      ["InstaSwarm"]
      .-"""-.
     / .===. \
     \/ 6 6 \/
     ( \___/ )
 ___ooo__V__ooo___
     ⚙️ InstaSwarm by ZehraSec | Multi-account IG Bot
```

## ⚡ Features

- 🔥 **Multi-Account Support**: Manage multiple Instagram accounts simultaneously
- 🌐 **Advanced Proxy Support**: HTTP(S), SOCKS4, and SOCKS5 proxy compatibility
- 🎯 **Automated Actions**: Like, comment, follow, and auto-reply to comments
- 📊 **Comprehensive Logging**: Detailed activity logging for monitoring
- 🔀 **Smart Randomization**: Random delays and proxy rotation for authenticity
- 🛡️ **Error Handling**: Robust error management and recovery
- 📱 **Cross-Platform**: Works on Windows, Linux, and Termux (Android)

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashab-cyber/instaswarm.git
   cd instaswarm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration files**
   - Create `accounts.txt` with your Instagram accounts
   - Create `comments.txt` with comments to use
   - Configure `proxies.txt` with your proxy list (optional)

## 📁 File Structure

```
instaswarm/
├── bot.py              # Main bot script
├── requirements.txt    # Python dependencies
├── accounts.txt        # Instagram account credentials
├── comments.txt        # Comment templates
├── proxies.txt         # Proxy list (optional)
├── instaswarm.log     # Activity log file
└── README.md          # This file
```

## ⚙️ Configuration

### 1. Account Setup (`accounts.txt`)

Add your Instagram accounts in the format:
```
username1,password1
username2,password2
username3,password3
```

### 2. Comments Setup (`comments.txt`)

Add comments that the bot will randomly select:
```
Amazing post! 🔥
Love this content! ❤️
Great work! 👏
Awesome! 😍
```

### 3. Proxy Setup (`proxies.txt`)

Configure proxies for enhanced anonymity:
```
# HTTP/HTTPS Proxies
http://user:pass@proxy1.example.com:8080
https://user:pass@proxy2.example.com:8080

# SOCKS5 Proxies
socks5://user:pass@proxy3.example.com:1080

# SOCKS4 Proxies
socks4://user:pass@proxy4.example.com:1080
```

## 🎮 Usage

1. **Run the bot**
   ```bash
   python bot.py
   ```

2. **Enter Instagram Post URL**
   - Paste the Instagram post URL you want to interact with
   - The bot will automatically extract the post ID

3. **Monitor Activity**
   - Check `instaswarm.log` for detailed activity logs
   - Watch terminal output for real-time status

## 🔧 Configuration Options

### Proxy Settings
```python
PROXY_ENABLED = True        # Enable/disable proxy usage
PROXY_FILE = "proxies.txt"  # Proxy file location
```

### Logging Configuration
- Log file: `instaswarm.log`
- Log level: INFO
- Includes timestamps and detailed activity tracking

## 🛡️ Security Features

- **Proxy Rotation**: Automatically rotates through available proxies
- **Random Delays**: Implements human-like delays between actions
- **Error Recovery**: Continues operation even if individual accounts fail
- **Proxy Validation**: Validates proxy format before usage

## 📝 Automated Actions

For each account, the bot performs:

1. **Login** with proxy support
2. **Like** the target post
3. **Comment** with random message from your list
4. **Follow** the post author
5. **Auto-reply** to recent comments on the post
6. **Logout** safely

## 🔍 Monitoring & Logs

All activities are logged to `instaswarm.log` including:
- Account login status
- Proxy usage information
- Action confirmations (likes, comments, follows)
- Error messages and recovery attempts
- Timestamps for all activities

## ⚠️ Important Notes

- **Rate Limiting**: Built-in delays prevent Instagram rate limiting
- **Account Safety**: Use high-quality proxies to protect accounts
- **Terms of Service**: Ensure compliance with Instagram's ToS
- **Responsible Usage**: Use for legitimate engagement only

## 🛠️ Dependencies

- `instagrapi`: Instagram API client
- `pysocks`: Advanced proxy support
- `pillow`: Image processing support

## 📊 Proxy Support

| Proxy Type | Supported | Format |
|------------|-----------|--------|
| HTTP | ✅ | `http://user:pass@host:port` |
| HTTPS | ✅ | `https://user:pass@host:port` |
| SOCKS4 | ✅ | `socks4://user:pass@host:port` |
| SOCKS5 | ✅ | `socks5://user:pass@host:port` |

## 🐛 Troubleshooting

### Common Issues

1. **Login Failed**
   - Check account credentials in `accounts.txt`
   - Verify proxy connectivity
   - Ensure accounts aren't restricted

2. **Proxy Errors**
   - Validate proxy format and credentials
   - Test proxy connectivity manually
   - Check proxy server status

3. **Rate Limiting**
   - Increase delays between actions
   - Use fewer accounts simultaneously
   - Implement longer session breaks

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is for educational purposes only. Users are responsible for compliance with Instagram's Terms of Service and applicable laws.

## 🔗 ZehraSec Links

- 📷 **Instagram**: [@_zehrasec](https://www.instagram.com/_zehrasec)
- 📘 **Facebook**: [ZehraSec](https://www.facebook.com/people/ZehraSec/61575580721849/)
- 💬 **WhatsApp**: [Channel](https://www.whatsapp.com/channel/0029Vaoa1GfKLaHlL0Kc8k1q)
- 🔗 **LinkedIn**: [Company](https://www.linkedin.com/company/zehrasec)
- 🐦 **Twitter**: [@zehrasec](https://x.com/zehrasec)
- 🌐 **Website**: [zehrasec.com](https://zehrasec.com)
- 🧠 **Lewis AI**: [lewis.zehrasec.com](https://lewis.zehrasec.com)
- 👁 **ZehraSight**: [zehrasight.zehrasec.com](https://zehrasight.zehrasec.com)

## ⭐ Support

If you find this project helpful, please give it a star! For support and questions, reach out through our social media channels.

---

**⚠️ Disclaimer**: This tool is for educational and research purposes only. Users are responsible for ensuring their usage complies with Instagram's Terms of Service and applicable laws. The developers are not responsible for any misuse or consequences resulting from the use of this software.
