import sys
import re
import pytest
import os

def setup_module(module):
    """ setup any state specific to the execution of the given module."""

    if not os.path.exists('owid-covid-data.csv'):
        os.system('wget https://github.com/owid/covid-19-data/raw/69de52175d96f7badcc7ec58ca910d091ca0fd0e/public/data/owid-covid-data.csv')

@pytest.mark.skipif(sys.platform == "win32", reason="Tests cannot be executed on windows")
class TestUnixPart:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""

        pexpect = pytest.importorskip("pexpect")
        # Import pywrapper (complication due to dot in directory name)
        import importlib
        spec = importlib.util.spec_from_file_location('sh_pywrapper', '.testsetup/sh_pywrapper.py')
        cls.sh_pywrapper = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.sh_pywrapper)

        cls.process = cls.sh_pywrapper.create_process()
        cls.base_dir = os.path.abspath(cls.sh_pywrapper.get_cwd(cls.process)).strip()

    @classmethod
    def teardown_class(cls):
        """ teardown any state specific to the execution of the given class."""

        pytestmark = pytest.mark.skipif(sys.platform == "win32", reason="tests for linux only")
        pexpect = pytest.importorskip("pexpect")
        cls.sh_pywrapper.kill_process(cls.process)

    @classmethod
    def unix_command_check(cls, exercise_number):

        # Test for existance of Unix command file
        commands_list = cls.sh_pywrapper.parse('exam.sh')

        non_empty_commands_list = []
        for command in commands_list:
            non_empty_commands_list.append([])
            for line in command:
                if line[0] != "#":
                    non_empty_commands_list[-1].append(line)
        
        # Test that there are at least n commands
        assert len(commands_list) >= exercise_number, "No commands found at index {}".format(exercise_number)
        assert len(commands_list[exercise_number - 1]) > 0, "No commands found at index {}".format(exercise_number)
        assert len(non_empty_commands_list[exercise_number - 1]) > 0, "No commands found at index {}".format(exercise_number)

        # Run command
        return cls.sh_pywrapper.run(cls.process, commands_list[exercise_number - 1])

    def test_ex1_1_basic(cls):
        '''Test that command exists in .sh file'''
        cls.unix_command_check(1)

    def test_ex1_2_basic(cls):
        '''Test that command exists in .sh file'''
        cls.unix_command_check(2)

    def test_ex1_3_basic(cls):
        '''Test that command exists in .sh file'''
        cls.unix_command_check(3)

    def test_ex1_4_basic(cls):
        '''Test that command exists in .sh file'''
        cls.unix_command_check(4)

    def test_ex1_5_basic(cls):
        '''Test that command exists in .sh file'''
        cls.unix_command_check(5)


