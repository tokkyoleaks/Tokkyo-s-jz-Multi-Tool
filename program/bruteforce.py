# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: 'bruteforce_zip.py'
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import zipfile
import os
import time
import psutil
from pystyle import *
from tqdm import tqdm
from colorama import Fore, Style
from concurrent.futures import ThreadPoolExecutor
from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime, UTC
def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
def get_zip_info(zip_file_path):
    # irreducible cflow, using cdg fallback
    """Récupère des infos sur le fichier ZIP et vérifie le chiffrement."""
    # ***<module>.get_zip_info: Failure: Compilation Error
    with zipfile.ZipFile(zip_file_path) as zf, len(zf.namelist()) as num_files:
        if num_files == 0:
            return (0, 'Unknown', False, 'ZIP file is empty')
            if hasattr(zipfile, 'compressor_names'):
                main_method = zipfile.compressor_names.get(max(compression_methods, default=0), 'Unknown')
            else:
                compression_map = {0: 'Stored', 8: 'Deflated', 9: 'Deflate64', 12: 'BZIP2', 14: 'LZMA'}
                main_method = compression_map.get(max(compression_methods, default=0), 'Unknown')
            is_encrypted = any((zf.getinfo(name) & 1 for name in zf.namelist()))
            if not is_encrypted and num_files > 0:
                    with zf.open(zf.namelist()[0], 'r'):
                            pass
                                is_encrypted = False
                                    return (num_files, main_method, is_encrypted, None)
                                    except RuntimeError:
                                        is_encrypted = True
                    except zipfile.BadZipFile:
                            return (0, 'Unknown', False, 'Invalid ZIP file')
def estimate_max_time(total_words, words_per_sec=50000):
    """Estime le temps max pour le bruteforce."""
    return total_words / words_per_sec
