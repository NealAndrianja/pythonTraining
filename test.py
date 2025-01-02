# Converts from celcius to fahrenheit

def c_to_f(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

def main():
    celcius=float(input("Enter temperature in Celcius: "))
    fahrenheit=c_to_f(celcius)
    print(f"{celcius}°C is equal to {fahrenheit}°F")

main()