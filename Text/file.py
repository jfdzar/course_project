file = open('example.txt')

content=file.read()

print(content)

file.seek(0)
content = file.readlines()
content = [i.strip('\n') for i in content]
print(content)

file.close()
