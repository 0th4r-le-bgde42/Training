# import sys
# import traceback
# import time
# import random

# # import tes fonctions
# from ex1.brackets import brackets
# from ex2.echo_validator import echo_validator
# from ex3.matrix_reverse import matrix_reverse
# from ex4.pattern_tracker import pattern_tracker
# from ex5.number_base_converter import number_base_converter
# from ex6.shadow_merge import shadow_merge
# from ex7.string_permutation_checker import string_permutation_checker
# from ex8.py_string_sculptor import py_string_sculptor
# from ex9.twist_sequence import twist_sequence
# from ex10.whisper_cipher import whisper_cipher

# # couleurs cyberpunk
# RESET = "\033[0m"
# NEON_PINK = "\033[95m"
# NEON_BLUE = "\033[94m"
# NEON_GREEN = "\033[92m"
# NEON_RED = "\033[91m"
# NEON_YELLOW = "\033[93m"
# BOLD = "\033[1m"
# DIM = "\033[2m"

# total = 30
# passed = 0


# def slow_print(text, color="", delay=0.01):
#     for c in text:
#         sys.stdout.write(color + c + RESET)
#         sys.stdout.flush()
#         time.sleep(delay)
#     print()


# def scan(text):
#     for i in range(3):
#         sys.stdout.write(NEON_BLUE + f"\r{text}{'.'*i}" + RESET)
#         sys.stdout.flush()
#         time.sleep(0.2)
#     print()


# def progress():
#     bar_len = 20
#     done = int((passed / total) * bar_len) if total else 0
#     bar = "█" * done + "░" * (bar_len - done)
#     print(f"{NEON_PINK}[{bar}] {passed}/{total}{RESET}")


# def banner():
#     print()
#     slow_print("╔══════════════════════════════════════╗", NEON_PINK, 0.002)
#     slow_print("║        PYTHON EXAM TEST SYSTEM       ║", NEON_PINK, 0.002)
#     slow_print("║          CYBERPUNK EDITION           ║", NEON_PINK, 0.002)
#     slow_print("╚══════════════════════════════════════╝", NEON_PINK, 0.002)
#     print()


# def section(title):
#     slow_print(f">>> {title}", NEON_BLUE, 0.01)
#     time.sleep(0.2)


# def run_test(name, func_name, args, expected):
#     global total, passed

#     if func_name not in globals():
#         slow_print(f"[MISSING] {func_name} not implemented yet", NEON_YELLOW, 0.005)
#         progress()
#         print()
#         return

#     func = globals()[func_name]

#     scan(f"Running {name}")

#     try:
#         result = func(*args)

#         if result == expected:
#             passed += 1
#             slow_print(f"[OK] {name} {args} -> {result}", NEON_GREEN, 0.003)
#         else:
#             slow_print(f"[FAIL] {name} {args}", NEON_RED, 0.003)
#             slow_print(f"expected : {expected}", NEON_YELLOW, 0.002)
#             slow_print(f"got      : {result}", NEON_RED, 0.002)

#     except Exception:
#         slow_print(f"[CRASH] {name} {args}", NEON_RED, 0.003)
#         print(traceback.format_exc())

#     progress()
#     print()

# def print_test():
#     """Affiche un résumé détaillé en respectant l'ordre des exercices ex1 à ex10."""
#     print(f"\n{NEON_BLUE}{BOLD}═══ DECRYPTED DATA : SYSTEM CHRONOLOGY ═══{RESET}")

#     # ex1: brackets
#     print(f"\n{NEON_PINK}[ex1] Brackets Validation{RESET}")
#     for b in ['()', '([])', '(]', '([)]', '{[]}']:
#         res = brackets(b)
#         color = NEON_GREEN if (res and b in ['()', '([])', '{[]}']) or (not res and b in ['(]', '([)]']) else NEON_RED
#         print(f"  {DIM}{b:6}{RESET} -> {color}{res}{RESET}")

#     # ex2: echo_validator
#     print(f"\n{NEON_PINK}[ex2] Echo Validator{RESET}")
#     print(f"  Radar   : {NEON_GREEN if echo_validator('Radar') else NEON_RED}VALID{RESET}")
#     print(f"  Panama  : {NEON_GREEN if echo_validator('A man, a plan, a canal: Panama') else NEON_RED}VALID{RESET}")

