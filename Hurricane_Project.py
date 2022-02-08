# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_damages(damages):
    #purpose of function is to convert the strings in the list"damages" to float so we can perform some financial analysis, where there is no data available keep the string as 'damages not recorded'
    #input to the function is a list of strings
    #use the strip method to remove M and convert to float using the 'conversion' dictionary, do the same for B
    #output is a new list of damages that includes numbers
    monetise_damages = []
    for event in damages:
        if event == "Damages not recorded":
            monetise_damages.append(event)
        elif "M" in event:
            convert_rate = conversion["M"]
            million_event = float(event.strip("M")) * convert_rate
            monetise_damages.append(million_event)
        elif "B" in event:
            convert_rate = conversion["B"]
            billion_event = float(event.strip("B")) * convert_rate
            monetise_damages.append(billion_event)
        else:
            print("check")
    return monetise_damages
# test function by updating damages
print("Task 2: Hurricane damage converted into dollars")
print()
print(convert_damages(damages))
print()

# 2
# Create a Table
# Create and view the hurricanes dictionary
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    sub_dict = {}
    for num in range(len(names)):
        sub_dict[names[num]] = {"Name": names[num], "Month": months[num], "Year": years[num], "Max Sustained Wind": max_sustained_winds[num], "Areas Affected": areas_affected[num], "Damages": damages[num], "Deaths": deaths[num]}
    return sub_dict
print()
print("Task 3: Create a dictionary from the data collected about the 34 strongest Atlantic Hurricanes")
print()
hurricane_dict_by_name = (create_dictionary(names, months, years, max_sustained_winds, areas_affected, convert_damages(damages), deaths))
print(hurricane_dict_by_name)
print()
#print(new_dict.get("Cuba I"))
print()

# 3
# Organizing by Year
def convert_dict_year(input_dict, year):
    #takes the original dictionary which uses the name of the hurrican as the key, converts this to a new dictionary where the key is the year of the hurricane. note the year is a value within a value of the sub-dictionary for each hurricane
    new_key = {}
    for name in input_dict.keys():
        new_key[input_dict.get(name).get(year)] = input_dict.get(name)
    return new_key

print()
# create a new dictionary of hurricanes with year and key
print("Task 4: Convert the Hurricane dictionary and create a new dictionary where 'year' becomes the key instead of name")
print()
hurricane_dict_by_year = convert_dict_year(hurricane_dict_by_name, "Year")
print(hurricane_dict_by_year)
print()
print("Test this function works by calling key = 2018")
print(hurricane_dict_by_year.get(2018, "not found"))
print()
print()

# 4
# Counting Damaged Areas
def area_count(input_dict, areas):
    #create a list of the lists of areas in the dictionary
    areas_list = []
    for name in input_dict.keys():
        areas_list.append([input_dict.get(name).get(areas)])
    #flatten to remove nested lists
    flatten_areas_list = []
    for area in areas_list:
        for location in area:
            for place in location:
                flatten_areas_list.append(place)
    ##create a distinct list of areas from the flattened list
    areas_list = list(dict.fromkeys(flatten_areas_list, {}))
    ##using areas list, iterate through areas_list and count the frequency each area, creating a new list of counts
    count_list = []
    for areas in areas_list:
        count_area = flatten_areas_list.count(areas)
        count_list.append(count_area)
    ##zip together area_list and count_list to create a new dictionary
    area_count_dict = {key:value for key, value in zip(areas_list, count_list)}
    return area_count_dict


# create dictionary of areas to store the number of hurricanes involved in
print("Task 5: Create a dictionary to store the frequency of areas affected by hurricanes:")
print()
areas_affected_dict = area_count(hurricane_dict_by_name, "Areas Affected")
print(areas_affected_dict)
print()
print()

# 5
# Calculating Maximum Hurricane Count
def most_affected(lst):
    # find the max value of all the values and use this as the conditional when iterating over the dictionary of affected areas to find the key:value pair
    all_values = lst.values()
    max_value = max(all_values)
    for key, value in lst.items():
        if value == max_value:
            return key, value
        else:
            continue

print("Task 6: Find out which area has been most affected by hurricanes")
print()
print(most_affected(areas_affected_dict))
print()
print()

# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(lst):
    high = 0
    for key, value in lst.items():
        value_death = (value.get("Deaths"))
        if value_death > high:
            high = value_death
        else:
            continue
    for key, value in lst.items():
        if value.get("Deaths") == high:
            return key, value

print("Task 7: Find out which is the deadliest hurricane i.e. the highest number of deaths")
print()
print(deadliest_hurricane(hurricane_dict_by_name))
print()
print()

# 7
# Rating Hurricanes by Mortality
def create_mortality_dict(input_dict):
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in input_dict.items():
        if value.get("Deaths") > 10000:
            mortality_dict[5].append(value)
        elif 1000 < value.get("Deaths") <= 10000:
            mortality_dict[4].append(value)
        elif 500 < value.get("Deaths") <= 1000:
            mortality_dict[3].append(value)
        elif 100 < value.get("Deaths") <= 500:
            mortality_dict[2].append(value)
        elif 0 < value.get("Deaths") <= 100:
            mortality_dict[1].append(value)
        else:
            mortality_dict[0].append(value)
    return mortality_dict

print("Task 8: Create a new dictionary where the keys are the mortality ratings and the values are the hurricanes that fall into that rating")
print()
hurricanes_by_mortality = create_mortality_dict(hurricane_dict_by_name)
print(hurricanes_by_mortality)
print()
print()

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost

def most_damaging_hurricane(input_dict):
    #find the max damage in dollars and store this in variable 'high'
    high = 0
    for key, value in input_dict.items():
        value_damage = (value.get("Damages"))
        if value_damage == "Damages not recorded":
            continue
        elif value_damage > high:
            high = value_damage
        else:
            continue
    for key, value in input_dict.items():
        if value.get("Damages") == high:
            return key, value


print("Task 9: Find out what the most damaging hurricane in terms of dollars")
print()
print(most_damaging_hurricane(hurricane_dict_by_name))
print()
print()

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
def create_damage_scale_dict(input_dict):
    damage_scale_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in input_dict.items():
        if value.get("Damages") == "Damages not recorded":
            continue
        elif value.get("Damages") > 50000000000:
            damage_scale_dict[5].append(value)
        elif 10000000000 < value.get("Damages") <= 50000000000:
            damage_scale_dict[4].append(value)
        elif 1000000000 < value.get("Damages") <= 10000000000:
            damage_scale_dict[3].append(value)
        elif 100000000 < value.get("Damages") <= 1000000000:
            damage_scale_dict[2].append(value)
        elif 0 < value.get("Damages") <= 100000000:
            damage_scale_dict[1].append(value)
        else:
            damage_scale_dict[0].append(value)
    return damage_scale_dict

print("Task 10: Create a dictionary where the keys are the damage rating (dollars) and values are the corresponding hurricanes")
print()
hurricanes_by_damage_scale = create_damage_scale_dict(hurricane_dict_by_name)
print(hurricanes_by_damage_scale)