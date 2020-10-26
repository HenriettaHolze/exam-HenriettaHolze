# 1
# Write a Unix command that selects only the lines that have a legal ISO 3166-1 alpha-3 in the first field and 
# saves these lines to a new file called owid-covid-data-filtered.csv. 
# You should use a regular expression for this. 
# The filtered file should not contain the header line. 
cat owid-covid-data.csv | grep '^[a-zA-Z][a-zA-Z][a-zA-Z],' > owid-covid-data-filtered.csv

# 2
# count how many different ISO 3166-1 alpha-3 codes there are in the owid-covid-data-filtered.csv dataset
cat owid-covid-data-filtered.csv | cut -d',' -f1 | sort | uniq | wc -l
# 210

# 3
# for which months we have data (for any country) in the owid-covid-data-filtered.csv dataset. 
# The output should contain a number of lines in YYYY-MM format, sorted chronologically (earliest first).
# -o, --only-matching: Print only the matched (non-empty) parts of a matching line
# -E, --extended-regexp: Interpret PATTERNS as extended regular expressions
cat owid-covid-data-filtered.csv | grep -o -E '[0-9]+-[0-9]+' | sort | uniq

# 4
# 10 country names (not the country codes) for which the total number of deaths was highest on Oct 10, 2020, sorted with highest first.
# grep lines with relevant date
# sort numeric according to total deaths, this way all empty lines will be on top
# get 1o lines with highest count
# reverse sort 
# cut column with country name
grep '2020-10-10' owid-covid-data-filtered.csv | sort -t',' -k8,8 -n | tail | sort -t',' -k8,8 -nr | cut -d',' -f3

# 5
# 10 country names (not the country codes) for which the total number of deaths per million was highest on Oct 10, 2020, 
# sorted with highest first. Notice how the ordering changes.
# do the same as in 4 but on column 14 
grep '2020-10-10' owid-covid-data-filtered.csv | sort -t',' -k14,14 -n | tail | sort -t',' -k14,14 -nr | cut -d',' -f3