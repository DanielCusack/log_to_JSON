# log_to_JSON
Convert a log to a JSON file. This program can take two arguments which are the log path and the path of the directory where the JSON will be stored.

This program can be used with the command `python3 log_parser.py $log_path $output_path`.

I was not able to finish this task. I have gotten to a point where I can generate a dictionary with:

key: month/date

value: dictionary with:

-----key: language

-----value: list containing file size for each file of that language and month/year.

I would need to generate the appropriate statistics from these lists (total size, mean and standard deviation), convert the dictionary to a JSON using the json module and save it to the output_path.
