
def temp(usr_inp1, usr_inp2, value1):
    if (usr_inp1 == 'celsius'):
        if (usr_inp2 == 'kelvin'):
            output = value1 + 273
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")
        else:
            output = 1.8*value1 + 32
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")

    elif (usr_inp1 == 'fahrenheit'):
        if (usr_inp2 == 'celsius'):
            output = (5/9)*(value1-32)
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")
        else:
            output = (5/9)*(value1-32) + 273     
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")

    else:
        if (usr_inp2 == 'celsius'):
            output = value1 - 273
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")
        else:
            c = value1 - 273
            output = 1.8*c + 32
            print(f"{value1} {usr_inp1} tp {usr_inp2} is {output}")


def Mass(usr_inp1, usr_inp2, value1):
    
    flag1 = False
    flag2 = False

    for key in gram_converter.keys():
        if usr_inp1 == key:
            flag1 = True
        if usr_inp2 == key:
            flag2 = True
    
    if flag1 == True and flag2 == True:
        temp = value1
        value1 = value1 * (gram_converter[usr_inp1]/gram_converter[usr_inp2])
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")

    elif flag1 == True:
        temp = value1
        value1 = value1 * gram_converter[usr_inp1] * gram_to_other[usr_inp2] # convert to grams then to other by multiplying factors
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")

    elif flag2 == True:
        temp = value1
        value1 = value1 / gram_to_other[usr_inp1] # convert to gram
        value1 = value1 / gram_converter[usr_inp2] # convert to desired output
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")
    
    else: 
        temp = value1
        value1 = value1 / gram_to_other[usr_inp1] # input to gram
        value1 = value1 * gram_to_other[usr_inp2] # grams to output
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")


def length(usr_inp1, usr_inp2, value1):
     
    flag1 = False
    flag2 = False

    for key in meter_convert.keys():
        if usr_inp1 == key:
            flag1 = True
        if usr_inp2 == key:
            flag2 = True

    if flag1 == True and flag2 == True: 
        temp = value1
        value1 = value1 * (meter_convert[usr_inp1]/meter_convert[usr_inp2]) # convert to desired output by multiplying conversion factor
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")

    elif flag1 == True:
        temp = value1
        value1 = value1 * (meter_convert[usr_inp1]/meter_convert['meter']) # we multiply by conversion factor to convert to meter
        #print(value1)
        value1 = value1 * meter_to_other[usr_inp2]
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")
    
    elif flag2 == True:
        temp = value1
        value1 = value1 / (meter_to_other[usr_inp1]) # now other value converted to meter
        value1 = value1 / meter_convert[usr_inp2] # meter to desired output
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1}")
                                                                                                               
    else:
        temp = value1
        value1 = value1 / (meter_to_other[usr_inp1]) # convert input to meter
        value1 = value1 * meter_to_other[usr_inp2] # meter to desired output
        print(f"{temp} {usr_inp1} to {usr_inp2} is {value1}")

def Time(usr_inp1, usr_inp2, value1):
    temp = value1
    value1 = value1 * (hour_to_other[usr_inp2]/hour_to_other[usr_inp1])
    print(f"{temp} {usr_inp1} to {usr_inp2} is {value1} {usr_inp2}")
    

def Speed(usr_inp1, value1):
    pass
        
# conversion factor dicts   
meter_convert = {'millimeter':0.001, 'centimeter':0.01, 'decimeter': 0.1, 'meter':1, 'kilometer':1000}
meter_to_other = {'mile': 0.00062137273, 'inch': 39.37, 'yard': 1.09361, 'foot': 3.281}  

gram_converter = {'milligram': 0.001, 'gram': 1, 'kilogram': 1000}
gram_to_other = {'pound': 0.00220462262, 'ounce': 0.035274, 'stone': 0.00015747}

hour_to_other = {'milliseconds': 3.6*10**6, 'seconds': 3600, 'minute': 60, 'hour': 1, 'day': 0.04166666666, 'week': 0.00595238095, 'month': 0.00136986301, 'year': 0.00011415525}

speed = {
        'KiloMeters per Hour to Miles per Hour': 1,
        'Miles per Hour to KiloMeters per Hour': 2,
        'KiloMeters per Hour to Meters per Second': 3,
        'Meters per Second to KiloMeters per Second': 4, 
        'Miles per Hour to Meters per Second': 5,
        'Meters per Second to Miles per Hour': 6
    }


# initial User Input
init_input = input("What conversion woudl you like to do, Temperature, Mass, Speed, Length, or Time: ")
init_input.lower()




if (init_input.lower() == 'temperature'):
    print('choose from following units')
    print('\n')
    print('Celsius', 'Fahrenheit', 'Kelvin')

    usr_inp1 = input("What is your input unit (enter full): ")
    usr_inp2 = input("What is your desired output unit(enter full): ")
    print(f"What is the value of {usr_inp1}: ")
    value1 = float(input()) 

    temp(usr_inp1.lower(), usr_inp2.lower(), value1)

elif init_input.lower() == 'length':
    print('choose from following units')
    print('\n')
    for keys in meter_convert.keys():
        print(keys)
    for keys in meter_to_other.keys():
        print(keys)
    
    usr_inp1 = input("What is your input unit (enter full): ")
    usr_inp2 = input("What is your desired output unit(enter full): ")
    print(f"What is the value of {usr_inp1}: ")
    value1 = float(input()) 

    length(usr_inp1.lower(), usr_inp2.lower(), value1)

elif init_input.lower() == 'mass':
    print('choose from following units')
    print('\n')
    for keys in gram_converter.keys():
        print(keys)
    for keys in gram_to_other.keys():
        print(keys)

    usr_inp1 = input("What is your input unit (enter full): ")
    usr_inp2 = input("What is your desired output unit(enter full): ")
    print(f"What is the value of {usr_inp1}: ")
    value1 = float(input())

    Mass(usr_inp1.lower(), usr_inp2.lower(), value1)

elif init_input.lower() == 'time':
    print('choose from following units')
    print('\n')
    for keys in hour_to_other.keys():
        print(keys)
    
    usr_inp1 = input("What is your input unit (enter full): ")
    usr_inp2 = input("What is your desired output unit(enter full): ")
    print(f"What is the value of {usr_inp1}: ")
    value1 = float(input())

    Time(usr_inp1.lower(), usr_inp2.lower(), value1)

elif init_input.lower() == 'speed':
    print('Please choose corrosponding number to conversion')
    for keys in speed.items():
        print(keys)
    usr_inp1 = input(": ")
    print(f"What is the value of {usr_inp1}: ")
    value1 = float(input())

    
    Speed(usr_inp1, value1)

else:
    print('Sorry, your input caused me to crash :(')
