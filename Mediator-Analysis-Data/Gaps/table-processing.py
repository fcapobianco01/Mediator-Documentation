import re

table_base_row = 10


def find_keyword_count(line, implicit=True):
    exist = 0
    if implicit:
        exist = len(re.findall("large_blue_diamond|red_circle", line))
    else:
        exist = len(re.findall("red_circle", line))

    if exist > 0:
        return int(re.search(r'\d+', line).group())
    return 0


def find_keyword_count_implicit(line):
    if len(re.findall("large_blue_diamond", line)) > 0:
        return int(re.search(r'\d+', line).group())
    return 0


def update_table_helper(table, annotation, pattern, implicit, offset):
    """Helper function for update_table. Updates the table with the annotation
    and the offset
    """
    if pattern:
        file1 = "Purpose-Final.md"
        file2 = "Other-Final.md"
    elif annotation:
        file1 = "Purpose-Relaxed.md"
        file2 = "Other-Relaxed.md"
    else:
        if implicit:
            file1 = "Purpose-Strict.md"
            file2 = "Other-Strict.md"
        else:
            file1 = "Purpose-Field.md"
            file2 = "Other-Field.md"

    field = [0, 0, 0]
    with open(file1, "r") as f:
        for i, line in enumerate(f):
            if i in range(7, 31):  # tomoyo
                field[1] += find_keyword_count(line, implicit=implicit)
            if i in range(32, 53):  # apparmor
                field[2] += find_keyword_count(line, implicit=implicit)
            if i in range(54, 157):  # selinux
                field[0] += find_keyword_count(line, implicit=implicit)
        table[table_base_row + offset][0] = str(field[0])
        table[table_base_row + offset + 5][0] = str(field[1])
        table[table_base_row + offset + 10][0] = str(field[2])
        f.close()

    field = [[0, 0, 0], [0, 0, 0]]
    with open(file2, "r") as f:
        for i, line in enumerate(f):
            if i in range(7, 31):  # tomoyo
                l = line.split("|")
                field[0][1] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][1] += find_keyword_count(l[j], implicit=implicit)
            if i in range(32, 53):  # apparmor
                l = line.split("|")
                field[0][2] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][2] += find_keyword_count(l[j], implicit=implicit)
            if i in range(54, 157):  # selinux
                l = line.split("|")
                field[0][0] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][0] += find_keyword_count(l[j], implicit=implicit)
        table[table_base_row + offset][1] = str(field[0][0])
        table[table_base_row + offset + 5][1] = str(field[0][1])
        table[table_base_row + offset + 10][1] = str(field[0][2])
        table[table_base_row + offset][2] = str(field[1][0])
        table[table_base_row + offset + 5][2] = str(field[1][1])
        table[table_base_row + offset + 10][2] = str(field[1][2])
        f.close()


def update_table():
    table = []
    with open("benchmark-comparison.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(10, 25):
                l = line.split("&")
                table.append([
                    s.replace("\\", "").replace("cline{2-5}",
                                                "").replace("hline",
                                                            "").strip()
                    for s in l[2:5]
                ])
            else:
                table.append(line)
        f.close()

    update_table_helper(table,
                        annotation=False,
                        pattern=False,
                        implicit=False,
                        offset=1)
    update_table_helper(table,
                        annotation=False,
                        pattern=False,
                        implicit=True,
                        offset=2)
    update_table_helper(table,
                        annotation=True,
                        pattern=False,
                        implicit=True,
                        offset=3)
    update_table_helper(table,
                        annotation=True,
                        pattern=True,
                        implicit=True,
                        offset=4)

    with open("benchmark-comparison.tex", "w") as f:
        for row in table[0:10]:
            f.write(row)
        for i, row in enumerate(table[table_base_row:table_base_row + 15]):
            line = ''
            if i % 5 == 0:
                line += '    \multirow{5}{*}{'
                if i / 5 == 0:
                    line += 'SELinux}      & Baseline'.ljust(54)
                elif i / 5 == 1:
                    line += 'Tomoyo}       & Baseline'.ljust(54)
                elif i / 5 == 2:
                    line += 'AppArmor}     & Baseline'.ljust(54)
            elif i % 5 == 1:
                line += ' ' * 34 + '& Field-sensitive                       '
            elif i % 5 == 2:
                line += ' ' * 34 + '& Strict NI + Constants                 '
            elif i % 5 == 3:
                line += ' ' * 34 + '& Relaxed NI + Constants                '
            elif i % 5 == 4:
                line += ' ' * 34 + '& Relaxed NI + Constants + Patterns     '
            line += '& ' + \
                row[0].rjust(5) + ' & ' + row[1].rjust(5) + \
                ' & ' + row[2].rjust(5) + ' \\\\'
            if i % 5 == 1:
                line += ' \cline{2-5}'
            elif i % 5 == 4:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[table_base_row + 15:]:
            f.write(row)
        f.close()


def update_table1():
    table = []
    with open("benchmark-column.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(20, 23):
                l = line.split("&")
                table.append([
                    s.replace("\\", "").replace("cline{2-5}",
                                                "").replace("hline",
                                                            "").strip()
                    for s in l
                ])
            else:
                table.append(line)
        f.close()
    for l in table:
        print(l)

    field = [0, 0, 0]
    file1 = "Purpose-Final.md"
    file2 = "Other-Final.md"

    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=True)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=True)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=True)
            table[20][4 + idx] = str(field[0])
            table[21][4 + idx] = str(field[1])
            table[22][4 + idx] = str(field[2])
            print(field)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=True)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=True)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=True)
            table[20][10 + idx] = str(field[0])
            table[21][10 + idx] = str(field[1])
            table[22][10 + idx] = str(field[2])
            print(field)
    f.close()

    with open("benchmark-column.tex", "w") as f:
        for row in table[0:20]:
            f.write(row)
        for i, row in enumerate(table[20:23]):
            row[0] = row[0].ljust(10)
            for j, e in enumerate(row[1:]):
                row[j + 1] = e.rjust(3)
            line = ' & '.join(row)
            line += ' \\\\'
            if i == 2:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[23:]:
            f.write(row)
        f.close()


