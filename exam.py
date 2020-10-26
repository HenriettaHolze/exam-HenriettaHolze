# Part 2: Data preprocessing in Python (25%)
# ------------------------------------------------------
# 1
# country name: column 3
# date:         column 4
# new_cases:    column 6 
def read_data_1(filename):
    '''
    reads file, 
    return a dictionary, where the keys are country names and each value is a list of (date, new_cases) tuples
    '''
    covid_records_per_country = {}
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            # csv -> split entries at comma
            entries = line.split(',')
            # assign each value to variable for readability
            country_name = entries[2]
            date = entries[3]
            new_cases = entries[5]
            # check if country is already in dict; if not, make new entry, else append to entry
            if country_name not in covid_records_per_country:
                covid_records_per_country[country_name] = [(date, new_cases)]
            else: 
                covid_records_per_country[country_name].append((date, new_cases))

    return covid_records_per_country


def read_data_2(filename):
    '''
    reads file, selects entries with valid ISO 3166-1 alpha-3 country code, 
    return a dictionary, where the keys are country names and each value is a list of (date, new_cases) tuples
    '''
    covid_records_per_country = {}
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            # define pattern to check for 3-letter country code
            import re
            regex = '^[a-zA-Z][a-zA-Z][a-zA-Z],'
            pattern = re.compile(regex)
            # check if line matches pattern
            if pattern.match(line):
                entries = line.split(',')
                country_name = entries[2]
                date = entries[3]
                new_cases = entries[5]
                if country_name not in covid_records_per_country:
                    covid_records_per_country[country_name] = [(date, new_cases)]
                else: 
                    covid_records_per_country[country_name].append((date, new_cases))

    return covid_records_per_country

