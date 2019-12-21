import itertools

aa = [int(x) for x in input().split(',')]


output = ""
class CPU:
    def __init__(self, tape):
        self.a = tape[:] + [0]*10000
        self.i = 0
        self.rel_base = 0
    def run(self):
        global output
        def get_value(value, mode):
            if mode == 2:
                return self.a[value + self.rel_base]
            elif mode == 1:
                return value
            else:
                return self.a[value]
        def set_value(loc, mode, new_val):
            if mode == 2:
                self.a[loc + self.rel_base] = new_val
            elif mode == 0:
                self.a[loc] = new_val
            else:
                raise ValueError("mode for set_value is not 0 or 2")
        # rel_base = 0
        # i = 0
        while self.a[self.i] != 99:
            code = self.a[self.i]%100
            params = self.a[self.i]//100
            m3,m2,m1 = params//100, (params//10)%10, params%10

            x, y, z = self.a[self.i+1], self.a[self.i+2], self.a[self.i+3]
            if code == 1:
                #print(get_value(x,m1), get_value(y, m2))
                new_val = get_value(x, m1) + get_value(y, m2)
                set_value(z, m3, new_val)
                self.i += 4
            elif code == 2:
                new_val = get_value(x, m1) * get_value(y, m2)
                set_value(z, m3, new_val)
                self.i += 4
            elif code == 3:
                # GET INPUT
                n = inputs.pop()
                set_value(x, m1, n)
                self.i += 2
            elif code == 4:
                # OUTPUT
                out = get_value(x, m1) # to get the answer when it all works
                # output +=  chr(out) # to print the debug outputs
                print(out)
                self.i += 2
            elif code == 5:
                if get_value(x, m1):
                    self.i = get_value(y, m2)
                else:
                    self.i += 3
            elif code == 6:
                if not get_value(x, m1):
                    self.i = get_value(y, m2)
                else:
                    self.i += 3
            elif code == 7:
                if get_value(x, m1) < get_value(y, m2):
                    set_value(z, m3, 1)
                else:
                    set_value(z, m3, 0)
                self.i += 4
            elif code == 8:
                if get_value(x, m1) == get_value(y, m2):
                    set_value(z, m3, 1)
                else:
                    set_value(z, m3, 0)
                self.i += 4
            elif code == 9:
                self.rel_base += get_value(x, m1)
                self.i += 2
            else:
                raise ValueError(a[i])

c = CPU(aa)
# PART 1:
# inputs = """NOT A T
# OR T J
# NOT B T
# OR T J
# NOT C T
# OR T J
# AND D J
# WALK
# """

# PART 2:
inputs = """NOT A T
OR T J
NOT B T
OR T J
NOT C T
OR T J
AND D J
AND E T
OR H T
AND T J
RUN
"""
inputs = list(ord(x) for x in inputs)
inputs.reverse()
c.run()
print(output)