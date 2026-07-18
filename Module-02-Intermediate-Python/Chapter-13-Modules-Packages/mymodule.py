# ==========================================================
#   A CUSTOM MODULE (imported by "Modules and Packages.py")
# ==========================================================

# Any .py file can be imported as a module - there is nothing special
# about this file except that another script says "import mymodule".
# Python finds it because it sits in the same folder as the lesson file.


def greet(name):
    return f"Hello, {name}! Welcome to Python Modules."


def add(a, b):
    return a + b


PI_APPROX = 3.14159


# ==========================================================
#      __name__ == "__main__"
# ==========================================================

# Every module has a built-in variable called __name__.
#
# - If the file is RUN DIRECTLY      -> __name__ == "__main__"
# - If the file is IMPORTED elsewhere -> __name__ == "mymodule"
#
# This lets a module carry quick self-tests that only run when you
# execute the module by itself (python mymodule.py), and stay silent
# when someone else just imports it.

if __name__ == "__main__":
    print(greet("Tester"))
    print(add(2, 3))
