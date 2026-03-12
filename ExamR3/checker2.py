"""
╔══════════════════════════════════════════════════════════════════╗
║          TEST RUNNER — exercises.py — 42 Python Exam            ║
║  Usage : python test_runner.py                                   ║
║  Requis: exercises.py dans le même dossier                       ║
╚══════════════════════════════════════════════════════════════════╝
"""

import json
import sys
import time
import traceback
import os

# ─── ANSI COLORS ───────────────────────────────────────────────────
R  = "\033[0m"
BOLD = "\033[1m"
DIM  = "\033[2m"

CYAN    = "\033[96m"
PINK    = "\033[95m"
GREEN   = "\033[92m"
RED     = "\033[91m"
YELLOW  = "\033[93m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"
GREY    = "\033[90m"

BG_DARK  = "\033[40m"

def c(text, color, bold=False):
    return f"{BOLD if bold else ''}{color}{text}{R}"

def fmt(v):
    """Format a value for display."""
    if v is None:
        return c("None", PINK)
    if isinstance(v, bool):
        return c(str(v), GREEN if v else RED)
    if isinstance(v, str):
        return c(f'"{v}"', CYAN)
    if isinstance(v, list):
        inner = ", ".join(fmt(x) for x in v)
        return c("[", GREY) + inner + c("]", GREY)
    return c(str(v), YELLOW)

def fmt_args(args):
    return ", ".join(fmt(a) for a in args)

def deep_equal(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, list):
        if len(a) != len(b):
            return False
        return all(deep_equal(x, y) for x, y in zip(a, b))
    return a == b

# ─── TEST SUITE ────────────────────────────────────────────────────

