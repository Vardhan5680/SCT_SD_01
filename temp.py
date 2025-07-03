def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()

    if from_scale == to_scale:
        return value

    # Convert input to Celsius first
    if from_scale == "celsius":
        celsius = value
    elif from_scale == "fahrenheit":
        celsius = fahrenheit_to_celsius(value)
    elif from_scale == "kelvin":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError("Invalid input scale")

    # Convert from Celsius to target scale
    if to_scale == "celsius":
        return celsius
    elif to_scale == "fahrenheit":
        return celsius_to_fahrenheit(celsius)
    elif to_scale == "kelvin":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError("Invalid target scale")

# Example usage:
if __name__ == "__main__":
    try:
        value = float(input("Enter temperature value: "))
        from_scale = input("Enter input scale (Celsius, Fahrenheit, Kelvin): ")
        to_scale = input("Enter target scale (Celsius, Fahrenheit, Kelvin): ")
        result = convert_temperature(value, from_scale, to_scale)
        print(f"{value}° {from_scale.capitalize()} is {result:.2f}° {to_scale.capitalize()}")
    except ValueError as e:
        print("Error:", e)