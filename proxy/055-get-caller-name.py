import sys
import inspect

def stack(context=1):
    """Return a list of records for the stack above the caller's frame."""
    print(inspect.stack()[1].function) # this will print the function name
    return inspect.getouterframes(sys._getframe(1), context)


class A:

    def another_test(self):
        return stack()


    @staticmethod
    def test_function():
        stack()


def test():
    print(stack())

print(stack())
print("##############")
test()
print("##############")
A.test_function()
print("##############")
a = A()
out = a.another_test()
print(out)
'''
<module>
[FrameInfo(frame=<frame at 0x7f8036e86640, file './055-get-caller-name.py', line 24, code <module>>, filename='./055-get-caller-name.py', lineno=24, function='<module>', code_context=['print(stack())\n'], index=0)]
##############
test
[FrameInfo(frame=<frame at 0x1b9cde0, file './055-get-caller-name.py', line 22, code test>, filename='./055-get-caller-name.py', lineno=22, function='test', code_context=['    print(stack())\n'], index=0), FrameInfo(frame=<frame at 0x7f8036e86640, file './055-get-caller-name.py', line 26, code <module>>, filename='./055-get-caller-name.py', lineno=26, function='<module>', code_context=['test()\n'], index=0)]
##############
test_function
##############
another_test
[FrameInfo(frame=<frame at 0x7f8036d041d0, file './055-get-caller-name.py', line 13, code another_test>, filename='./055-get-caller-name.py', lineno=13, function='another_test', code_context=['        return stack()\n'], index=0), FrameInfo(frame=<frame at 0x7f8036e86640, file './055-get-caller-name.py', line 32, code <module>>, filename='./055-get-caller-name.py', lineno=31, function='<module>', code_context=['out = a.another_test()\n'], index=0)]
'''