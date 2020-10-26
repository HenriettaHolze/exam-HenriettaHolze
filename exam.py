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
    # define dict 
    covid_records_per_country = {}

    with open(filename, 'r') as csvfile:
        # skip header/save for later
        header = csvfile.readline().strip().split(',')

        # iterate over lines in csv
        for line in csvfile:
            # csv -> split entries at comma, remove trailing newlines
            entries = line.strip().split(',')

            # convert line into dict with column header as keys and entries as values
            new_entry = {}
            for i, column_name in enumerate(header):
                new_entry[column_name] = entries[i]

            # check if country is already in dict; if not, make new entry, else append (date, new_cases) tuple to country-entry
            if new_entry['location'] not in covid_records_per_country:
                covid_records_per_country[new_entry['location']] = [(new_entry['date'], new_entry['new_cases'])]
            else: 
                covid_records_per_country[new_entry['location']].append((new_entry['date'], new_entry['new_cases']))

    return covid_records_per_country


def read_data_2(filename):
    '''
    reads file, selects entries with valid ISO 3166-1 alpha-3 country code, 
    return a dictionary, where the keys are country names and each value is a list of (date, new_cases) tuples
    '''
    # define dict 
    covid_records_per_country = {}

    with open(filename, 'r') as csvfile:
        # skip header/save for later
        header = csvfile.readline().strip().split(',')

        # iterate over lines in csv
        for line in csvfile:
            # define pattern to check for 3-letter country code
            import re
            regex = '^[a-zA-Z][a-zA-Z][a-zA-Z],'
            pattern = re.compile(regex)

            # check if line matches pattern
            if pattern.match(line):
                # csv -> split entries at comma, remove trailing newlines
                entries = line.strip().split(',')

                # convert line into dict with column header as keys and entries as values
                new_entry = {}
                for i, column_name in enumerate(header):
                    new_entry[column_name] = entries[i]

                # check if country is already in dict; if not, make new entry, else append (date, new_cases) tuple to country-entry
                if new_entry['location'] not in covid_records_per_country:
                    covid_records_per_country[new_entry['location']] = [(new_entry['date'], new_entry['new_cases'])]
                else: 
                    covid_records_per_country[new_entry['location']].append((new_entry['date'], new_entry['new_cases']))

    return covid_records_per_country


def read_data_3(filename):
    '''
    reads file, selects entries with valid ISO 3166-1 alpha-3 country code, 
    return a dictionary of dictionary with structure {country: {date: {header1: ..., header2: ...}}}
    '''
    # define dict 
    covid_records_per_country = {}

    with open(filename, 'r') as csvfile:
        # skip header/save for later
        header = csvfile.readline().strip().split(',')

        # iterate over lines in csv
        for line in csvfile:
            # define pattern to check for 3-letter country code
            import re
            regex = '^[a-zA-Z][a-zA-Z][a-zA-Z],'
            pattern = re.compile(regex)

            # check if line matches pattern
            if pattern.match(line):
                # csv -> split entries at comma, remove trailing newlines
                entries = line.strip().split(',')

                # convert line into dict with column header as keys and entries as values
                new_entry = {}
                for i, column_name in enumerate(header):
                    new_entry[column_name] = entries[i]
                
                # check if country is already in dict; if not, make new entry, else create new entry for specific date
                # There should not be 2 entries for the same country and the same date -> no need to check whether date exists already
                if new_entry['location'] not in covid_records_per_country:
                    covid_records_per_country[new_entry['location']] = {new_entry['date']: new_entry}
                else: 
                    covid_records_per_country[new_entry['location']][new_entry['date']] = new_entry

    return covid_records_per_country