#     # ex3: matrix_reverse
#     print(f"\n{NEON_PINK}[ex3] Matrix Reverse{RESET}")
#     print(f"  Input   : [[1,2,3],[4,5,6]]")
#     print(f"  Output  : {NEON_YELLOW}{matrix_reverse([[1,2,3],[4,5,6]])}{RESET}")

#     # ex4: pattern_tracker
#     print(f"\n{NEON_PINK}[ex4] Pattern Tracker{RESET}")
#     print(f"  'a123b45' : {NEON_BLUE}{pattern_tracker('a123b45')} sequences found{RESET}")

#     # ex5: number_base_converter
#     print(f"\n{NEON_PINK}[ex5] Number Base Converter{RESET}")
#     print(f"  101 (2->10) : {NEON_GREEN}{number_base_converter('101', 2, 10)}{RESET}")
#     print(f"  255 (10->16): {NEON_GREEN}{number_base_converter('255', 10, 16)}{RESET}")

#     # ex6: shadow_merge
#     print(f"\n{NEON_PINK}[ex6] Shadow Merge{RESET}")
#     print(f"  Result  : {NEON_YELLOW}{shadow_merge([3,1,5],[2,4])}{RESET}")

#     # ex7: string_permutation_checker
#     print(f"\n{NEON_PINK}[ex7] Permutation Checker{RESET}")
#     print(f"  abc/cab : {NEON_GREEN if string_permutation_checker('abc', 'cab') else NEON_RED}MATCH{RESET}")

#     # ex8: py_string_sculptor
#     print(f"\n{NEON_PINK}[ex8] String Sculptor{RESET}")
#     print(f"  Result  : {NEON_YELLOW}{py_string_sculptor('Hello World')}{RESET}")

#     # ex9: twist_sequence
#     print(f"\n{NEON_PINK}[ex9] Twist Sequence (Rotation){RESET}")
#     print(f"  k=1     : {NEON_YELLOW}{twist_sequence([1,2,3,4], 1)}{RESET}")
#     print(f"  k=2     : {NEON_YELLOW}{twist_sequence([1,2,3,4], 2)}{RESET}")

#     # ex10: whisper_cipher
#     print(f"\n{NEON_PINK}[ex10] Whisper Cipher{RESET}")
#     print(f"  Shift 3 : {NEON_BLUE}{whisper_cipher('Hello', 3)}{RESET}")

#     print(f"\n{NEON_BLUE}{BOLD}══════════════════════════════════════════{RESET}\n")

# banner()

# # Liste des tests : nom à afficher, nom de la fonction, args, valeur attendue
# tests = [
#     ("brackets ()", "brackets", ("()",), True),
#     ("brackets ([])","brackets", ("([])",), True),
#     ("brackets (]", "brackets", ("(]",), False),
#     ("brackets ([)]","brackets", ("([)]",), False),
#     ("brackets {[]}", "brackets", ("{[]}",), True),

#     ("echo_validator Radar","echo_validator",("Radar",), True),
#     ("echo_validator Panama","echo_validator",("A man, a plan, a canal: Panama",), True),
#     ("echo_validator Hello","echo_validator",("Hello",), False),
#     ("echo_validator Kayak", "echo_validator", ("K351635413Ay@#$%^&*a[}K]",), True),

#     ("matrix_reverse", "matrix_reverse", ([[1,2,3],[4,5,6]],), [[3,2,1],[6,5,4]]),

#     ("pattern_tracker 123","pattern_tracker",("123",),2),
#     ("pattern_tracker 1293","pattern_tracker",("1293",),1),
#     ("pattern_tracker a123b45","pattern_tracker",("a123b45",),3),

#     ("number_base_converter 101","number_base_converter",("101",2,10),"5"),
#     ("number_base_converter FF","number_base_converter",("FF",16,10),"255"),
#     ("number_base_converter 255","number_base_converter",("255",10,16),"FF"),
#     ("number_base_converter XYZ","number_base_converter",("XYZ",10,2),"ERROR"),

