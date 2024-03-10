subjects = {}
print("Insert how many subjects we have")
num = int(input())
for x in range(num):
    print("Insert subject name")
    name = input()
    print("Insert subject score")
    score = int(input())
    subjects[name] = score

result = 0
for key, value in subjects.items():
    print(key, value)
    result += value

print("Your yearly score is %s" % (result/ len(subjects)))