TEST_SUITE = [
    {
        "name": "brackets",
        "tests": [
            (["()"],           True,  "simple parenthèses"),
            (["([])"],         True,  "imbriqués"),
            (["{[]}"],         True,  "accolades + crochets"),
            (["([)]"],         False, "mauvais ordre"),
            (["(]"],           False, "mauvaise correspondance"),
            ([""],             True,  "string vide"),
            (["({[]})"],       True,  "triple imbrication"),
            (["((()))"],       True,  "trois paires imbriquées"),
            (["((("],          False, "jamais fermé"),
            ([")))"],          False, "closing sans opening"),
            (["abc(def)ghi"],  True,  "texte autour des brackets"),
            (["hello"],        True,  "aucun bracket"),
            (["{([])}"],       True,  "imbrication complexe"),
            (["{[}]"],         False, "entrelacement invalide"),
            (["["],            False, "un seul ouvert"),
            (["[](){}"],       True,  "trois paires séquentielles"),
            (["[({})]"],       True,  "imbrication profonde"),
        ],
    },
    {
        "name": "echo_validator",
        "tests": [
            (["Radar"],                         True,  "palindrome basique"),
            (["A man a plan a canal Panama"],   True,  "phrase sans ponctuation"),
            (["Hello"],                         False, "non-palindrome"),
            (["racecar"],                       True,  "lowercase palindrome"),
            ([""],                              True,  "string vide"),
            (["a"],                             True,  "un seul caractère"),
            (["Aa"],                            True,  "insensible à la casse"),
            (["Was it a car or a cat I saw"],   True,  "phrase palindrome"),
            (["Not a palindrome"],              False, "phrase normale"),
            (["12321"],                         True,  "chiffres ignorés → vide = palindrome"),
            (["Madam"],                         True,  "Madam"),
            (["Never odd or even"],             True,  "phrase palindrome 2"),
            (["ab"],                            False, "deux chars différents"),
            (["abba"],                          True,  "abba"),
        ],
    },
    {
        "name": "matrix_reverse",
        "tests": [
            ([[[1,2,3],[4,5,6]]],         [[3,2,1],[6,5,4]], "matrice 2x3"),
            ([[[1,2],[3,4]]],              [[2,1],[4,3]],     "matrice 2x2"),
            ([[[1]]],                      [[1]],             "matrice 1x1"),
            ([[]],                         [],                "matrice vide"),
            ([[[5,4,3,2,1]]],              [[1,2,3,4,5]],    "une seule ligne"),
            ([[[1],[2],[3]]],              [[1],[2],[3]],     "une colonne"),
            ([[[9,8,7],[6,5,4],[3,2,1]]], [[7,8,9],[4,5,6],[1,2,3]], "matrice 3x3"),
            ([[[1,2,3,4]]],               [[4,3,2,1]],       "4 éléments"),
            ([[[1,2],[3,4],[5,6]]],        [[2,1],[4,3],[6,5]], "matrice 3x2"),
            ([[[0,0],[0,0]]],              [[0,0],[0,0]],     "tous zéros"),
        ],
    },
    {
        "name": "pattern_tracker",
        "tests": [
            (["123"],          2, "123 → 2 paires"),
            (["1293"],         1, "reset par non-consécutif"),
            (["a123b45"],      3, "non-digit reset"),
            (["12345"],        4, "séquence longue"),
            ([""],             0, "string vide"),
            (["abc"],          0, "que des lettres"),
            (["1"],            0, "un seul chiffre"),
            (["11"],           0, "mêmes chiffres (non +1)"),
            (["21"],           0, "décroissant"),
            (["0123456789"],   9, "0 à 9 complet"),
            (["1a2b3"],        0, "chaque reset par lettre"),
            (["99"],           0, "9→9 pas +1"),
            (["89"],           1, "8→9 c'est +1"),
            (["a12bc34de56"], 3, "3 séquences séparées"),
        ],
    },
    {
        "name": "number_base_converter",
        "tests": [
            (["101", 2, 10],    "5",     "binaire → décimal"),
            (["FF", 16, 10],    "255",   "hex → décimal"),
            (["255", 10, 16],   "FF",    "décimal → hex"),
            (["XYZ", 10, 2],    "ERROR", "char invalide"),
            (["0", 10, 2],      "0",     "zéro"),
            (["Z", 36, 10],     "35",    "base 36 → Z = 35"),
            (["10", 8, 10],     "8",     "octal 10 → décimal 8"),
            (["A", 10, 2],      "ERROR", "A invalide en base 10"),
            (["1111", 2, 16],   "F",     "binaire 1111 → hex F"),
            (["10", 2, 8],      "2",     "binaire → octal"),
            (["G", 16, 10],     "ERROR", "G invalide en hex"),
            (["1", 10, 2],      "1",     "1 en binaire"),
            (["100", 10, 10],   "100",   "même base"),
            (["1A", 16, 10],    "26",    "1A hex → 26"),
            (["777", 8, 10],    "511",   "octal 777"),
        ],
    },
    {
        "name": "shadow_merge",
        "tests": [
            ([[3,1,5],[2,4]],         [1,2,3,4,5],         "exemple de base"),
            ([[],[1,2]],               [1,2],               "liste1 vide"),
            ([[1,2],[]],               [1,2],               "liste2 vide"),
            ([[], []],                 [],                  "deux listes vides"),
            ([[5,5],[5]],             [5,5,5],              "doublons"),
            ([[1],[2]],               [1,2],                "un élément chacun"),
            ([[10,5,1],[9,3,7]],      [1,3,5,7,9,10],      "mélangé"),
            ([[-3,-1,2],[-5,0,4]],   [-5,-3,-1,0,2,4],    "négatifs"),
            ([[100],[1]],             [1,100],              "grand écart"),
            ([[1,3,5,7],[2,4,6,8]],  [1,2,3,4,5,6,7,8],  "alternés parfaits"),
            ([[9,8,7,6,5],[4,3,2,1,0]], [0,1,2,3,4,5,6,7,8,9], "inversés"),
        ],
    },
    {
        "name": "string_permutation_checker",
        "tests": [
            (["abc","cab"],     True,  "permutation simple"),
            (["hello","olleh"], True,  "hello inversé"),
            (["abc","abcc"],    False, "longueurs différentes"),
            (["",""],           True,  "deux strings vides"),
            (["a","a"],         True,  "même caractère"),
            (["ab","ba"],       True,  "swap 2 chars"),
            (["aab","aba"],     True,  "avec doublons"),
            (["abc","def"],     False, "chars complètement différents"),
            (["aab","aac"],     False, "même longueur, char diff"),
            (["abcd","dcab"],   True,  "4 chars permutés"),
            (["a","b"],         False, "chars différents courts"),
            (["listen","silent"], True, "listen / silent"),
            (["abc","ab"],      False, "longueur différente"),
            (["aaa","aab"],     False, "fréquence différente"),
        ],
    },
    {
        "name": "py_string_sculptor",
        "tests": [
            (["Hello World"],   "hElLo WoRlD", "exemple de base"),
            ([""],              "",            "string vide"),
            (["a"],             "a",           "un char (index 0 → lower)"),
            (["ab"],            "aB",          "deux chars"),
            (["abc"],           "aBc",         "trois chars"),
            (["HELLO"],         "hElLo",       "all caps input"),
            (["hello"],         "hElLo",       "all lowercase input"),
            (["hello world"],   "hElLo WoRlD", "avec espace (ignoré pour l'index)"),
            (["a1b2c3"],        "a1B2c3",      "chiffres ignorés pour l'index"),
            (["123"],           "123",         "que des chiffres"),
            (["H3llo W0rld"],   "h3LlO w0RlD", "alphanum mixte"),
            (["a!b@c#"],        "a!B@c#",      "caractères spéciaux ignorés"),
        ],
    },
    {
        "name": "twist_sequence",
        "tests": [
            ([[1,2,3,4], 1],    [4,1,2,3],   "k=1"),
            ([[1,2,3,4], 2],    [3,4,1,2],   "k=2"),
            ([[1,2,3,4], 0],    [1,2,3,4],   "k=0"),
            ([[1,2,3,4], 4],    [1,2,3,4],   "k=n (cycle complet)"),
            ([[1,2,3,4], 5],    [4,1,2,3],   "k>n (mod)"),
            ([[], 3],            [],           "liste vide"),
            ([[1], 1],           [1],          "un seul élément"),
            ([[1,2], 1],         [2,1],        "deux éléments k=1"),
            ([[5,1,3,2,4], 3],  [3,2,4,5,1], "5 éléments k=3"),
            ([[1,2,3], 6],      [1,2,3],      "k=2n (double cycle)"),
            ([[1,2,3,4,5], 5],  [1,2,3,4,5], "k=n=5"),
            ([[10,20,30], 1],   [30,10,20],   "3 éléments k=1"),
        ],
    },
    {
        "name": "whisper_cipher",
        "tests": [
            (["Hello", 3],       "Khoor",       "exemple de base Caesar +3"),
            (["abc", 1],         "bcd",         "shift 1"),
            (["xyz", 3],         "abc",         "wrap alphabet"),
            (["Hello", 0],       "Hello",       "shift 0 = identique"),
            (["ABC", 26],        "ABC",         "shift 26 = cycle complet"),
            (["Hello World", 13],"Uryyb Jbeyq", "ROT13"),
            (["z", 1],           "a",           "z → a wrap"),
            (["a b c", 1],       "b c d",       "espaces préservés"),
            (["Hello123", 3],    "Khoor123",    "chiffres inchangés"),
            (["", 5],            "",            "string vide"),
            (["ZzAa", 1],        "AaBb",        "casse préservée + wrap"),
            (["abc", -1],        "zab",         "shift négatif"),
            (["Hello", 52],      "Hello",       "shift 52 = 2 cycles"),
            (["Xyz", 3],         "Abc",         "fin d'alphabet + casse"),
        ],
    },
    {
    "name": "cryptic_sorter",
    "tests": [
        ([["apple", "cat", "banana", "dog", "elephant"]], ["cat", "dog", "apple", "banana", "elephant"], "exemple de base"),
        ([["aaa", "bbb", "AAA", "BBB"]],                  ["AAA", "aaa", "BBB", "bbb"],                  "casse insensible"),
        ([["hello", "world", "hi", "test"]],              ["hi", "test", "hello", "world"],              "longueurs mixtes"),
        ([[]],                                             [],                                            "liste vide"),
        ([[""]],                                          [""],                                           "string vide"),
        ([["b", "a", "c"]],                               ["a", "b", "c"],                               "tri alpha même longueur"),
        ([["bb", "aa", "a", "b"]],                        ["a", "b", "aa", "bb"],                        "longueurs 1 et 2"),
        ([["aei", "bcd"]],                                ["aei", "bcd"],                                "même longueur, tri par voyelles"),
        ([["AEI", "bcd"]],    ["AEI", "bcd"],  "voyelles en majuscules"),
        ([["dog", "cat", "ant"]],                         ["ant", "cat", "dog"],                         "même longueur tri alpha"),
        ([["z", "a", "m"]],                               ["a", "m", "z"],                               "un char chacun"),
        ([["abc"]],                                       ["abc"],                                        "un seul élément"),
        ([["banana", "apple", "cherry"]],                 ["apple", "banana", "cherry"],                  "longueurs 5-6"),
        ([["!!!", "aaa", "bbb"]], ["!!!", "aaa", "bbb"], "caractères spéciaux"),
    ],
},
]

