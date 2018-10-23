def celsiusToFahr(tempC):
    return 9/5 * tempC + 32

def kelvinsToCelsius(tempK):
    return tempK - 273.15

def hello(name, age):
    return 'Hello '+name+ ' I am ' +str(age)+ ' years old'

def kelvinsToFahr (tempK):
    tempC = kelvinsToCelsius(tempK)
    tempFahr = celsiusToFahr(tempC)
    return tempFahr

