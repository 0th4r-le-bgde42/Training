import sys
import traceback
import time
import random

# import tes fonctions
from exercises import *

# couleurs cyberpunk
RESET = "\033[0m"
NEON_PINK = "\033[95m"
NEON_BLUE = "\033[94m"
NEON_GREEN = "\033[92m"
NEON_RED = "\033[91m"
NEON_YELLOW = "\033[93m"
BOLD = "\033[1m"
DIM = "\033[2m"

total = 0
passed = 0


def slow_print(text, color="", delay=0.01):
    for c in text:
        sys.stdout.write(color + c + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def scan(text):
    for i in range(3):
        sys.stdout.write(NEON_BLUE + f"\r{text}{'.'*i}" + RESET)
        sys.stdout.flush()
        time.sleep(0.2)
    print()


def progress():
    bar_len = 20
    done = int((passed / total) * bar_len) if total else 0
    bar = "█" * done + "░" * (bar_len - done)
    print(f"{NEON_PINK}[{bar}] {passed}/{total}{RESET}")


def banner():
    print()
    slow_print("╔══════════════════════════════════════╗", NEON_PINK, 0.002)
    slow_print("║        PYTHON EXAM TEST SYSTEM       ║", NEON_PINK, 0.002)
    slow_print("║          CYBERPUNK EDITION           ║", NEON_PINK, 0.002)
    slow_print("╚══════════════════════════════════════╝", NEON_PINK, 0.002)
    print()


def section(title):
    slow_print(f">>> {title}", NEON_BLUE, 0.01)
    time.sleep(0.2)


def run_test(name, func_name, args, expected):
    global total, passed

    total += 1

    if func_name not in globals():
        slow_print(f"[MISSING] {func_name} not implemented yet", NEON_YELLOW, 0.005)
        progress()
        print()
        return

    func = globals()[func_name]

    scan(f"Running {name}")

    try:
        result = func(*args)

        if result == expected:
            passed += 1
            slow_print(f"[OK] {name} {args} -> {result}", NEON_GREEN, 0.003)
        else:
            slow_print(f"[FAIL] {name} {args}", NEON_RED, 0.003)
            slow_print(f"expected : {expected}", NEON_YELLOW, 0.002)
            slow_print(f"got      : {result}", NEON_RED, 0.002)

    except Exception:
        slow_print(f"[CRASH] {name} {args}", NEON_RED, 0.003)
        print(traceback.format_exc())

    progress()
    print()


banner()

# Liste des tests : nom à afficher, nom de la fonction, args, valeur attendue
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

    ("string_permutation_checker abc/cab","string_permutation_checker",("abc","cab"),True),
    ("string_permutation_checker hello/olleh","string_permutation_checker",("hello","olleh"),True),
    ("string_permutation_checker abc/abcc","string_permutation_checker",("abc","abcc"),False),

    ("py_string_sculptor","py_string_sculptor",("Hello World",),"hElLo wOrLd"),

    ("twist_sequence k=1","twist_sequence",([1,2,3,4],1),[4,1,2,3]),
    ("twist_sequence k=2","twist_sequence",([1,2,3,4],2),[3,4,1,2]),

    ("whisper_cipher Hello","whisper_cipher",("Hello",3),"Khoor"),
    ("whisper_cipher abc","whisper_cipher",("abc",1),"bcd"),
]

# Regroupe les tests par fonction
current_section = ""
for t in tests:
    section_name = t[1]
    if section_name != current_section:
        section(section_name + " tests")
        current_section = section_name
    run_test(*t)

print()
slow_print("══════════════════════════════════════", NEON_PINK, 0.002)
slow_print(
    f"PASSED {passed}/{total} TESTS",
    NEON_GREEN if passed == total else NEON_YELLOW,
    0.004
)
slow_print("══════════════════════════════════════", NEON_PINK, 0.002)
print()