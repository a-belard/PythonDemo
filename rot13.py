import re


def check_capital(let: str) -> bool:
    return True if ord(let) == ord(let.lower()) else False


def extract_rot13(hashed_str: str) -> str:
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    alphabet_cap: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mystr: str = ""
    for let in hashed_str:
        if re.search(r"[^a-zA-Z]", let):
            mystr += let
            continue
        let_index = alphabet.index(let.lower())
        rot13_index = let_index - 13
        mystr += alphabet[rot13_index] if check_capital(let) else alphabet_cap[rot13_index]
    return mystr


print(extract_rot13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"))