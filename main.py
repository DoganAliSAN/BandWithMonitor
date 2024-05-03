import psutil
import time
from pynput import keyboard

start_time = time.time()
old_sent = psutil.net_io_counters().bytes_sent
old_recv = psutil.net_io_counters().bytes_recv
download_started = False

def on_press(key):
    global download_started
    if key == keyboard.Key.f9:
        download_started = True

def on_release(key):
    global download_started
    if key == keyboard.Key.f9:
        download_started = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while True:
        new_sent = psutil.net_io_counters().bytes_sent
        new_recv = psutil.net_io_counters().bytes_recv
        elapsed_time = time.time() - start_time
        
        if download_started:
            download_sent = new_sent - old_sent
            download_recv = new_recv - old_recv
            
            print(f"Downloaded: {download_sent/1024/1024:.2f} MB, Speed: {download_recv/elapsed_time/1024/1024:.2f} MB/s")
        
        old_sent = new_sent
        old_recv = new_recv
        time.sleep(1)