#     ("shadow_merge","shadow_merge",([3,1,5],[2,4]),[1,2,3,4,5]),

#     ("string_permutation_checker abc/cab","string_permutation_checker",("abc","cab"),True),
#     ("string_permutation_checker hello/olleh","string_permutation_checker",("hello","olleh"),True),
#     ("string_permutation_checker abc/abcc","string_permutation_checker",("abc","abcc"),False),
#     ("string_permutation_checker Voldemort", "string_permutation_checker",("Tom Marvolo Riddle","I am Lord Voldemort"), False),

#     ("py_string_sculptor","py_string_sculptor",("Hello World",),"hElLo wOrLd"),
#     ("py_string_sculptor","py_string_sculptor",("BONjoUr A tous LE MondE",),"bOnJoUr a tOuS Le mOnDe"),

#     ("twist_sequence k=1","twist_sequence",([1,2,3,4],1),[4,1,2,3]),
#     ("twist_sequence k=2","twist_sequence",([1,2,3,4],2),[3,4,1,2]),
#     ("twist_sequence k=3","twist_sequence",([1,2,3,4],3),[2,3,4,1]),
#     ("twist_sequence k=4","twist_sequence",([1,2,3,4],4),[1,2,3,4]),

#     ("whisper_cipher Hello","whisper_cipher",("Hello",3),"Khoor"),
#     ("whisper_cipher abc","whisper_cipher",("abc",1),"bcd"),
# ]

# # Regroupe les tests par fonction
# current_section = ""
# for t in tests:
#     section_name = t[1]
#     if section_name != current_section:
#         section(section_name + " tests")
#         current_section = section_name
#     run_test(*t)

# print()
# slow_print("══════════════════════════════════════", NEON_PINK, 0.002)
# slow_print(
#     f"PASSED {passed}/{total} TESTS",
#     NEON_GREEN if passed == total else NEON_YELLOW,
#     0.004
# )
# slow_print("══════════════════════════════════════", NEON_PINK, 0.002)
# print()

# try:
#     while True:
#         print(f"{BOLD}{NEON_YELLOW}>> SYSTEM STATUS: ONLINE{RESET}")
#         print(f"{NEON_BLUE}1.{RESET} Scan all sectors (Run Tests)")
#         print(f"{NEON_BLUE}2.{RESET} View detailed decrypted logs (Print Test)")
#         print(f"{NEON_BLUE}3.{RESET} Emergency Exit")
        
#         choice = input(f"\n{NEON_PINK}cyber@rank3 > {RESET}").strip()
        
#         if choice == "1":
#             print("\033c", end="") # Clear screen
#             banner()
#             current_section = ""
#             passed = 0 # Reset counter for re-run
#             for t in tests:
#                 section_name = t[1]
#                 if section_name != current_section:
#                     section(section_name + " tests")
#                     current_section = section_name
#                 run_test(*t)
#             print(f"\n{NEON_GREEN}SCAN COMPLETE.{RESET}\n")
            
#         elif choice == "2":
#             scan("Fetching data from memory")
#             print_test()
#             input(f"{DIM}Press Enter to return to main menu...{RESET}")
#             print("\033c", end="")
            
#         elif choice == "3":
#             slow_print("Disconnecting from Neural Link...", NEON_RED, 0.02)
#             break
#         else:
#             print(f"{NEON_RED}Invalid command. Sequence aborted.{RESET}")

# except KeyboardInterrupt:
#     print(f"\n{NEON_RED}System breach detected. Manual override. Goodbye.{RESET}")

import sys, traceback, time

# Imports des modules
from ex1.brackets import brackets
from ex2.echo_validator import echo_validator
from ex3.matrix_reverse import matrix_reverse
from ex4.pattern_tracker import pattern_tracker
from ex5.number_base_converter import number_base_converter
from ex6.shadow_merge import shadow_merge
from ex7.string_permutation_checker import string_permutation_checker
from ex8.py_string_sculptor import py_string_sculptor
from ex9.twist_sequence import twist_sequence
from ex10.whisper_cipher import whisper_cipher

