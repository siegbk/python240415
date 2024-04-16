#DemoFile.py

#write unicode
f = open("demo.txt", "wt", encoding="utf-8")
f.write("first\nsecond\nthird3")
f.close()

#read
r = open("demo.txt", "rt", encoding="utf-8")
print(r.read())
r.close()
