import controller

convert = controller.DataController.convert

f = open("sample.json")

raw = convert(f)

print(raw["patient"])

f.close()
