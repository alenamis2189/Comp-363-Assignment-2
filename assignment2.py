def add_strings(a, b):
    return str(int(a) + int(b))

def karatsuba_multiplication(x, y):
    n = max(len(x),len(y))

    if n == 1:
        return str(int(x) * int (y))

    m = n // 2

    a = x[:-m] or "0"
    b = x[-m:]
    c = y[:-m] or "0"
    d = y[-m:]

    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)

    a_plus_b = add_strings(a, b)
    c_plus_d = add_strings(c, d)

    ac_bd = karatsuba_multiplication(a_plus_b, c_plus_d)

    ad_plus_bc = str(int(ac_bd) - int(ac) - int(bd))

    term1 = ac + ("0" * (2 * m))
    term2 = ad_plus_bc + ("0" * m)

    return str(int(term1) + int(term2) + int(bd))

# --- quick sanity checks ---
if __name__ == "__main__":
    tests = [
        ("12", "34"),
        ("99", "99"),
        ("0123", "0456"),
        ("1234", "5678"),
        ("0000", "0000"),
        ("1111", "0001"),
        ("1234567890123456", "9876543210123456"),
        ("12345678901234561234567890123456", "12345678901234561234567890123456"),
        ("1234567890123456123456789012345612345678901234561234567890123456", "1234567890123456123456789012345612345678901234561234567890123456"),
    ]

    for x, y in tests:
        # Compare against Python int multiplication for correctness.
        got = karatsuba_multiplication(x, y)
        want = str(int(x) * int(y))
        print(f"{x} * {y} = {got}  (ok={got == want})")