# Style & Couleurs
RESET, BOLD, DIM = "\033[0m", "\033[1m", "\033[2m"
NEON_PINK, NEON_BLUE = "\033[95m", "\033[94m"
NEON_GREEN, NEON_RED, NEON_YELLOW = "\033[92m", "\033[91m", "\033[93m"

def fast_scan(tests_list):
    """Scan visuel avec barre de progression dynamique (écrase la ligne)."""
    passed = 0
    total = len(tests_list)
    print(f"\n{NEON_BLUE}{BOLD}⚡ INITIATING AUTO-SCAN PROTOCOL...{RESET}")
    
    for i, (name, func_name, args, expected) in enumerate(tests_list):
        current = i + 1
        percent = int(current / total * 100)
        filled = int(current / total * 30)
        bar = "█" * filled + "░" * (30 - filled)
        
        # Affichage dynamique
        sys.stdout.write(f"\r{NEON_PINK}[{bar}] {percent}%{RESET} Analyzing: {DIM}{name[:35]:<35}{RESET}")
        sys.stdout.flush()

        time.sleep(0.02) # Vitesse de défilement visuel

        if func_name in globals():
            try:
                if globals()[func_name](*args) == expected:
                    passed += 1
            except: pass
    
    color = NEON_GREEN if passed == total else NEON_YELLOW
    print(f"\n\n{BOLD}{color}▶ SYSTEM STATUS: {passed}/{total} NODES OPERATIONAL{RESET}\n")
    return passed

def print_inspection(func_filter, tests_list):
    """Affiche les logs détaillés avec un effet de défilement fluide."""
    print(f"\n{NEON_BLUE}{BOLD}═══ DECRYPTING SECTOR : {func_filter.upper() if func_filter else 'ALL MODULES'} ═══{RESET}")
    time.sleep(0.3) # Petit temps de chargement initial

    for name, f_name, args, expected in tests_list:
        if func_filter and f_name != func_filter:
            continue
        
        # Micro-latence entre chaque ligne pour l'effet visuel
        time.sleep(0.05) 
        
        try:
            res = globals()[f_name](*args)
            if res == expected:
                status = f"{NEON_GREEN}[OK]{RESET}"
                details = f"{NEON_GREEN}{res}{RESET}"
            else:
                status = f"{NEON_RED}[FAIL]{RESET}"
                details = f"{NEON_RED}{res}{RESET} {DIM}(expected: {expected}){RESET}"
            
            print(f" {status} {DIM}{f_name}{RESET}({str(args)[1:-1]}) -> {details}")
            
        except Exception:
            print(f" {NEON_RED}[CRASH]{RESET} {f_name} : Critical logic failure.")
            
    print(f"\n{NEON_BLUE}{BOLD}══════════════════════════════════════════{RESET}\n")

# --- DATABASE COMPLETE DES 30 TESTS ---
tests = [
    ("brackets ()", "brackets", ("()",), True),
    ("brackets ([])","brackets", ("([])",), True),
    ("brackets (]", "brackets", ("(]",), False),
    ("brackets ([)]","brackets", ("([)]",), False),
    ("brackets {[]}", "brackets", ("{[]}",), True),
    ("echo_validator Radar","echo_validator",("Radar",), True),
    ("echo_validator Panama","echo_validator",("A man, a plan, a canal: Panama",), True),
    ("echo_validator Hello","echo_validator",("Hello",), False),
    ("echo_validator Kayak", "echo_validator", ("K351635413Ay@#$%^&*a[}K]",), True),
    ("matrix_reverse", "matrix_reverse", ([[1,2,3],[4,5,6]],), [[3,2,1],[6,5,4]]),
    ("pattern_tracker 123","pattern_tracker",("123",),2),
    ("pattern_tracker 1293","pattern_tracker",("1293",),1),
    ("pattern_tracker a123b45","pattern_tracker",("a123b45",),3),
    ("number_base_converter 101","number_base_converter",("101",2,10),"5"),
    ("number_base_converter FF","number_base_converter",("FF",16,10),"255"),
    ("number_base_converter 255","number_base_converter",("255",10,16),"FF"),
    ("number_base_converter XYZ","number_base_converter",("XYZ",10,2),"ERROR"),
    ("shadow_merge","shadow_merge",([3,1,5],[2,4]),[1,2,3,4,5]),
    ("permutation abc/cab","string_permutation_checker",("abc","cab"),True),
    ("permutation hello/olleh","string_permutation_checker",("hello","olleh"),True),
    ("permutation abc/abcc","string_permutation_checker",("abc","abcc"),False),
    ("permutation Voldemort", "string_permutation_checker",("Tom Marvolo Riddle","I am Lord Voldemort"), False),
    ("sculptor Hello World","py_string_sculptor",("Hello World",),"hElLo wOrLd"),
    ("sculptor BONjoUr","py_string_sculptor",("BONjoUr A tous LE MondE",),"bOnJoUr a tOuS Le mOnDe"),
    ("twist k=1","twist_sequence",([1,2,3,4],1),[4,1,2,3]),
    ("twist k=2","twist_sequence",([1,2,3,4],2),[3,4,1,2]),
    ("twist k=3","twist_sequence",([1,2,3,4],3),[2,3,4,1]),
    ("twist k=4","twist_sequence",([1,2,3,4],4),[1,2,3,4]),
    ("whisper Hello","whisper_cipher",("Hello",3),"Khoor"),
    ("whisper abc","whisper_cipher",("abc",1),"bcd"),
]

