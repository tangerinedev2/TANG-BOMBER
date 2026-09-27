# modules/proxy_manager.py - V13.0 DRAGON EDITION

import requests
import random
import os
import time
import json
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
from fake_useragent import UserAgent

class ProxyManager:
    def __init__(self, use_proxy=True, use_tor=False, use_fake_logs=True):
        self.use_proxy = use_proxy
        self.use_tor = use_tor
        self.use_fake_logs = use_fake_logs
        self.ua = UserAgent()
        self.proxies = []
        self.working_proxies = []
        self.fast_proxies = []
        self.blacklisted_proxies = set()
        self.last_update = 0
        self.fake_logs = []
        
        self.webshare_username = "sdbxufzg"
        self.webshare_password = "60rasjhi4xii"
        self.webshare_proxies = [
            "31.59.20.176:6754", "45.38.107.97:6014", "198.105.121.200:6462",
            "64.137.96.74:6641", "198.23.243.226:6361", "38.154.185.97:6370",
            "84.247.60.125:6095", "142.111.67.146:5611", "191.96.254.138:6185",
            "31.58.9.4:6077"
        ]
        
        if use_proxy:
            self._load_proxies()
        
        if use_fake_logs:
            self._generate_fake_logs()
    
    def _log(self, mesaj, seviye="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open('data/tang_bomber.log', 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{seviye}] [ProxyManager] {mesaj}\n")
        except:
            pass
    
    def _generate_fake_logs(self):
        self.fake_logs = [
            f"User from {random.choice(['Ankara', 'İstanbul', 'İzmir', 'Bursa', 'Antalya'])}",
            f"Session: {time.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Browser: {random.choice(['Chrome', 'Firefox', 'Safari', 'Edge'])}",
            f"Device: {random.choice(['Windows', 'MacOS', 'Linux', 'Android'])}",
            f"Language: tr-TR",
        ]
        self._log(f"{len(self.fake_logs)} fake log oluşturuldu", "INFO")
        print(f"{Fore.GREEN}[+] {len(self.fake_logs)} fake log oluşturuldu!{Style.RESET_ALL}")
    
    def _load_proxies(self):
        self.proxies.extend(self.webshare_proxies)
        self._log(f"{len(self.webshare_proxies)} Webshare proxy eklendi", "INFO")
        print(f"{Fore.CYAN}[+] {len(self.webshare_proxies)} Webshare proxy eklendi!{Style.RESET_ALL}")
        
        try:
            if os.path.exists('data/proxies.txt'):
                with open('data/proxies.txt', 'r') as f:
                    file_proxies = [line.strip() for line in f if line.strip()]
                    self.proxies.extend(file_proxies)
                    self._log(f"{len(file_proxies)} proxy dosyadan yüklendi", "INFO")
                    print(f"{Fore.GREEN}[+] {len(file_proxies)} proxy dosyadan yüklendi!{Style.RESET_ALL}")
        except:
            pass
        
        self.proxies = list(set(self.proxies))
        self._log(f"Toplam {len(self.proxies)} proxy", "INFO")
        print(f"{Fore.GREEN}[+] Toplam {len(self.proxies)} proxy!{Style.RESET_ALL}")
        self._test_all_proxies()
    
    def _test_single_proxy(self, proxy):
        try:
            if proxy in self.webshare_proxies:
                proxy_str = f"{self.webshare_username}:{self.webshare_password}@{proxy}"
                test_proxy = {"http": f"http://{proxy_str}", "https": f"http://{proxy_str}"}
            else:
                if not proxy.startswith(('http://', 'https://')):
                    test_proxy = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
                else:
                    test_proxy = {"http": proxy, "https": proxy}
            
            start = time.time()
            response = requests.get(
                'http://httpbin.org/ip',
                proxies=test_proxy,
                timeout=5,
                verify=False,
                headers={"User-Agent": self.ua.random}
            )
            elapsed = time.time() - start
            
            if response.status_code == 200 and elapsed < 3.0:
                return True, elapsed
            return False, elapsed
        except:
            return False, 999
    
    def _test_all_proxies(self):
        if not self.proxies:
            return
        
        test_limit = min(300, len(self.proxies))
        self._log(f"{test_limit} proxy test ediliyor", "INFO")
        print(f"{Fore.YELLOW}[!] {test_limit} proxy test ediliyor...{Style.RESET_ALL}")
        
        self.working_proxies = []
        self.fast_proxies = []
        self.blacklisted_proxies = set()
        
        with ThreadPoolExecutor(max_workers=30) as executor:
            futures = {executor.submit(self._test_single_proxy, proxy): proxy for proxy in self.proxies[:test_limit]}
            
            for future in as_completed(futures):
                proxy = futures[future]
                try:
                    success, elapsed = future.result(timeout=6)
                    if success:
                        self.working_proxies.append(proxy)
                        if elapsed < 1.5:
                            self.fast_proxies.append(proxy)
                            print(f"{Fore.GREEN}⚡{Style.RESET_ALL}", end="", flush=True)
                        else:
                            print(f"{Fore.GREEN}.{Style.RESET_ALL}", end="", flush=True)
                    else:
                        self.blacklisted_proxies.add(proxy)
                        print(f"{Fore.RED}.{Style.RESET_ALL}", end="", flush=True)
                except:
                    self.blacklisted_proxies.add(proxy)
                    print(f"{Fore.RED}.{Style.RESET_ALL}", end="", flush=True)
        
        print()
        self._log(f"{len(self.working_proxies)} proxy bulundu, {len(self.fast_proxies)} hızlı", "INFO")
        print(f"{Fore.GREEN}[+] {len(self.working_proxies)} proxy bulundu!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[⚡] {len(self.fast_proxies)} hızlı proxy (1.5 sn altı)!{Style.RESET_ALL}")
        self.last_update = time.time()
    
    def get_proxy(self):
        if not self.use_proxy:
            return None
        
        webshare_working = [p for p in self.working_proxies if p in self.webshare_proxies]
        if webshare_working:
            proxy = random.choice(webshare_working)
            proxy_str = f"{self.webshare_username}:{self.webshare_password}@{proxy}"
            return {"http": f"http://{proxy_str}", "https": f"http://{proxy_str}"}
        
        if self.fast_proxies:
            proxy = random.choice(self.fast_proxies)
            if not proxy.startswith(('http://', 'https://')):
                proxy = f"http://{proxy}"
            return {"http": proxy, "https": proxy}
        
        if self.working_proxies:
            proxy = random.choice(self.working_proxies)
            if not proxy.startswith(('http://', 'https://')):
                proxy = f"http://{proxy}"
            return {"http": proxy, "https": proxy}
        
        return None
    
    def get_random_proxy(self):
        return self.get_proxy()
    
    def get_fake_log(self):
        return random.choice(self.fake_logs) if self.fake_logs else "Fake log yok"
    
    def count(self):
        return len(self.working_proxies)
    
    def get_stats(self):
        webshare_count = len([p for p in self.working_proxies if p in self.webshare_proxies])
        return {
            "toplam": len(self.proxies),
            "calisan": len(self.working_proxies),
            "hizli": len(self.fast_proxies),
            "webshare": webshare_count,
            "olu": len(self.blacklisted_proxies),
            "oran": f"{len(self.working_proxies)/len(self.proxies)*100:.1f}%" if self.proxies else "0%",
            "tor_aktif": False,
            "tor_port": None,
            "fake_logs": len(self.fake_logs)
        }