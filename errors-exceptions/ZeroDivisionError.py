# In math there are rules about dividing by zero. 
# It is trying to do just that and will throw a ZeroDivisionError. 
# Add exception handling to return back 0 instead of allowing the error to be thrown.

def divide_by(a, b):
    
    try:
        return a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(e, "Something went wrong")

ans = divide_by(40, 0)
print(ans)


# 0