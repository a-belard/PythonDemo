import re


def arithmetic_arranger(problems):
    if len(problems) > 5:
      return "Error: Too many problems."
    upperline = ""
    secline = ""
    thirdline = ""
    lastline = ""
    arranged_problems = ""
    for i in problems:
        if "*" in i or "/" in i:
            return "Error: Operator must be '+' or '-'."
        if not re.search(r"[0-9\s\+\-]", i):
            return "Error: Numbers must only contain digits."
        operator = "+" if "+" in i else "-"
        numbers = [k.strip() for k in i.split(operator)]
        for j in numbers:
            if len(j) > 4:
                return "Error: Numbers cannot be more than four digits."
            if not j.isnumeric():
                return "Error: Numbers must only contain digits."
        result = eval(i)
        maxLength = max([len(str(result)), len(numbers[0]), len(numbers[1])])
        upperline += str(numbers[0]).rjust(maxLength + 4, " ")
        secline += "  {} {}".format(operator, numbers[1].rjust(maxLength, " "))
        thirdline += "  {}".format("-" * (maxLength + 2))
        lastline += str(result).rjust(maxLength + 4, " ")

    for line in [upperline[2:], secline.strip(), thirdline.strip()]:
        arranged_problems += line + "\n"

    arranged_problems += lastline[2:]
    return arranged_problems


print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
