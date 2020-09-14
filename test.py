def get_value_from_line(file_name, line_num):
    f = open(file_name, "r")
    i = 0
    for line in f:
        # For Python3, use print(line)
        if i == line_num:
            line = line.split(": ")[1]
            f.close()
            return line
        i = i + 1
