import re


def get_count(line, explicit, implicit):
    count = 0
    line = line.strip().replace("-", "0").split("/")
    if len(line) > 1:
        if explicit:
            count += int(line[0])
        if implicit:
            count += int(line[1])
    return count


def update_table1():
    table = []
    with open("benchmark-column.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(21, 24):
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

    field = [0, 0, 0]
    file = "Purpose-Relaxed.md"

    for idx in range(0, 10):
        with open(file, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                l = line.split("|")
                if len(l) > 1:
                    l = l[2 + idx]
                if i in range(7, 31):  # tomoyo
                    field[1] += get_count(l, explicit=True, implicit=True)
                if i in range(32, 53):  # apparmor
                    field[2] += get_count(l, explicit=True, implicit=True)
                if i in range(54, 157):  # selinux
                    field[0] += get_count(l, explicit=True, implicit=True)
            table[21][5 + idx] = str(field[0])
            table[22][5 + idx] = str(field[1])
            table[23][5 + idx] = str(field[2])
    f.close()

    with open("benchmark-column.tex", "w") as f:
        for row in table[0:21]:
            f.write(row)
        for i, row in enumerate(table[21:24]):
            row[0] = row[0].ljust(10)
            for j, e in enumerate(row[1:]):
                row[j + 1] = e.rjust(3)
            line = ' & '.join(row)
            line += ' \\\\'
            if i == 2:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[24:]:
            f.write(row)
        f.close()


def update_table4():
    table = []
    with open("benchmark-implicit.tex", "r") as f:
        for i, line in enumerate(f):
            if i in range(20, 23):
                l = re.split('&|/', line)
                table.append([
                    s.replace("\\", "").replace("hline", "").strip() for s in l
                ])
            else:
                table.append(line)
        f.close()
    for l in table[20:23]:
        print(l)

    field = [0, 0, 0]
    file = "Purpose-Strict.md"
    for idx in range(0, 10):
        with open(file, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                l = line.split("|")
                if len(l) > 1:
                    l = l[2 + idx]
                if i in range(7, 31):  # tomoyo
                    field[1] += get_count(l, explicit=False, implicit=True)
                if i in range(32, 53):  # apparmor
                    field[2] += get_count(l, explicit=False, implicit=True)
                if i in range(54, 157):  # selinux
                    field[0] += get_count(l, explicit=False, implicit=True)
            table[20][3 + idx * 2] = str(field[0])
            table[21][3 + idx * 2] = str(field[1])
            table[22][3 + idx * 2] = str(field[2])
            print(field)
            for l in table[20:23]:
                print(l)
    f.close()

    file = "Purpose-Relaxed.md"
    for idx in range(0, 10):
        with open(file, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                l = line.split("|")
                if len(l) > 1:
                    l = l[2 + idx]
                if i in range(7, 31):  # tomoyo
                    field[1] += get_count(l, explicit=False, implicit=True)
                if i in range(32, 53):  # apparmor
                    field[2] += get_count(l, explicit=False, implicit=True)
                if i in range(54, 157):  # selinux
                    field[0] += get_count(l, explicit=False, implicit=True)
            table[20][4 + idx * 2] = str(field[0])
            table[21][4 + idx * 2] = str(field[1])
            table[22][4 + idx * 2] = str(field[2])
            print(field)
            for l in table[20:23]:
                print(l)
    f.close()

    with open("benchmark-implicit.tex", "w") as f:
        for row in table[0:20]:
            f.write(row)
        for i, row in enumerate(table[20:23]):
            new_row = []
            new_row.append(row[0].ljust(10))
            new_row.append(row[1].ljust(3))
            new_row.append(row[2].ljust(3))
            strict = 0.0
            relaxed = 0.0
            for j in range(3, 22, 2):
                new_row.append((row[j] + '/' + row[j + 1]).rjust(7))
                strict += float(row[j])
                relaxed += float(row[j + 1])
            new_row.append(
                (str(round(100 - 100 * relaxed / strict, 1)) + '\%').rjust(3))
            line = ' & '.join(new_row)
            line += ' \\\\'
            if i == 2:
                line += ' \hline'
            f.write(line + '\n')
        for row in table[23:]:
            f.write(row)
        f.close()
    for l in table[20:23]:
        print(l)


def update_table7():
    table = []
    with open("benchmark-comparison.tex", "r") as f:
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
    file = "Purpose-Baseline.md"
    for idx in range(0, 10):
        with open(file, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                l = line.split("|")
                if len(l) > 1:
                    l = l[2 + idx]
                if i in range(7, 31):  # tomoyo
                    field[1] += get_count(l, explicit=True, implicit=False)
                if i in range(32, 53):  # apparmor
                    field[2] += get_count(l, explicit=True, implicit=False)
                if i in range(54, 157):  # selinux
                    field[0] += get_count(l, explicit=True, implicit=False)
            table[19][3 + idx * 2] = str(field[0])
            table[20][3 + idx * 2] = str(field[1])
            table[21][3 + idx * 2] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    file = "Purpose-Field.md"
    for idx in range(0, 10):
        with open(file, "r") as f:
            field = [0, 0, 0]
            for i, line in enumerate(f):
                l = line.split("|")
                if len(l) > 1:
                    l = l[2 + idx]
                if i in range(7, 31):  # tomoyo
                    field[1] += get_count(l, explicit=True, implicit=False)
                if i in range(32, 53):  # apparmor
                    field[2] += get_count(l, explicit=True, implicit=False)
                if i in range(54, 157):  # selinux
                    field[0] += get_count(l, explicit=True, implicit=False)
            table[19][4 + idx * 2] = str(field[0])
            table[20][4 + idx * 2] = str(field[1])
            table[21][4 + idx * 2] = str(field[2])
            print(field)
            for l in table[19:22]:
                print(l)
    f.close()

    with open("benchmark-comparison.tex", "w") as f:
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