# ─── RUNNER ────────────────────────────────────────────────────────

def run_tests():
    # Banner
    print()
    print(c("╔" + "═"*66 + "╗", CYAN))
    print(c("║", CYAN) + c("  ░▒▓  TEST RUNNER  ▓▒░  exercises.py  ·  42 Python Exam       ", PINK, bold=True) + c("  ║", CYAN))
    print(c("╚" + "═"*66 + "╝", CYAN))
    print()

    # Import exercises
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("exercises", os.path.join(os.path.dirname(__file__), "exercises.py"))
        exercises = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(exercises)
    except FileNotFoundError:
        print(c("  ✗ ERREUR: exercises.py introuvable dans le même dossier.", RED, bold=True))
        print(c("  → Lance ce script depuis le dossier qui contient exercises.py", GREY))
        sys.exit(1)
    except SyntaxError as e:
        print(c(f"  ✗ ERREUR DE SYNTAXE dans exercises.py:", RED, bold=True))
        print(c(f"    {e}", YELLOW))
        sys.exit(1)

    total = 0
    total_pass = 0
    total_fail = 0
    total_skip = 0
    results_summary = []

    for suite in TEST_SUITE:
        fn_name = suite["name"]
        tests   = suite["tests"]
        fn = getattr(exercises, fn_name, None)

        # Header function
        print(c("┌─", CYAN) + c(f" {fn_name}", WHITE, bold=True))

        fn_pass = 0
        fn_fail = 0
        fn_skip = 0

        for args, expected, label in tests:
            total += 1
            prefix = c("│", CYAN) + "  "

            if fn is None:
                fn_skip += 1
                total_skip += 1
                print(prefix + c("⚠ SKIP", YELLOW) + c(f"  {label}", GREY) +
                      c(f"  [fonction non implémentée]", DIM + GREY))
                continue

            try:
                t0 = time.perf_counter()
                got = fn(*args)
                elapsed = (time.perf_counter() - t0) * 1000

                if deep_equal(got, expected):
                    fn_pass += 1
                    total_pass += 1
                    timing = c(f"  {elapsed:.2f}ms", DIM + GREY)
                    print(prefix + c("✓ PASS", GREEN) +
                          c(f"  {label}", GREY) + timing)
                else:
                    fn_fail += 1
                    total_fail += 1
                    print(prefix + c("✗ FAIL", RED, bold=True) +
                          c(f"  {label}", WHITE))
                    print(prefix + c("  args    : ", GREY) + fmt_args(args))
                    print(prefix + c("  expected: ", GREY) + fmt(expected))
                    print(prefix + c("  got     : ", GREY) + fmt(got))

            except Exception as e:
                fn_fail += 1
                total_fail += 1
                tb = traceback.format_exc().strip().split('\n')[-1]
                print(prefix + c("✗ ERROR", RED, bold=True) +
                      c(f"  {label}", WHITE))
                print(prefix + c("  args    : ", GREY) + fmt_args(args))
                print(prefix + c("  expected: ", GREY) + fmt(expected))
                print(prefix + c(f"  error   : {tb}", YELLOW))

        # Footer function
        fn_total = fn_pass + fn_fail + fn_skip
        if fn is None:
            status_str = c("⚠ NOT IMPLEMENTED", YELLOW)
        elif fn_fail == 0:
            status_str = c(f"✓ {fn_pass}/{fn_total} PASSED", GREEN, bold=True)
        else:
            status_str = c(f"✗ {fn_fail}/{fn_total} FAILED", RED, bold=True)

        print(c("└─", CYAN) + c(f" [{fn_name}] ", GREY) + status_str)
        print()
        results_summary.append((fn_name, fn_pass, fn_fail, fn_skip, fn is not None))

    # ─── FINAL SUMMARY ───────────────────────────────────────────
    pct = int((total_pass / total) * 100) if total > 0 else 0
    bar_len = 40
    filled = int(bar_len * total_pass / total) if total > 0 else 0
    bar = c("█" * filled, GREEN) + c("░" * (bar_len - filled), GREY)

    print(c("═"*68, CYAN))
    print(c("  RÉSULTATS FINAUX", WHITE, bold=True))
    print(c("─"*68, GREY))
    print()

    # Per-function summary table
    print(f"  {'FONCTION':<32} {'PASS':>6} {'FAIL':>6} {'SKIP':>6}  STATUS")
    print(c("  " + "─"*62, GREY))
    for fn_name, fp, ff, fs, implemented in results_summary:
        if not implemented:
            status = c("⚠ NOT IMPL", YELLOW)
        elif ff == 0:
            status = c("✓ OK", GREEN)
        else:
            status = c("✗ KO", RED)
        fn_total = fp + ff + fs
        pass_str = c(str(fp), GREEN) if fp > 0 else c("0", GREY)
        fail_str = c(str(ff), RED) if ff > 0 else c("0", GREY)
        skip_str = c(str(fs), YELLOW) if fs > 0 else c("0", GREY)
        print(f"  {c(fn_name, CYAN):<42} {pass_str:>15} {fail_str:>15} {skip_str:>15}  {status}")

    print()
    print(c("─"*68, GREY))
    print(f"  {bar}  {c(str(pct)+'%', PINK, bold=True)}")
    print()
    print(f"  {c('Total  :', GREY)} {c(str(total), WHITE, bold=True)} tests")
    print(f"  {c('Passed :', GREY)} {c(str(total_pass), GREEN, bold=True)}")
    print(f"  {c('Failed :', GREY)} {c(str(total_fail), RED, bold=True)}")
    print(f"  {c('Skipped:', GREY)} {c(str(total_skip), YELLOW, bold=True)}")
    print()

    if total_fail == 0 and total_skip == 0:
        print(c("  ★  PARFAIT — TOUTES LES FONCTIONS PASSENT !  ★", GREEN, bold=True))
    elif total_fail == 0:
        print(c(f"  ✓  Aucun échec ! ({total_skip} fonctions non implémentées)", YELLOW, bold=True))
    else:
        print(c(f"  ✗  {total_fail} test(s) échoué(s). Courage !", RED))

    print()
    print(c("═"*68, CYAN))
    print()

if __name__ == "__main__":
    run_tests()
