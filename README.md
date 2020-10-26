# Python Programming for Data Science, Exam, 2020

## Background

We are in the middle of a Corona pandemic. In this exam, we will study
the infection numbers across the globe. We will be working on a dataset
provided by Our World in Data:

<dl>
<dt>Description of the dataset (README)</dt>
<dd>https://github.com/owid/covid-19-data/tree/master/public/data</dd>
<dt>Data file in CSV format</dt>
<dd>To make sure we all work on the same data, please download this particular
version of the data (from Oct 22):

<a href="https://github.com/owid/covid-19-data/raw/69de52175d96f7badcc7ec58ca910d091ca0fd0e/public/data/owid-covid-data.csv">https://github.com/owid/covid-19-data/raw/69de52175d96f7badcc7ec58ca910d091ca0fd0e/public/data/owid-covid-data.csv</a></dd>

Please place this file in the main directory of your repository.
</dl>

Start by looking at the README and the csv file to get an overview of
the data. Below, we will explore these data files in various Unix and
Python exercises. Before we begin, however, please read carefully
through the following practical details of the exam.

<table style="width:100%"><tr><td>
<div style="margin-top:1em; margin-bottom:2em; width:100%; border:1px solid grey; padding: 0em 1em 1em 1em; box-sizing:border-box">
  <h3 style="padding-top:0;text-align:center"><strong>Formal requirements:</strong></h3>

  <dl>
    <dt>How do I hand-in?</dt>
    <dd>We will be using a combination of the Digital Exam system (https://eksamen.ku.dk) and Github to submit the exams. Submission of the exam consists of two steps: 1) Commit&push your code to github just as we have done in the weekly hand-ins. 2) Within the digital exam system itself, submit a text-file called <code>github_link.txt</code>, which contains just a single line with only the link to your exam github repository (i.e. <code>https://github.com/UCPH-PPDS2020/exam-YOUR-USER-NAME</code>). <strong>It is important that you do both these steps!</strong> Note that you can actually complete the second step whenever you want during the exam week - even if you haven't finished your exam yet. We will simply extract the latest version from your github repository that was pushed before the deadline. </dd>
    <dt>Format:</dt>
    <dd>You should modify the following files in your github repository:
      <ol>
        <li>A Python file called <code>exam.py</code>, containing the function and class definitions.</li>
        <li>A Python file called <code>exam_test.py</code>, containing test code for the individual questions.</li>
        <li>A plain text file called <code >exam.sh</code>, containing the Unix commands used. The commands should be separated by empty lines, just like in the handins. The commands should be written so that they can be executed from the top-level directory (i.e. the directory in which <code>exam.sh</code> is located).</li>
      </ol>
    </dd>
    <dt>Content:</dt>
    <dd>For the Python part, remember to use
      meaningful variable names, include docstrings for each
      function, and add comments when code is not self-explanatory. Also, limit yourself to the curriculum covered in
      the course, that is, <span style="font-weight:bold">do not use
  list and dict comprehension, map, zip, reduce, filter and
  lambda</span>. Also, <strong>please use external modules only when they
  are explicitly mentioned in the exercise</strong>. Failure to do
      any of these will force us to deduct points even for code that works.</dd>
    <dt>Can we work in groups?</dt>
    <dd><strong>No!</strong> You should do the exam <strong>by yourself</strong>, and <strong>not discuss or share your solutions with anyone</strong>.</span> We will systematically use plagiarism programs to catch similarities between the exam solutions, and if we detect any suspicious overlap we will be forced to report it to the University Study Administration, who will then act accordingly. Students have been expelled on the basis of plagiarism on this course
      previously, so please take this seriously. You are of course welcome to seek information online, but please try to avoid copying large blocks of code verbatim from online examples. If you for some reason find it necessary to copy code directly (without rewriting it), then please add a comment that specifies the source of this code.</dd>
  </dl>
</div>
</td></tr></table>
</td></tr></table>

## Part 1: Data exploration in Unix (25%)

We'll start with inspecting the data using Unix commands. 

<ol>
<li>The first column in the dataset contains country codes, following the ISO 3166-1 alpha-3 standard (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3). However, some lines do not fulfill this format. Write a Unix command that selects only the lines that have a legal ISO 3166-1 alpha-3 in the first field and saves these lines to a new file called <code>owid-covid-data-filtered.csv</code>. You should use a regular expression for this. The filtered file should not contain the header line. Note that for the remaining Unix commands, you should use this filtered version of the dataset.</li>
<li>Write a command that counts how many <em>different</em> ISO 3166-1 alpha-3 codes there are in the <code>owid-covid-data-filtered.csv</code> dataset. It should output a single line containing only a number.</li>
<li>Write a command that outputs for which months we have data (for any country) in the <code>owid-covid-data-filtered.csv</code> dataset. The output should contain a number of lines in YYYY-MM format, sorted chronologically (earliest first).</li>
<li>Write a command that outputs, for the <code>owid-covid-data-filtered.csv</code> file, the 10 country names (not the country codes) for which the <em>total number of deaths</em> was highest on Oct 10, 2020, sorted with highest first.</li>
<li>Write a command that outputs, for the <code>owid-covid-data-filtered.csv</code> file, the 10 country names (not the country codes) for which the <em>total number of deaths per million</em> was highest on Oct 10, 2020, sorted with highest first. Notice how the ordering changes.</li>
</ol>


## Part 2: Data preprocessing in Python (25%)

The next step is to process the data in Python. Please note that for the remainder of the exam, we will be using the raw <code>owid-covid-data.csv</code> file, not the filtered version.

<ol>
<li>Write a function called <code>read_data_1</code> that takes a filename (string) as argument. The function should read the file and return a dictionary, where the keys are country names ( strings, from the <code>location</code> field) and each value is a list of (date, new_cases) tuples. Both these values in each tuple should be strings.

Inside the <code>exam_test.py</code> file, import the <code>exam</code> module, and test your <code>read_data_1</code> function by calling it on the <code>owid-covid-data.csv</code> file. Save the result in a variable called <code>covid_dict_1</code>.
</li>
<li>We're now going to do the same preprocessing step as we did in the Unix part. Make a copy of your <code>read_data_1</code> function, call it <code>read_data_2</code>. This function should be identical to <code>read_data_1</code>, but now only include countries which have a valid ISO 3166-1 alpha-3 country code. You should use a regular expression for this (applied on the raw input lines).

Inside the <code>exam_test.py</code> file, test your <code>read_data_2</code> function by calling it on the <code>owid-covid-data.csv</code> file. Save the result in a variable called <code>covid_dict_2</code>.
</li>
<li>Rather than just reading in the <code>new_cases</code> field, we'll now read in all the columns. Make a copy of your <code>read_data_2</code> function, call it <code>read_data_3</code>. This function should be identical to <code>read_data_2</code>, but now the inner-tuples should be replaced by a dictionary of dictionaries, such that you can index into the dictionary using: <code>['Denmark']['2020-10-10']['new_cases']</code> to access the new cases for Denmark on a particular date. Note that you should use the field names from the first line of the .csv file as the keys for this inner dictionary. To keep things simple, the inner dictionary should contain <em>all</em> fields (including the location and date fields, even though they are already present as keys in the outer directory)

Inside the <code>exam_test.py</code> file, test your <code>read_data_3</code> function by calling it on the <code>owid-covid-data.csv</code> file. Save the result in a variable called <code>covid_dict_3</code>. Verify that the <code>covid_dict_3['Denmark']['2020-10-10']['new_cases']</code> lookup works.

<table style="width:100%"><tr><td>

If you have problems completing this exercise, and therefore do not
have the <code>covid_dict_3</code> dictionary, please
follow the following instructions in order to be able to complete
the remainder of the exercises:

<ol>
<li>Download the following file to your current directory: https://wouterboomsma.github.io/ppds2020/data/owid-covid-data.json.gz.</li>

<li>Insert the following lines of code in your <code>exam_test.py</code> file:

```python
import json
import gzip
with gzip.open("owid-covid-data.json.gz", "rb") as f:
    covid_dict_3 = dict(json.loads(f.read().decode("ascii")))
```
</li>

Note that this dictionary is not exactly identical to the one you get from solving the exercise yourself (so you cannot use it for verification purposes).

</td></tr></table>
</li>
</ol>


## Part 3: Analyses 1 (25%)

The Danish authorities have placed restrictions on which countries Danes can travel to based on the number of new infection cases in the destination country. One of the main criteria is that a country should have less than 20 new weekly cases per 100,000 inhabitants. Let's take a look at this number.

<ol>
<li>Write a function called <code>get_weekly_per_100k_for_country_date</code>. The function should take three arguments: a dictionary with covid data (like the one from exercise 2.3), a country-name (string) and a date (a string in the format YYYY-MM-DD), and return a floating point number. As a rough estimate for the number of cases per week, you should use the <code>new_cases_smoothed_per_million</code> field and multiple it by seven (but remember to rescale it to 100,000 inhabitants instead of a million). The function should raise an exception when called on dates and countries for which no data is available.

Inside the <code>exam_test.py</code> file, test your <code>get_weekly_per_100k_for_country_date</code> function by calling it like this:

<pre><code>print(exam.get_weekly_per_100k_for_country_date(covid_dict_3, "Czech Republic", '2020-10-20'))</code></pre></li>

<li>Let's now take a look at the development of this number over time. Write a function called <code>get_weekly_per_100k_for_country</code> that takes two arguments: a dictionary with covid data (like the one from exercise 2.3) and a country name (string). The function should return two lists: 1) a list of dates, and 2) a list of weekly-per-100k values as discussed in 3.1 (as floats). The latter values should be obtained by calling your own <code>get_weekly_per_100k_for_country_date</code> from the previous exercise. The dates should be in Python <code>datetime</code> format, which makes it possible to easily plot them. To convert from date-strings to <code>datetime</code> objects, you should use the <code>strptime()</code> method. For more information, see https://docs.python.org/3/library/datetime.html. 

Inside the <code>exam_test.py</code> file, test your <code>get_weekly_per_100k_for_country</code> function by calling it like this:

<pre><code>dates, values = exam.get_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")</code></pre></li>

<li>Now, let's plot the data. Write a function called <code>plot_weekly_per_100k_for_country</code>. The function should take take two arguments: a dictionary with covid data (like the one from exercise 2.3) and a country name (string). The function should call the <code>get_weekly_per_100k_for_country</code> function to get the relevant data, and then create a line plot using <code>matplotlib</code>. In addition to the main plot, add the following features to your plot:

<ol><ol>
<li>Use the <code>MonthLocator</code> in <code>matplotlib.dates</code> to limit your x-axis to only have one tick mark per month (depending on your installation, it might already do this by default)</li>
<li>Use the <code>autofmt_xdate()</code> function in <code>matplotlib</code> to improve the layout of your x-axis labels.
<li>Add a constant dotted line at y=20 to show the threshold for being considered an open country.</li>
<li>Add a title to the plot "Weekly cases per 100k for COUNTRY-NAME", where COUNTRY-NAME is the argument that the function was called with.</li>
<li>Add titles to the x- and y-axes: "time", and "new weekly cases (per 100k)".</li>
</ol></ol>

Inside the <code>exam_test.py</code> file, test your <code>plot_weekly_per_100k_for_country</code> function by calling it like this:

<pre><code>import matplotlib.pyplot as plt
exam.plot_weekly_per_100k_for_country(covid_dict_3, "Czech Republic")
plt.savefig('weekly_cases_cze.png')</code></pre></li>

</ol>

## Part 4: Analyses 2 - pandas (25%)

We'll now do a similar analyses using Pandas. Pandas makes it easier to do the analyses properly (e.g. calculating sums per week), and also makes it possible to easily align the date entries across all countries.

<ol>
<li>Write a function called <code>read_into_dataframe</code> that reads the .csv file into a pandas dataframe. The function takes two arguments: 1) the name of the .csv file (as a string), and 2) an optional argument called <code>countries</code>(defaulting to <code>None</code>) that allows the user to select only a subset of countries. The function should:

