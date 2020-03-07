message = input()
with open("badwords.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line)
for x in range(len(lines)):
    lines[x] = lines[x][len(lines[x]) - 2]
while (message != "exit"):
    printable = True
    # print(lines)
    for x in range(len(lines)):
        if (lines[x] in message):
            printable = False
    if (printable):
        print(message)
    else:
        print("message redacted")
    message = input()