class TestPythonPart:

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class."""

        global exam
        import exam

    def test_exam_test_import(cls):
        '''Test that exam_test works'''
        import exam_test

    def test_python_ex_2_1_basic(cls):
        '''Test for existence and callability of read_data_1'''

        # Check that the function exists
        assert hasattr(exam, "read_data_1"), "Function not found"

        # Check that the function can be called
        exam.read_data_1("owid-covid-data.csv")

    def test_python_ex_2_2_basic(cls):
        '''Test for existence and callability of read_data_2'''

        # Check that the function exists
        assert hasattr(exam, "read_data_2"), "Function not found"

        # Check that the function can be called
        exam.read_data_2("owid-covid-data.csv")

    def test_python_ex_2_3_basic(cls):
        '''Test for existence and callability of read_data_3'''

        # Check that the function exists
        assert hasattr(exam, "read_data_3"), "Function not found"

        # Check that the function can be called
        exam.read_data_3("owid-covid-data.csv")

    def test_python_ex_3_1_basic(cls):
        '''Test for existence and callability of get_weekly_per_100k_for_country_date'''

        # Check that the function exists
        assert hasattr(exam, "get_weekly_per_100k_for_country_date"), "Function not found"

        # Check that the function can be called
        exam.get_weekly_per_100k_for_country_date({"Czech Republic": {'2020-10-19':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-19', 'total_cases': '173885.0', 'new_cases': '5058.0', 'new_cases_smoothed': '8110.714', 'total_deaths': '1422.0', 'new_deaths': '70.0', 'new_deaths_smoothed': '55.429', 'total_cases_per_million': '16237.304', 'new_cases_per_million': '472.314', 'new_cases_smoothed_per_million': '757.375', 'total_deaths_per_million': '132.786', 'new_deaths_per_million': '6.537', 'new_deaths_smoothed_per_million': '5.176', 'total_tests': '1845161.0', 'new_tests': '31051.0', 'total_tests_per_thousand': '172.3', 'new_tests_per_thousand': '2.9', 'new_tests_smoothed': '31046.0', 'new_tests_smoothed_per_thousand': '2.899', 'tests_per_case': '3.8280000000000003', 'positive_rate': '0.261', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}, '2020-10-20':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-20', 'total_cases': '181962.0', 'new_cases': '8077.0', 'new_cases_smoothed': '8648.714', 'total_deaths': '1513.0', 'new_deaths': '91.0', 'new_deaths_smoothed': '66.0', 'total_cases_per_million': '16991.531', 'new_cases_per_million': '754.227', 'new_cases_smoothed_per_million': '807.613', 'total_deaths_per_million': '141.283', 'new_deaths_per_million': '8.498', 'new_deaths_smoothed_per_million': '6.163', 'total_tests': '1885488.0', 'new_tests': '40327.0', 'total_tests_per_thousand': '176.066', 'new_tests_per_thousand': '3.766', 'new_tests_smoothed': '32298.0', 'new_tests_smoothed_per_thousand': '3.016', 'tests_per_case': '3.734', 'positive_rate': '0.268', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}}}, "Czech Republic", '2020-10-20')

    def test_python_ex_3_2_basic(cls):
        '''Test for existence and callability of get_weekly_per_100k_for_country'''

        # Check that the function exists
        assert hasattr(exam, "get_weekly_per_100k_for_country"), "Function not found"

        # Check that the function can be called
        exam.get_weekly_per_100k_for_country({"Czech Republic": {'2020-10-19':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-19', 'total_cases': '173885.0', 'new_cases': '5058.0', 'new_cases_smoothed': '8110.714', 'total_deaths': '1422.0', 'new_deaths': '70.0', 'new_deaths_smoothed': '55.429', 'total_cases_per_million': '16237.304', 'new_cases_per_million': '472.314', 'new_cases_smoothed_per_million': '757.375', 'total_deaths_per_million': '132.786', 'new_deaths_per_million': '6.537', 'new_deaths_smoothed_per_million': '5.176', 'total_tests': '1845161.0', 'new_tests': '31051.0', 'total_tests_per_thousand': '172.3', 'new_tests_per_thousand': '2.9', 'new_tests_smoothed': '31046.0', 'new_tests_smoothed_per_thousand': '2.899', 'tests_per_case': '3.8280000000000003', 'positive_rate': '0.261', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}, '2020-10-20':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-20', 'total_cases': '181962.0', 'new_cases': '8077.0', 'new_cases_smoothed': '8648.714', 'total_deaths': '1513.0', 'new_deaths': '91.0', 'new_deaths_smoothed': '66.0', 'total_cases_per_million': '16991.531', 'new_cases_per_million': '754.227', 'new_cases_smoothed_per_million': '807.613', 'total_deaths_per_million': '141.283', 'new_deaths_per_million': '8.498', 'new_deaths_smoothed_per_million': '6.163', 'total_tests': '1885488.0', 'new_tests': '40327.0', 'total_tests_per_thousand': '176.066', 'new_tests_per_thousand': '3.766', 'new_tests_smoothed': '32298.0', 'new_tests_smoothed_per_thousand': '3.016', 'tests_per_case': '3.734', 'positive_rate': '0.268', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}}}, "Czech Republic")

    def test_python_ex_3_3_basic(cls):
        '''Test for existence and callability of plot_weekly_per_100k_for_country'''

        # Check that the function exists
        assert hasattr(exam, "plot_weekly_per_100k_for_country"), "Function not found"

        # Check that the function can be called
        exam.plot_weekly_per_100k_for_country({"Czech Republic": {'2020-10-19':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-19', 'total_cases': '173885.0', 'new_cases': '5058.0', 'new_cases_smoothed': '8110.714', 'total_deaths': '1422.0', 'new_deaths': '70.0', 'new_deaths_smoothed': '55.429', 'total_cases_per_million': '16237.304', 'new_cases_per_million': '472.314', 'new_cases_smoothed_per_million': '757.375', 'total_deaths_per_million': '132.786', 'new_deaths_per_million': '6.537', 'new_deaths_smoothed_per_million': '5.176', 'total_tests': '1845161.0', 'new_tests': '31051.0', 'total_tests_per_thousand': '172.3', 'new_tests_per_thousand': '2.9', 'new_tests_smoothed': '31046.0', 'new_tests_smoothed_per_thousand': '2.899', 'tests_per_case': '3.8280000000000003', 'positive_rate': '0.261', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}, '2020-10-20':{'iso_code': 'CZE', 'continent': 'Europe', 'location': 'Czech Republic', 'date': '2020-10-20', 'total_cases': '181962.0', 'new_cases': '8077.0', 'new_cases_smoothed': '8648.714', 'total_deaths': '1513.0', 'new_deaths': '91.0', 'new_deaths_smoothed': '66.0', 'total_cases_per_million': '16991.531', 'new_cases_per_million': '754.227', 'new_cases_smoothed_per_million': '807.613', 'total_deaths_per_million': '141.283', 'new_deaths_per_million': '8.498', 'new_deaths_smoothed_per_million': '6.163', 'total_tests': '1885488.0', 'new_tests': '40327.0', 'total_tests_per_thousand': '176.066', 'new_tests_per_thousand': '3.766', 'new_tests_smoothed': '32298.0', 'new_tests_smoothed_per_thousand': '3.016', 'tests_per_case': '3.734', 'positive_rate': '0.268', 'tests_units': 'tests performed', 'stringency_index': '48.15', 'population': '10708982.0', 'population_density': '137.176', 'median_age': '43.3', 'aged_65_older': '19.027', 'aged_70_older': '11.58', 'gdp_per_capita': '32605.906', 'extreme_poverty': '', 'cardiovasc_death_rate': '227.485', 'diabetes_prevalence': '6.82', 'female_smokers': '30.5', 'male_smokers': '38.3', 'handwashing_facilities': '', 'hospital_beds_per_thousand': '6.63', 'life_expectancy': '79.38', 'human_development_index': '0.888'}}}, "Czech Republic")

    def test_python_ex_4_1_basic(cls):
        '''Test for existence and callability of read_into_dataframe'''

        # Check that the function exists
        assert hasattr(exam, "read_into_dataframe"), "Function not found"

        # Check that the function can be called
        exam.read_into_dataframe("owid-covid-data.csv")

        # exam.read_into_dataframe('owid-covid-data.csv',
        #                          ['Austria', 'Belarus', 'Belgium',
        #                           'Bulgaria', 'Czech Republic', 'Denmark',
        #                           'Finland', 'France', 'Germany', 'Greece',
        #                           'Hungary', 'Italy', 'Netherlands', 'Norway',
        #                           'Poland', 'Portugal', 'Romania', 'Russia',
        #                           'Serbia', 'Slovakia', 'Spain', 'Sweden',
        #                           'Switzerland', 'Ukraine', 'United Kingdom',
        #                           'United States'])

    def test_python_ex_4_2_basic(cls):
        '''Test for existence and callability of get_weekly_per_100k'''

        # Check that the function exists
        assert hasattr(exam, "get_weekly_per_100k"), "Function not found"

        # Check that the function can be called
        exam.get_weekly_per_100k(exam.read_into_dataframe("owid-covid-data.csv"))

    def test_python_ex_4_3_basic(cls):
        '''Test for existence and callability of get_weekly_per_100k_country_vs_date'''

        # Check that the function exists
        assert hasattr(exam, "get_weekly_per_100k_country_vs_date"), "Function not found"

        # Check that the function can be called
        exam.get_weekly_per_100k_country_vs_date(exam.get_weekly_per_100k(exam.read_into_dataframe("owid-covid-data.csv")))