<ol><ol>
    <li>Read the data into a dataframe.</li>
    <li>Modify the dataframe so that it ignores the lines for which the <code>iso_code</code> country code string does not consist of three characters.</li>
    <li>Convert the <code>date</code> column to be of type <code>datetime64</code>.</li>
    <li>if the countries argument is provided, the function should filter the dataframe such that only lines for the specified countries are included in the dataframe (hint: dataframes have an <code>isin</code> method that helps doing this).</li>
</ol></ol>

Inside the <code>exam_test.py</code> file, test your <code>read_into_dataframe</code> function by calling it both with and without selecting countries, like this:

<pre><code>df = exam.read_into_dataframe('owid-covid-data.csv')
df_selected_countries = exam.read_into_dataframe('owid-covid-data.csv',
                                                 ['Austria', 'Belarus', 'Belgium',
						  'Bulgaria', 'Czech Republic', 'Denmark',
						  'Finland', 'France', 'Germany', 'Greece',
						  'Hungary', 'Italy', 'Netherlands', 'Norway',
						  'Poland', 'Portugal', 'Romania', 'Russia',
						  'Serbia', 'Slovakia', 'Spain', 'Sweden',
						  'Switzerland', 'Ukraine', 'United Kingdom',
						  'United States'])
</code></pre></li>

