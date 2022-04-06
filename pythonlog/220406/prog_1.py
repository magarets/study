def get_peri(x):
    return x**2*3.14

Uinput = input(f"get_peri() = ")

if( Uinput == ""):
    print(get_peri(5.0))
else:
    Uinput = float(Uinput)
    print(get_peri(Uinput))
