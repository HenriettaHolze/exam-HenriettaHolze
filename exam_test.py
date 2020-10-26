# Part 2: Data preprocessing in Python (25%)
# ------------------------------------------------------
# 1
import exam
covid_dict_1 = exam.read_data_1('owid-covid-data.csv')
# print(len(covid_dict_1.keys()))

# 2
covid_dict_2 = exam.read_data_2('owid-covid-data.csv')
# print(len(covid_dict_2.keys()))

# 3
covid_dict_3 = exam.read_data_3('owid-covid-data.csv')
print(covid_dict_3['Denmark']['2020-10-10']['new_cases'])
# 482.0

# Part 3: Analyses 1 (25%)
# ------------------------------------------------------
# 1
print(exam.get_weekly_per_100k_for_country_date(covid_dict_3, "Czech Republic", '2020-10-20'))
# print(exam.get_weekly_per_100k_for_country_date(covid_dict_3, "Aruba", '2020-03-13'))
# No data available for Aruba for 2020-03-13
# None

# 2
dates, values = exam.get_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
# print(exam.get_weekly_per_100k_for_country(covid_dict_3, "Czech Republic"))
# print('dates', dates)
# print('values', values)

# 3
import matplotlib.pyplot as plt
exam.plot_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
plt.savefig('weekly_cases_cze.png')


# Part 4: Analyses 2 - pandas (25%)
# ------------------------------------------------------
# 1
df = exam.read_into_dataframe('owid-covid-data.csv')
df_selected_countries = exam.read_into_dataframe('owid-covid-data.csv',
                                                 ['Austria', 'Belarus', 'Belgium',
						  'Bulgaria', 'Czech Republic', 'Denmark',
						  'Finland', 'France', 'Germany', 'Greece',
						  'Hungary', 'Italy', 'Netherlands', 'Norway',
						  'Poland', 'Portugal', 'Romania', 'Russia',
						  'Serbia', 'Slovakia', 'Spain', 'Sweden',
						  'Switzerland', 'Ukraine', 'United Kingdom',
						  'United States'])


# 2
weekly_per_100k = exam.get_weekly_per_100k(df_selected_countries)

# 3
country_vs_date = exam.get_weekly_per_100k_country_vs_date(weekly_per_100k)

import matplotlib
import numpy as np
import pandas as pd
fig, ax = plt.subplots()
x_vals = matplotlib.dates.date2num(pd.to_datetime(country_vs_date.columns))
aspect_ratio = (country_vs_date.shape[1] /
                country_vs_date.shape[0]*7)
plt.imshow(country_vs_date.values, aspect=aspect_ratio,
           extent=[x_vals[0], x_vals[-1],
                   0, country_vs_date.shape[0]])
ax.xaxis_date()
fig.autofmt_xdate()
ax.set_yticks(np.arange(country_vs_date.values.shape[0])+0.5)
ax.set_yticklabels(country_vs_date.index[::-1])
plt.colorbar()
plt.savefig('weekly_new_cases_per_100k.png')