<li>We will now calculate the weekly sums ourselves. Write a function called <code>get_weekly_per_100k</code> that takes a dataframe as input (like the one from the previous exercise), and returns a new dataframe which only contains entries for one day per week (Sundays). These values should be the sum over the entire week.

Hints: if a dataframe has a datetime index, you can use the <code>resample</code> method to up- or down-sample the frequency of observations in a dataframe. Here is an example where we sum the entries for a week:

<pre><code>import pandas as pd
import numpy as np
idx = pd.date_range('2020/10/12',
                    periods=14, freq='D')
df = pd.DataFrame(np.ones(len(idx)),
                  index=idx)
print(df.resample('W').sum())</code></pre>

For our data, it is a little more complicated than this, because we only want to sum entries for the same country. Note, however, that pandas also allows you to call <code>resample</code> on the result of a <code>groupby</code> operation. Follow the following steps to solve this exercise:

<ol><ol>
<li>Change the index of the dataframe to be the <code>date</code> column.</li>
<li>Use a combination of <code>groupby</code> and <code>resample('W')</code> to reduce the dataframe to only weekly entries, consisting of the average for that week, multiplied by 7 (this corresponds to the sum, but also works for incomplete weeks).</li>
<li>Reset the index on the resulting data frame to get back the <code>date</code> and <code>location</code> columns.
<li>Finally, return a dataframe that only consists of three columns: <code>location</code>, <code>date</code> and <code>weekly_new_cases_per_100k</code>, where the latter is based on the averaged <code>new_cases_per_million</code> column, but scaled to be per 100,000 instead of per million.</li>
</ol></ol>

