def arithmetic_arranger(problems, showResults = False):
    firstLine = ""
    secondLine = ""
    lines = ""
    finalResult = ""
    if len(problems) < 5:
        for i in range(len(problems)):
            newOperation = problems[i].split()
            firstNumber = str(newOperation[0])
            operator = str(newOperation[1])
            secondNumber = str(newOperation[2])
            line = ""
            lineLength = max(len(newOperation[0]), len(newOperation[2])) + 2
            for y in range(lineLength):
                line = line + "-"
            try:
                int(newOperation[0]) and int(newOperation[2])
                if len(newOperation[0]) < 5 and len(newOperation[2]) < 5:
                    if newOperation[1] == "+":
                        result = int(newOperation[0]) + int(newOperation[2])
                    elif newOperation[1] == "-":
                        result = int(newOperation[0]) - int(newOperation[2])
                    else:
                        return "Error: Operator must be '+' or '-'."
                    top = firstNumber.rjust(lineLength)
                    bottom = operator + secondNumber.rjust(lineLength - 1)
                    res = str(result).rjust(lineLength)
                else:
                    return "Error: Numbers cannot be more than four digits."
            except:
                return "Error: Numbers must only contain digits."
            if i != problems[-1]:
                firstLine += top + '    '
                secondLine += bottom + '    '
                lines += line + '    '
                finalResult += res + '    '
            else:
                firstLine += top
                secondLine += bottom
                lines += line
                finalResult += res
    else:
        return "Error: Too many problems."
    firstLine.rstrip()
    secondLine.rstrip()
    lines.rstrip()
    if showResults:
        finalResult.rstrip()
        arranged_problems = firstLine + "\n" + secondLine + "\n" + lines + "\n" + finalResult
    else:
        arranged_problems = firstLine + "\n" + secondLine + "\n" + lines
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3815 - 2", "45 + 43", "123 + 49"], showResults = True))

#str(f"{newOperation[0]:>5}")
#str(f"{newOperation[2]:>3}")
#answer = answer + firstOperand + "\n" + newOperation[1] + " " + secondOperand + "\n" + line + "\n" + finalResult + "\n" + "    "