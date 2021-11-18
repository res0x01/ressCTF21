from Crypto.Util.number import long_to_bytes, bytes_to_long, getStrongPrime

with open("flag.txt", "rb") as f:
    flag = f.read().strip()

m = bytes_to_long(flag)

p = getStrongPrime(1024)
q = getStrongPrime(1024)

N = p*q
e = 2 
assert pow(m,e) < N

C = pow(m,e,N)
with open("output.txt", "w") as f:
    f.write(f"{C}")
