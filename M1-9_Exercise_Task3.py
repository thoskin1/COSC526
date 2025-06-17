import requests

translit_dict = {
    "ä" : "ae",
    "ö" : "oe",
    "ü" : "ue",
    "Ä" : "Ae",
    "Ö" : "Oe",
    "Ü" : "Ue", 
    "ł" : "l",
    "ō" : "o",
}
#3.0
#read data from a URL
def parse_delimited_file(file_url, delimiter):
    response = requests.get(file_url)
    if response.status_code == 200:
        lines = response.text.split('\n')
    else:
        print('Failed to fetch the file from GitHub.')
        return
    lines = [line.rstrip('\n') for line in lines if line.strip()]  # Skip empty lines
    return lines

file_url = "https://raw.githubusercontent.com/cosc-526/home.page/main/data.M.1.exercise.csv"
lines = parse_delimited_file(file_url, delimiter=",")

#3.1
#with open("data.exercise.M.1.csv", 'r', encoding='utf8') as csvfile:
#    lines = csvfile.readlines()
#3.2
# Strip off the newline from the end of each line
lines = [line.rstrip() for line in lines]

#3.3   
# Split each line based on the delimiter (which, in this case, is the comma)
split_lines = [line.split(",") for line in lines]

#3.4
# Separate the header from the data
header = split_lines[0]
data_lines = split_lines[1:]
    
#3.5    
# Find "name" within the header
name_index = header.index("name")

#3.6
# Extract the names from the rows
unicode_names = [line[name_index] for line in data_lines]

#3.7
# Iterate over the names
translit_names = []
for unicode_name in unicode_names:
    # Perform the replacements in the translit_dict
    # HINT: ref [1]
    translit_name = unicode_name
    for key, value in translit_dict.items():
        translit_name = translit_name.replace(key, value)
    translit_names.append(translit_name)

#3.8
# Write out the names to a file named "data-ascii.txt"
# HINT: ref [2]
with open("data.exercise.M.1.ascii.txt", 'w') as outfile:
    for name in translit_names:
        outfile.write(name + "\n")
#3.9
# Verify that the names were converted and written out correctly
with open("data.exercise.M.1.ascii.txt", 'r') as infile:
    for line in infile:
        print(line.rstrip())