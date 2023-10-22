def mdc(x, y):
    r = x % y
    if r == 0:
        return y
    else:
        return mdc(y, r)
    
num = mdc(15, 10)
print(f"MDC(15, 10): {num}")