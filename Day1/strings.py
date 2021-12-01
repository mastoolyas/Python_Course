s1 = """aaa
    bbb
  xx
zz    
"""
s3 = r"C:\temp\newfile" # C:\\temp\\newfile rew-string
print(s3[0:3]) # c:\
print(s3[:3])  # c:\
print(s3[3:])  # temp\newfile
print(s3[:-1]) # C:\temp\newfil
print(s3[:15]) # C:\temp\newfile
print(s3[80:81] == "") # true, no exp. in :
print(s3[::2]) # C\epnwie jump 2
print(s3[::-1]) # elifwen\pmet\:C

print(s3.upper()) # C:\TEMP\NEWFILE cannot change string, but in print or s = s it works
s = input("Enter a number:") # input always return string
if s.isnumeric():
    s = int(s)
    print(s ** 3)
else:
    print("Not a number")

