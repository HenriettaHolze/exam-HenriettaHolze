# Part 2: Data preprocessing in Python (25%)
# ------------------------------------------------------
# 1
import exam
covid_dict_1 = exam.read_data_1('owid-covid-data.csv')
print(len(covid_dict_1.keys()))

# 2
covid_dict_2 = exam.read_data_2('owid-covid-data.csv')
print(len(covid_dict_2.keys()))