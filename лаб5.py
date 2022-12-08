from statistics import median
import sys, re, os, io, gzip, locale

path_directory = 'C:\000\logy\\'
locale.getdefaultlocale()
locale.getdefaultlocale()
list_file = input("Enter the name of the first file: ")
list_file_open = open(list_file, encoding=locale.getdefaultlocale()[1])
list_file_content = list_file.read()
list_repeat_URl = []
count_list = len(list_file)
max_date = 0


def watch_log(file):
    total_count = 0
    result = {}
    for line in file:
        regex = re.compile(r'\"[A-Z]+ ([^\s]+) .* (\d+\.\d+)\n')
        parsed_line = re.findall(regex, line)
        total_count += 1
        if parsed_line and parsed_line[0]:
            url = parsed_line[0][0]
            time = parsed_line[0][1]
            if url not in result:
                result[url] = []
            result[url].append(float(time))

    for key in result:
        print(
        f'key : {key}; '
        f'count = {len(result[key])}; '
        f'count_perc = {len(result[key]) / total_count}; '
        f'time_avg = {sum(result[key]) / len(result[key])}; '
        f'time_max = {max(result[key])}; '
        f'time_med = {median(result[key])}; '
        )


if count_list == 0:
    print("Логов не найдено")
    sys.exit()

for name in list_file:
    regex = re.compile(r"nginx-access-ui\.log-(\d{8})(\.gz)?")
    value = re.findall(regex, name)
    date = int(value[0][0])
    if max_date < date:
        max_date = date
        file_name = name


if file_name.lower().endswith('.gz'):
    with gzip.open(path_directory + "\\" + file_name, "r") as file:
        with io.TextIOWrapper(file, encoding='utf-8') as file:
            watch_log(file)
else:
    with open(path_directory + "\\" + file_name, 'r') as file:
        watch_log(file)

