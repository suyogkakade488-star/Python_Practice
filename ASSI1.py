'''WAP to greet all personh names stored in a list l1  and which start with s
and ends with a'''
list = ["suyog","sachin","priya","kunal"]
for name in list:
    if(name.startswith("s")):
        print(f"hello {name}")
    if(name.endswith("a")):
        print(f"hello {name}")
    