def main():
    print("\033c", end="") # Clear terminal au lancement
    print(f"{NEON_PINK}{BOLD}╔══════════════════════════════════════╗")
    print(f"║        PYTHON EXAM TEST SYSTEM       ║")
    print(f"║          CYBER-CHECKER v3.0          ║")
    print(f"╚══════════════════════════════════════╝{RESET}")
    
    # --- LANCEMENT AUTOMATIQUE ---
    fast_scan(tests)
    
    while True:
        print(f"{BOLD}{NEON_YELLOW}>> ACCESS LEVEL: RANK 3{RESET}")
        print(f"{NEON_BLUE}1.{RESET} Re-run Rapid Scan")
        print(f"{NEON_BLUE}2.{RESET} Deep Inspection (Module Selection)")
        print(f"{NEON_BLUE}3.{RESET} Terminate Session")
        
        cmd = input(f"\n{NEON_PINK}cyber@prompt > {RESET}").strip()
        
        if cmd == "1":
            fast_scan(tests)
        elif cmd == "2":
                while True:
                    # 1. Préparation de la liste des fonctions
                    funcs = []
                    for t in tests: 
                        if t[1] not in funcs: funcs.append(t[1])
                    
                    print("\033c", end="") # Nettoie l'écran pour l'inspection
                    print(f"{BOLD}{NEON_BLUE}═══ SECTOR INSPECTION MENU ═══{RESET}")
                    for i, f in enumerate(funcs):
                        print(f" {NEON_BLUE}{i+1:2}.{RESET} {f}")
                    print(f" {NEON_BLUE} A.{RESET} Show All Modules")
                    print(f" {NEON_RED} R.{RESET} Return to Main Menu")
                    
                    sub = input(f"\n{NEON_PINK}inspect@id > {RESET}").strip().lower()
                    
                    if sub == 'r':
                        print("\033c", end="")
                        break # Sort de la boucle d'inspection pour revenir au menu principal
                    
                    if sub == 'a':
                        print_inspection(None, tests)
                    elif sub.isdigit() and 0 < int(sub) <= len(funcs):
                        print_inspection(funcs[int(sub)-1], tests)
                    else:
                        print(f"{NEON_RED}Invalid Sector ID.{RESET}")
                        time.sleep(0.5)
                        continue

                    # 2. Option de rebond rapide après l'affichage
                    print(f"{BOLD}{NEON_YELLOW}CONTINUE INSPECTION?{RESET}")
                    print(f" {DIM}(Enter to stay in Inspection / 'r' for Main Menu){RESET}")
                    nav = input(f"{NEON_PINK}nav > {RESET}").strip().lower()
                    
                    if nav == 'r':
                        print("\033c", end="")
                        break
        elif cmd == "3":
            print(f"{NEON_RED}Neural link severed. Disconnecting...{RESET}")
            break

if __name__ == "__main__":
    main()