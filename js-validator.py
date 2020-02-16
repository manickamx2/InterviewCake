import unittest

# Determine if the input code is valid
def is_valid(code):
    if code:
        if code == '': # if empty string
            return True
        else: # greedy approach using a stack
            stack = []
            openers = ['{', '[', '(']
            for operator in code:
                if operator in openers:
                    stack.append(operator)
                else: # meaning operator is a closing bracket
                    if len(stack) == 0: # stack is empty.
                        return False
                    else:
                        recent = stack.pop()
                    # check matching opening operator for closing operator
                    if recent == '{' and operator == '}':
                        continue
                    elif recent == '(' and operator == ')':
                        continue
                    elif recent == '[' and operator == ']':
                        continue
                    else:
                        return False
            return len(stack) == 0 # stack would be empty if valid, o.w. False.
    else:
        return True


# Tests
class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)

unittest.main(verbosity=2)
