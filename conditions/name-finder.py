
names = ["ali", "zeeshan", "hammad", "shaban", "usman", "ahmed"]

fname = input("Find your name: ").strip().lower()

if fname in names:
    print(fname, "is present.")
else:
    print(fname, "not found.")
