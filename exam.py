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


# Part 3: Analyses 1 (25%)
# ------------------------------------------------------
# 1
def get_weekly_per_100k_for_country_date(covid_data: dict, country_name: str, date: str):
    '''takes a dict with covid data, a country name and a date,
    returns estimated number of cases per week
    '''
    # check if entry is not empty, assumes that keys exist
    assert covid_data[country_name][date]['new_cases_smoothed_per_million'] != ''

    # find the relevant data entry with country name and date
    new_cases_smoothed_per_million = covid_data[country_name][date]['new_cases_smoothed_per_million']
    # estimate weekly cases and rescale to 100k
    weekly_per_100k = float(new_cases_smoothed_per_million) * 7 / 10
    return weekly_per_100k


# 2
def get_weekly_per_100k_for_country(covid_data: dict, country_name: str):
    '''
    returns list of dates and list of weekly-per-100k values for a country
    '''
    from datetime import datetime 

    # create list with all dates available for that country in the dict
    dates_in_dict = list(covid_data[country_name].keys())

    dates = []
    values = []
    
    for date in dates_in_dict:
        # check if data is available for that country and date, if yes, append to lists and convert datetime
        try:
            values.append(get_weekly_per_100k_for_country_date(covid_data, country_name, date))
            dates.append(datetime.strptime(date, "%Y-%m-%d"))
        except Exception as e:
            print(e)

    return dates, values


def plot_weekly_per_100k_for_country(covid_data: dict, country_name: str):
    '''
    plot weekly cases per 100k over time for country
    '''

    # get data
    dates, values = get_weekly_per_100k_for_country(covid_data, country_name)

    import matplotlib.pyplot as plt 
    from matplotlib.dates import MonthLocator

    # initiate plot
    fig, ax = plt.subplots()

    # create plot with data
    ax.plot(dates, values)
    # add horizontal dotted line for open-country limit
    ax.axhline(y=20, linestyle='dotted')

    # one tick per month and improve layout
    ax.xaxis.set_major_locator(MonthLocator())
    fig.autofmt_xdate()

    # set ax titles and figure title 
    ax.set(xlabel='time', ylabel='new weekly cases (per 100k)', title='Weekly cases per 100k for {}'.format(country_name))

    # plt.show()


# should we raise the exception only if date & country not in dict (KeyError) or also or only for empty entries (ValueError)?
# Is type checking ok?
# question: should we convert entries to integers?
# where import libraries? 
# do we have to include wget datafile in unix part?


# Part 4: Analyses 2 - pandas (25%)
# ------------------------------------------------------
# 1
def read_into_dataframe(filename: str, countries: list = None):
    '''
    read date into pandas df and filter for correct country code and optionally a list of countries
    '''
    import pandas as pd 
    df = pd.read_csv(filename)

    import re
    regex = '^[a-zA-Z][a-zA-Z][a-zA-Z]$'
    pattern = re.compile(regex)

    mask_iso = df['iso_code'].str.match(pattern)
    mask_nan = ~pd.isna(df['iso_code'])

    df_filtered = df[mask_iso & mask_nan]

    # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame.
    df_filtered.loc[:, 'date'] = pd.to_datetime(df_filtered.loc[:, 'date'])

    if countries != None:
        df_filtered = df_filtered[df_filtered['location'].isin(countries)]

    return df_filtered


def get_weekly_per_100k(df):
    '''
    returns dataframe with weekly sum of cases
    '''
    import pandas as pd
    import numpy as np 

    # Change the index of the dataframe to be the date column
    df = df.set_index('date')

    # reduce the dataframe to only weekly entries, consisting of the average for that week, multiplied by 7 
    df_resampled = df.groupby('location').resample('W').mean() * 7

    # Reset the index on the resulting data frame to get back the date and location columns
    df_resampled = df_resampled.reset_index()

    # return a dataframe that only consists of three columns: location, date and weekly_new_cases_per_100k, 
    # where the latter is based on the averaged new_cases_per_million column, but scaled to be per 100,000 
    # instead of per million.
    weekly_per_100k = df_resampled[['location', 'date']]

    # SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame.
    weekly_per_100k['weekly_new_cases_per_100k'] = df_resampled['new_cases_per_million'] / 10

    return weekly_per_100k


# 3
def get_weekly_per_100k_country_vs_date(df):
    '''
    pivot dataframe so that rows are countries and columns are dates
    '''
    import pandas as pd
    df_pivoted = pd.pivot_table(df, values='weekly_new_cases_per_100k', index=['location'], columns=['date'])
    return df_pivoted