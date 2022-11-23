import re

table_base_row = 10


def find_keyword_count(line, implicit=True):
    if implicit:
        return len(re.findall("large_blue_diamond|red_circle", line))
    else:
        return len(re.findall("red_circle", line))


def update_table_helper(table, annotation, implicit, offset):
    """Helper function for update_table. Updates the table with the annotation
    and the offset
    """
    file1 = "Purpose-Baseline.md"
    file2 = "Other-Baseline.md"

    field = [0, 0, 0]
    with open(file1, "r") as f:
        for i, line in enumerate(f):
            if i in range(7, 31):       # tomoyo
                field[1] += find_keyword_count(line, implicit=implicit)
            if i in range(32, 53):      # apparmor
                field[2] += find_keyword_count(line, implicit=implicit)
            if i in range(54, 157):     # selinux
                field[0] += find_keyword_count(line, implicit=implicit)
        table[table_base_row + offset][0] = str(field[0])
        table[table_base_row + offset + 4][0] = str(field[1])
        table[table_base_row + offset + 8][0] = str(field[2])
        f.close()

    field = [[0, 0, 0], [0, 0, 0]]
    with open(file2, "r") as f:
        for i, line in enumerate(f):
            if i in range(7, 31):       # tomoyo
                l = line.split("|")
                field[0][1] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][1] += find_keyword_count(l[j], implicit=implicit)
            if i in range(32, 53):      # apparmor
                l = line.split("|")
                field[0][2] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][2] += find_keyword_count(l[j], implicit=implicit)
            if i in range(54, 157):     # selinux
                l = line.split("|")
                field[0][0] += find_keyword_count(l[2], implicit=implicit)
                for j in range(3, 6):
                    field[1][0] += find_keyword_count(l[j], implicit=implicit)
        table[table_base_row + offset][1] = str(field[0][0])
        table[table_base_row + offset + 4][1] = str(field[0][1])
        table[table_base_row + offset + 8][1] = str(field[0][2])
        table[table_base_row + offset][2] = str(field[1][0])
        table[table_base_row + offset + 4][2] = str(field[1][1])
        table[table_base_row + offset + 8][2] = str(field[1][2])
        f.close()


def update_table():
    table = []
    with open("benchmark-comparison.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(10, 22):
                l = line.split("&")
                table.append(
                    [
                        s.replace("\\", "")
                        .replace("cline{2-5}", "")
                        .replace("hline", "")
                        .strip()
                        for s in l[2:5]
                    ]
                )
            else:
                table.append(line)
        f.close()

    update_table_helper(table, annotation=False, implicit=True, offset=0)

    with open("benchmark-comparison.tex", "w") as f:
        for row in table[0:10]:
            f.write(row)
        for i, row in enumerate(table[table_base_row: table_base_row + 12]):
            line = ''
            if i % 4 == 0:
                line += '    \multirow{4}{*}{'
                if i / 4 == 0:
                    line += 'SELinux}      & Baseline'.ljust(54)
                elif i / 4 == 1:
                    line += 'Tomoyo}       & Baseline'.ljust(54)
                elif i / 4 == 2:
                    line += 'AppArmor}     & Baseline'.ljust(54)
            elif i % 4 == 1:
                line += ' '*34 + '& Field-sensitive                       '
            elif i % 4 == 2:
                line += ' '*34 + '& Strict Noninterference + Constants    '
            elif i % 4 == 3:
                line += ' '*34 + '& Relaxed Noninterference + Constants   '
            line += '& ' + \
                row[0].rjust(5) + ' & ' + row[1].rjust(5) + \
                ' & ' + row[2].rjust(5) + ' \\\\'
            if i % 4 == 1:
                line += ' \cline{2-5}'
            elif i % 4 == 3:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[table_base_row + 12:]:
            f.write(row)
        f.close()


def main():
    """Looks at results from Vulnerable/Taint Analysis and records the associated
    line with it
    """
    update_table()


if __name__ == "__main__":
    main()
