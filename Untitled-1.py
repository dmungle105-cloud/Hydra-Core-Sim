#!/usr/bin/env python3
import sys
import os
import threading
import paramiko

# Safe thread limiting setup (Max 20 attempts at the exact same split second)
thread_limiter = threading.BoundedSemaphore(20)
password_found = False

def attempt_login(target_ip, username, password):
    global password_found
    
    if password_found:
        return

    thread_limiter.acquire()
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target_ip, port=22, username=username, password=password, timeout=2.0)
        print(f"\n[+] SUCCESS: Weak credentials found! -> {username}:{password}")
        password_found = True
        ssh.close()
    except paramiko.AuthenticationException:
        print(f"[-] Failed attempt: {username}:{password}")
    except Exception:
        pass
    finally:
        thread_limiter.release()

def main():
    print("=== Hydra-Core-Sim: Interactive Mode ===")
    
    # Check if arguments were passed in terminal; if not, ask the user interactively
    if len(sys.argv) >= 4:
        target_ip = sys.argv[1]
        username = sys.argv[2]
        wordlist_path = sys.argv[3]
    else:
        # Prompting the user directly for inputs
        target_ip = input("┌─ Enter Target IP (e.g., 127.0.0.1): ").strip()
        username = input("├─ Enter Username to audit (e.g., admin): ").strip()
        wordlist_path = input("└─ Enter Wordlist file path (e.g., common_passwords.txt): ").strip()
    
    # Input validation
    if not target_ip or not username or not wordlist_path:
        print("\n[-] Error: All fields are required to run the simulation.")
        sys.exit(1)
        
    if not os.path.exists(wordlist_path):
        print(f"\n[-] Error: Wordlist file not found at '{wordlist_path}'")
        print("Please check the filename spelling and ensure it is in the correct folder.")
        sys.exit(1)
        
    print(f"\n[*] Initializing password audit against {target_ip} for user '{username}'...")
    print("[*] Reading wordlist data...")
    
    threads = []
    
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            if password_found:
                break
                
            password = line.strip()
            if not password:
                continue
                
            t = threading.Thread(target=attempt_login, args=(target_ip, username, password))
            threads.append(t)
            t.start()
            
    for t in threads:
        t.join()
        
    if not password_found:
        print("\n[*] Audit complete. No weak passwords matched from the wordlist.")
    else:
        print("\n[*] Audit complete. Target verified as VULNERABLE.")

if __name__ == "__main__":
    main()
