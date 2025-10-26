# main.py（有意写得不符合 PEP8）
def   greet(name):
    print("Hello, " + name)  # 多余空格和字符串拼接

def long_line():
    x = "This is a very long string that will exceed the typical 79 or 88 character limit imposed by many linters and style guides, just to demonstrate the linter reporting long lines."
    print(x)

if __name__ == "__main__":
    greet(  "Alice" )
    long_line()
