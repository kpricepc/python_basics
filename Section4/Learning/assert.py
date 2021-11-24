# Kelvin to Fahrenheit
def KtoF(Temp):
    assert (Temp >=0), "Colder than 0"
    return((Temp-273)*1.8)+32

print(KtoF(273))
print(int(KtoF(505.78)))
print(KtoF(-5))

