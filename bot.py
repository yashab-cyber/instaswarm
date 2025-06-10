from instagrapi import Client
import time
import random
import re
import os
import logging
import socks  # PySocks for advanced proxy support

# ================= CONFIG =================
ZEHRASEC_LINKS = """
🔗 Follow ZehraSec:
📷 Instagram: https://www.instagram.com/_zehrasec
📘 Facebook: https://www.facebook.com/people/ZehraSec/61575580721849/
💬 WhatsApp: https://www.whatsapp.com/channel/0029Vaoa1GfKLaHlL0Kc8k1q
🔗 LinkedIn: https://www.linkedin.com/company/zehrasec
🐦 Twitter (X): https://x.com/zehrasec?t=Tp9LOesZw2d2yTZLVo0_GA&s=08
🌐 Website: https://zehrasec.com
🧠 Lewis AI: https://lewis.zehrasec.com
👁 ZehraSight: https://zehrasight.zehrasec.com
"""

PROXY_ENABLED = True
PROXY_FILE = "proxies.txt"

logging.basicConfig(
    filename="instaswarm.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def ascii_ui():
    os.system("clear" if os.name != "nt" else "cls")
    print(r'''
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
===============================================================================
''')
    print(ZEHRASEC_LINKS)

def load_file_lines(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    return []

def get_shortcode(url):
    m = re.search(r"/p/([a-zA-Z0-9_-]+)/", url)
    return m.group(1) if m else None

def auto_reply_to_comments(cl, media_id):
    comments = cl.media_comments(media_id, amount=5)
    for comment in comments:
        if not comment.user.is_self:
            reply_text = random.choice(["Thanks!", "Appreciate it 🙏", "❤️ from me"])
            cl.media_comment(media_id, f"@{comment.user.username} {reply_text}")
            logging.info(f"Replied to @{comment.user.username}")

def perform_actions(username, password, shortcode, comment_list, proxy=None):
    cl = Client()
    if proxy:
        logging.info(f"[{username}] Using proxy: {proxy}")
        try:
            if proxy.startswith("socks5://") or proxy.startswith("socks4://"):
                # Parse socks proxy
                proxy_type = socks.SOCKS5 if proxy.startswith("socks5://") else socks.SOCKS4
                proxy_url = proxy.split("//", 1)[1]
                if "@" in proxy_url:
                    creds, hostport = proxy_url.split("@", 1)
                    username, password = creds.split(":", 1)
                else:
                    username = password = None
                    hostport = proxy_url
                if ":" in hostport:
                    host, port = hostport.split(":", 1)
                else:
                    host = hostport
                    port = 1080
                port = int(port)
                socks.set_default_proxy(proxy_type, host, port, username=username, password=password)
                import socket
                socket.socket = socks.socksocket
                cl.set_proxy(None)  # Remove HTTP proxy if set
            else:
                cl.set_proxy(proxy)
        except Exception as e:
            logging.error(f"[{username}] Failed to set proxy {proxy}: {e}")
            raise

    try:
        cl.login(username, password)
    except Exception as e:
        logging.error(f"[{username}] Login failed: {e}")
        raise

    media_id = cl.media_id(cl.media_pk_from_shortcode(shortcode))

    cl.media_like(media_id)
    logging.info(f"[{username}] Liked post.")

    comment = random.choice(comment_list)
    cl.media_comment(media_id, comment)
    logging.info(f"[{username}] Commented: {comment}")

    user_info = cl.media_info(media_id).user
    cl.user_follow(user_info.pk)
    logging.info(f"[{username}] Followed post author: {user_info.username}")

    auto_reply_to_comments(cl, media_id)
    cl.logout()

def main():
    ascii_ui()
    post_url = input("🔗 Enter Instagram Post URL: ").strip()
    shortcode = get_shortcode(post_url)
    if not shortcode:
        print("❌ Invalid post URL.")
        return

    accounts = load_file_lines("accounts.txt")
    comments = load_file_lines("comments.txt")
    proxies = load_file_lines(PROXY_FILE) if PROXY_ENABLED else []

    if proxies:
        random.shuffle(proxies)

    for i, line in enumerate(accounts):
        try:
            username, password = line.split(",", 1)
            proxy = proxies[i % len(proxies)] if proxies else None
            if proxy and not proxy.startswith("http"):
                logging.warning(f"Skipping invalid proxy format: {proxy}")
                proxy = None
            perform_actions(username, password, shortcode, comments, proxy)
            time.sleep(random.randint(5, 10))  # delay between accounts
        except Exception as e:
            logging.error(f"[{line}] Error: {str(e)}")
            continue

if __name__ == "__main__":
    main()
