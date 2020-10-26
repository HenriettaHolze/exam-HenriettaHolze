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
print('dates', dates)
print('values', values)

# 3
import matplotlib.pyplot as plt
exam.plot_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
plt.savefig('weekly_cases_cze.png')
