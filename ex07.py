# exercies 7: More Printing
mm = "Mary had a little lamb"
print (mm)

m = mm.split(" ")
i = 0
for x in m:
    if len(x) == 4:
        i = i + 1
print (i)
print (m)
print ("Its fleece was white as {}.".format("snow"))
print ("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
