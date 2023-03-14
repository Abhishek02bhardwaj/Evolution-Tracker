# Evolution-Tracker
This repository is my submission for the task #T331202 where we had to build a build a tool to track the changes in a repository. 
<h2> Project Description</h2>
The support for language in software features such as machine translations has undergone changes over the years. The objective of this project is to create a tool that can monitor and document this evolution over time.
This code is designed to track changes to a CSV file over time using Git. It includes three functions: parse_csv(), run_git_command(), and get_commits(). The parse_csv() function reads in a CSV file, converts it to a dictionary, and returns it. The run_git_command() function runs a given Git command and returns the output. The get_commits() function retrieves a list of all Git commits and for each commit, retrieves the timestamp, CSV data, and appends them to a list of dictionaries. Finally, the export_csv() function writes the accumulated data for each commit into a new CSV file that includes an additional column for the commit timestamp.

The main program calls these functions and exports the data history to a CSV file named 'data_history.csv'. The data is arranged in a flat structure, with each row representing a single commit, and includes the city, temperature, and timestamp for that commit.
<h2>Installation</h2>
<h4>Requirements</h4>
1. Python 3.6 or higher<br>
2. pip<br>
3. git<br>
<h4>Libraries utilised</h4>
1. csv<br>
2. subprocess<br>
3. datetime<br>
<h2>Installation/Usage</h2>
To use the tool, first clone the repository you want to track. Then Clone this repository using git clone. Now copy the tset1.py file in the directory of the repository you wanted to track. Set file_path = Name/of/your/file and execute the file. The output CSV file will be generated in the same directory with the name "data_history.csv".
<h3>Thank You</h3>
