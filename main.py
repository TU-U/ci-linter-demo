# main.py (已修复)
def greet(name):
    print(f"Hello, {name}")


def long_line():
    x = (
        "This is a long string split across multiple lines so that it does not"
        " exceed the recommended maximum line length."
    )
    print(x)


if __name__ == "__main__":
    greet("Alice")
    long_line()