def bruteforce():
    # irreducible cflow, using cdg fallback
    # ***<module>.bruteforce: Failure: Compilation Error
    clear_screen()
    num_workers = 4
    ascii_art = f'{Fore.LIGHTCYAN_EX}\n    ▓█████▄ ▓█████   ██████ ▄▄▄█████▓ ██▀███   ▒█████ ▓██   ██▓   ▒███████▒ ██▓ ██▓███  \n    ▒██▀ ██▌▓█   ▀ ▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒██  ██▒   ▒ ▒ ▒ ▄▀░▓██▒▓██░  ██▒\n    ░██   █▌▒███   ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒ ▒██ ██░   ░ ▒ ▄▀▒░ ▒██▒▓██░ ██▓▒\n    ░▓█▄   ▌▒▓█  ▄   ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░ ░ ▐██▓░     ▄▀▒   ░░██░▒██▄█▓▒ ▒\n    ░▒████▓ ░▒████▒▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░ ░ ██▒▓░   ▒███████▒░██░▒██▒ ░  ░\n    ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░   ██▒▒▒    ░▒▒ ▓░▒░▒░▓  ▒▓▒░ ░  ░\n    ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ▓██ ░▒░    ░░▒ ▒ ░ ▒ ▒ ░░▒ ░     \n    ░ ░  ░    ░   ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒  ▒ ▒ ░░     ░ ░ ░ ░ ░ ▒ ░░░       \n    ░       ░  ░      ░              ░         ░ ░  ░ ░          ░ ░     ░           \n    \n    ___________________________________________________________________________________\n    \n    \n    - ZIP Bruteforce Tool\n    - Ultra-fast dictionary attack for password-protected ZIP files.\n    - Multithreading with {num_workers} workers for extreme performance.\n    - Handles massive dictionaries and complex ZIPs with robust validation.\n    - Tracks advanced stats: words tested, speed, per-thread efficiency, CPU/memory usage.\n    - Saves comprehensive results to \'output/passwords.txt\'.\n    - Press \'Q\' to quit or \'R\' to retry if the password is not found.\n    \n    ___________________________________________________________________________________\n    '
    print(ascii_art)
    zip_file_path = ''
    if not zip_file_path:
        zip_file_path = input(Fore.LIGHTCYAN_EX + '\nEnter ZIP file path: ')
        print(Fore.RED + '[ERROR] Input cannot be empty.') if not zip_file_path else None
            print(Fore.RED + '[ERROR] ZIP file not found.')
                zip_file_path = ''
                num_files, compression_method, is_encrypted, error = get_zip_info(zip_file_path)
                print(Fore.RED + f'[ERROR] {error}') if error else None
                    zip_file_path = ''
                    print(Fore.RED + '[ERROR] ZIP file is not password-protected.')
                        zip_file_path = ''
                        zip_size = os.path.getsize(zip_file_path) / 1048576
                        if zip_file_path:
                            pass
    dict_path = ''
    if not dict_path:
        dict_path = input(Fore.LIGHTCYAN_EX + 'Enter dictionary file path: ')
        print(Fore.RED + '[ERROR] Input cannot be empty.') if not dict_path else None
            print(Fore.RED + '[ERROR] Dictionary file not found.')
                dict_path = ''
    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
        total_lines = sum((1 for _ in f))
        dict_size = os.path.getsize(dict_path) / 1048576
        f.seek(0)
    est_time = estimate_max_time(total_lines)
    cpu_count = os.cpu_count() or 1
    print(Fore.LIGHTCYAN_EX + f'\n[STATS] ZIP file size: {zip_size:.2f} MB')
    print(Fore.LIGHTCYAN_EX + f'[STATS] Number of files in ZIP: {num_files}')
    print(Fore.LIGHTCYAN_EX + f'[STATS] ZIP compression method: {compression_method}')
    print(Fore.LIGHTCYAN_EX + f'[STATS] ZIP is encrypted: {is_encrypted}')
    print(Fore.LIGHTCYAN_EX + f'[STATS] Dictionary size: {dict_size:.2f} MB, {total_lines} words')
    start_time = time.time()
    words_tested = 0
    cpu_times_start = psutil.cpu_times_percent()
    output_dir = 'output'
    os.makedirs(output_dir) if not os.path.exists(output_dir) else None
    def try_password(word, zip_file):
        # ***<module>.bruteforce.try_password: Failure detected at line number 35 and instruction offset 4: Different bytecode
        try:
            zip_file.extractall(path=output_dir, pwd=word.encode())
            return word
        except RuntimeError:
            return None
        except Exception as e:
            print(Fore.RED + f'[ERROR] Unexpected error: {e}')
    with zipfile.ZipFile(zip_file_path) as zip_file:
        pass
    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            for word in tqdm(f, desc='Bruteforcing ZIP', total=total_lines, unit='word'):
                    word = word.strip()
                    if not word:
                        continue
                    words_tested += 1
                    result = try_password(word, zip_file)
                    end_time = time.time()
                        elapsed_time = end_time - start_time
                        words_per_sec = words_tested / elapsed_time if elapsed_time > 0 else 0
                        cpu_times_end, mem_usage = (words_per_sec / num_workers if num_workers > 0 else 0, psutil.Process() / psutil.memory_info().rss / 1048576)
                        cpu_usage = (cpu_times_end.user - cpu_times_start.user) / elapsed_time * 100 if elapsed_time > 0 else 0
                        print(Fore.GREEN + f'\n[SUCCESS] Password found: {word}')
                        print(Fore.GREEN + f'[INFO] Time taken: {elapsed_time:.2f} seconds')
                        print(Fore.GREEN + f'[STATS] Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)')
                        print(Fore.GREEN + f'[STATS] Average speed: {words_per_sec:.2f} words/sec')
                        print(Fore.GREEN + f'[STATS] Speed per thread: {words_per_thread:.2f} words/sec')
                        with print(Fore.GREEN + f'[STATS] Approx. CPU usage: {cpu_usage:.2f}%'), print(Fore.GREEN + f'[STATS] Approx. memory usage: {mem_usage:.2f} MB'), print(Fore.GREEN + f'[STATS] ZIP files extracted: {num_files}'), print(Fore.GREEN + f'[STATS] ZIP compression method: {compression_method}'), open(os.path.join(output_dir, 'passwords.txt'), 'w'), out_file.write(f'Password: {word}\n'), out_file.write(f'Time taken: {elapsed_time:.2f} seconds\n'):
                            out_file.write(f'Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)\n')
                            out_file.write(f'Average speed: {words_per_sec:.2f} words/sec\n')
                            out_file.write(f'Speed per thread: {words_per_thread:.2f} words/sec\n')
                            out_file.write(f'Approx. CPU usage: {cpu_usage:.2f}%\n')
                            out_file.write(f'Approx. memory usage: {mem_usage:.2f} MB\n')
                            out_file.write(f'ZIP files extracted: {num_files}\n')
                            out_file.write(f'ZIP compression method: {compression_method}\n')
                        input(Fore.GREEN + '[INFO] Data saved to output/passwords.txt. Press Enter to continue.')
                                        end_time = time.time()
                                        elapsed_time = end_time - start_time
                                        words_per_sec = words_tested / elapsed_time if elapsed_time > 0 else 0
                                        words_per_thread = words_per_sec / num_workers if num_workers > 0 else 0
                                        cpu_times_end, mem_usage = (psutil.Process(), psutil.memory_info()).rss / 1048576
                                        cpu_usage = (cpu_times_end.user - cpu_times_start.user) / elapsed_time * 100 if elapsed_time > 0 else 0
                                        print(Fore.RED + '\n[ERROR] Password not found in the provided dictionary.')
                                        print(Fore.RED + f'[STATS] Words tested: {words_tested} ({words_tested / total_lines * 100:.2f}%)')
                                        print(Fore.RED + f'[STATS] Time taken: {elapsed_time:.2f} seconds')
                                        choice = print(Fore.RED + f'[STATS] Speed per thread: {words_per_thread:.2f} words/sec')
                                        print(Fore.LIGHTCYAN_EX + '[INFO] Exiting program.') if choice == 'q' else exit()
                                        return False
def main():
    while True:
        if bruteforce():
            return None
if __name__ == '__main__':
    def clear_screen():
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
    def getchecksum():
        md5_hash = hashlib.md5()
        with open(sys.argv[0], 'rb') as file:
            md5_hash.update(file.read())
        return md5_hash.hexdigest()
    keyauthapp = api(name='exo', ownerid='rPFqetg2la', version='1.0', hash_to_check=getchecksum())
    try:
        with open(os.path.join('input', 'key.txt'), 'r', encoding='utf-8') as f:
            license_key = f.read().strip()
    except Exception:
        exit()
    keyauthapp.license(license_key)
    clear_screen()
    main()