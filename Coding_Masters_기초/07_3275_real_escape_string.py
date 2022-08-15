str1 = input()

str1 = str1.replace("\\", "\\\\")
str1 = str1.replace("\'", "\\\'")
str1 = str1.replace("\"", "\\\"")
print(str1)
