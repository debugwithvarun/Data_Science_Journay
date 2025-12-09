a=2

try:
    c=a/"e"
# except ZeroDivisionError as e:
#     print("error")
except Exception as e:
    print("error")
else:
    print("no error")

finally:
    print("always execute")
