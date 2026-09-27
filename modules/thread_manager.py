# modules/thread_manager.py - V13.0 DRAGON EDITION

import threading
import queue
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from colorama import Fore, Style

class ThreadManager:
    def __init__(self, max_threads=30):
        self.max_threads = min(max_threads, 100)
        self.queue = queue.Queue()
        self.results = []
        self.threads = []
        self.running = False
    
    def _log(self, mesaj, seviye="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open('data/tang_bomber.log', 'a', encoding='utf-8') as f:
                f.write(f"[{timestamp}] [{seviye}] [ThreadManager] {mesaj}\n")
        except:
            pass
    
    def add_task(self, task_func, *args, **kwargs):
        self.queue.put((task_func, args, kwargs))
    
    def _worker(self):
        while self.running:
            try:
                task_func, args, kwargs = self.queue.get(timeout=1)
                start_time = time.time()
                result = task_func(*args, **kwargs)
                elapsed = time.time() - start_time
                self.results.append(result)
                self.queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                self._log(f"Worker hatası: {e}", "ERROR")
                self.queue.task_done()
    
    def start(self):
        self.running = True
        thread_count = min(self.max_threads, self.queue.qsize() * 2, 100)
        self._log(f"{thread_count} thread başlatılıyor", "INFO")
        for _ in range(thread_count):
            thread = threading.Thread(target=self._worker)
            thread.daemon = True
            thread.start()
            self.threads.append(thread)
    
    def wait(self):
        self.queue.join()
        self.running = False
        for thread in self.threads:
            thread.join(timeout=1)
        self._log("Tüm thread'ler tamamlandı", "INFO")
    
    def get_results(self):
        return self.results
    
    @staticmethod
    def run_parallel(task_func, items, max_threads=30, *args, **kwargs):
        manager = ThreadManager(max_threads)
        for item in items:
            manager.add_task(task_func, item, *args, **kwargs)
        manager.start()
        manager.wait()
        return manager.get_results()
    
    @staticmethod
    def run_batch(task_func, items, batch_size=10, max_threads=30, *args, **kwargs):
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i+batch_size]
            batch_results = ThreadManager.run_parallel(task_func, batch, max_threads, *args, **kwargs)
            results.extend(batch_results)
        return results