Inside the <code>exam_test.py</code> file, test your <code>get_weekly_per_100k</code> function by calling it like this:

<pre><code>weekly_per_100k = exam.get_weekly_per_100k(df_selected_countries)</code></pre></li>

<li>We will now reformat our dataframe so that each <em>row</em> corresponds to a country, and the <em>columns</em> correspond to different date values. The values in the dataframe should be the <code>weekly_new_cases_per_100k</code> values that we calculated above. So for any (existing) combination of country and date, we should be able to look up in the dataframe using <code>.loc[country, date]</code>. This way of reorganizing a table is called pivoting a table, and this operation is built into pandas. Your task is to find out how to use this functionality. Write a function called <code>get_weekly_per_100k_country_vs_date</code> that takes a single value as argument: a dataframe like the one from the previous exercise. The function should return the pivoted table.

Inside the <code>exam_test.py</code> file, test your <code>get_weekly_per_100k_country_vs_date</code> function by calling it like this:

<pre><code>country_vs_date = exam.get_weekly_per_100k_country_vs_date(weekly_per_100k)

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
plt.savefig('weekly_new_cases_per_100k.png')</code></pre></li>


</ol>

## Final remarks

One last comment regarding help: while we can of course not help you
with solving the exam exercise itself, we are available for questions
regarding technical issues and in cases where you are in doubt about
how a question should be interpreted. In particular, if you experience
problems with your python installation that prevent you from solving the
exam, please contact us immediately so we can find a solution as
quickly as possible. Unlike the hand-ins throughout the course, you
will (of course) <strong>not</strong> be able to get detailed feedback on your solution
by submitting it to the automated correction server. However, we have
set up the system to allow you to test whether the basic structure of
your files is correct. It works exactly like the weekly handins: you
can either run <code>pytest</code> locally or use git commit and git push (and
receive an email). Please note that even if
tests pass, it says nothing about the correctness of your assignment,
so you cannot use it to validate your solution, but if a test fails,
it means that this particular exercise does not run, and will
therefore not be assessed for the exam. Using this service is entirely
optional, but we highly recommend using it to rule out any technical
issues.  If you experience code that works on your own machine but
fails on the server, feel free to contact us about this, as this will
fall under the category "technical issues" which we are allowed to
help with. <strong>It is extremely important to
note that the github submission by itself it not sufficient. YOU HAVE
TO SUBMIT A LINK TO DIGITAL EXAM AS WELL!</strong> Also note that pushing to github
once in a while is a good way to keep backups of your exam during
the exam week.