def update_table4():
    table = []
    with open("benchmark-implicit.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(19, 22):
                l = re.split('&|/', line)
                table.append([
                    s.replace("\\", "").replace("hline", "").strip() for s in l
                ])
            else:
                table.append(line)
        f.close()
    for l in table[19:22]:
        print(l)

    field = [0, 0, 0]
    file1 = "Purpose-Strict.md"
    file2 = "Other-Strict.md"
    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][3 + idx * 3] = str(field[0])
            table[20][3 + idx * 3] = str(field[1])
            table[21][3 + idx * 3] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][21 + idx * 3] = str(field[0])
            table[20][21 + idx * 3] = str(field[1])
            table[21][21 + idx * 3] = str(field[2])
    f.close()

    file1 = "Purpose-Relaxed.md"
    file2 = "Other-Relaxed.md"
    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][4 + idx * 3] = str(field[0])
            table[20][4 + idx * 3] = str(field[1])
            table[21][4 + idx * 3] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][22 + idx * 3] = str(field[0])
            table[20][22 + idx * 3] = str(field[1])
            table[21][22 + idx * 3] = str(field[2])
    f.close()

    file1 = "Purpose-Final.md"
    file2 = "Other-Final.md"
    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][5 + idx * 3] = str(field[0])
            table[20][5 + idx * 3] = str(field[1])
            table[21][5 + idx * 3] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count_implicit(l[2 + idx])
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count_implicit(l[2 + idx])
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count_implicit(l[2 + idx])
            table[19][23 + idx * 3] = str(field[0])
            table[20][23 + idx * 3] = str(field[1])
            table[21][23 + idx * 3] = str(field[2])
    f.close()

    with open("benchmark-implicit.tex", "w") as f:
        for row in table[0:19]:
            f.write(row)
        for i, row in enumerate(table[19:22]):
            new_row = []
            new_row.append(row[0].ljust(10))
            new_row.append(row[1].ljust(3))
            new_row.append(row[2].ljust(3))
            for j in range(3, 32, 3):
                new_row.append(
                    (row[j] + '/' + row[j + 1] + '/' + row[j + 2]).rjust(8))
            line = ' & '.join(new_row)
            line += ' \\\\'
            if i == 2:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[22:]:
            f.write(row)
        f.close()
    for l in table[19:22]:
        print(l)


def update_table7():
    table = []
    with open("benchmark-comparison1.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(19, 22):
                l = re.split('&|/', line)
                table.append([
                    s.replace("\\", "").replace("hline", "").strip() for s in l
                ])
            else:
                table.append(line)
        f.close()
    for l in table[19:22]:
        print(l)

    field = [0, 0, 0]
    file1 = "Purpose-Baseline.md"
    file2 = "Other-Baseline.md"
    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=False)
            table[19][3 + idx * 2] = str(field[0])
            table[20][3 + idx * 2] = str(field[1])
            table[21][3 + idx * 2] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=False)
            table[19][15 + idx * 2] = str(field[0])
            table[20][15 + idx * 2] = str(field[1])
            table[21][15 + idx * 2] = str(field[2])
    f.close()

    file1 = "Purpose-Field.md"
    file2 = "Other-Field.md"
    for idx in range(0, 6):
        with open(file1, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=False)
            table[19][4 + idx * 2] = str(field[0])
            table[20][4 + idx * 2] = str(field[1])
            table[21][4 + idx * 2] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    for idx in range(0, 4):
        with open(file2, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                if i in range(7, 31):  # tomoyo
                    l = line.split("|")
                    field[1] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(32, 53):  # apparmor
                    l = line.split("|")
                    field[2] += find_keyword_count(l[2 + idx], implicit=False)
                if i in range(54, 157):  # selinux
                    l = line.split("|")
                    field[0] += find_keyword_count(l[2 + idx], implicit=False)
            table[19][16 + idx * 2] = str(field[0])
            table[20][16 + idx * 2] = str(field[1])
            table[21][16 + idx * 2] = str(field[2])
    f.close()

    with open("benchmark-comparison1.tex", "w") as f:
        for row in table[0:19]:
            f.write(row)
        for i, row in enumerate(table[19:22]):
            new_row = []
            new_row.append(row[0].ljust(10))
            new_row.append(row[1].ljust(3))
            new_row.append(row[2].ljust(3))
            for j in range(3, 22, 2):
                new_row.append((row[j] + '/' + row[j + 1]).rjust(7))
            line = ' & '.join(new_row)
            line += ' \\\\'
            if i == 2:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[22:]:
            f.write(row)
        f.close()
    for l in table[19:22]:
        print(l)


def main():
    """Looks at results from Vulnerable/Taint Analysis and records the associated
    line with it
    """
    update_table1()
    update_table4()
    update_table7()


if __name__ == "__main__":
    main()
