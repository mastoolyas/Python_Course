import io
# with open("file.txt", "r") as fo:
#     # read data
#     # data = fo.read(10)
#     # data = fo.read()
#     # print(data)
#     # line = fo.readline()
#     # line = fo.readline()
#     # print(line.strip(), end="")
#
#     # l = fo.readlines()
#     # lines = [s.strip() for s in l]
#
#     # l = fo.readlines()
#     for line in fo:
#         print(line.strip())

fo = open("out.txt", "w+")
fo.write("hello\n")
fo.write("all")
fo.write("\nfoo bar")
fo.seek(2, io.SEEK_SET)
data = fo.read(3)
print(data)
size = fo.seek(0, io.SEEK_END)
fo.seek(size - 4, io.SEEK_SET)
fo.write(" mashoo")

# fo.close()
if not fo.closed:
    print("not closed yet....")
    fo.close()


