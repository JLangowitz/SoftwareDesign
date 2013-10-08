import math

def complex_mag(c):
    return math.hypot(c.real, c.imag)

def complex_angle(c):
    return math.atan2(c.real, c.imag)

c = complex(3, 4)
print complex_mag(c)
print complex_angle(c)

def signal_noise(signal, noise):
    return 10 * math.log10(float(signal) / noise)

print signal_noise(2, 1)

def binomial_coef(n, k):
    num = math.factorial(n)
    denom = math.factorial(k) * math.factorial(n-k)
    return num / denom

print binomial_coef(10, 3)

def factorial_length(n):
    return len(str(math.factorial(n)))

def factorial_length2(n):
    return (n * math.log(n) - n) / math.log(10)

print factorial_length(100)
print factorial_length2(100)

def triangle(n):
    if not isinstance(n,int) or n<0:
        return "n needs to be a natural number"
    if n == 0:
        return 0
    else:
        return n+triangle(n-1)

print triangle(10)
print triangle(-10)
print triangle(1.50)

