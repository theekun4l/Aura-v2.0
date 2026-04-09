import sys,time

class Text_Animator():
    def type_animator(self, text, new_line):
        for ch in text:
            if ch == '.':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.8)
            elif ch == '\n':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.08)
            elif ch == ',':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.25)
            elif ch == '?':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.7)
            elif ch == '!':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.4)
            elif ch == ' ':
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.01)
            else:
                sys.stdout.write(ch)
                sys.stdout.flush()
                time.sleep(0.04)
        if new_line == True:
            sys.stdout.write('\n')
            sys.stdout.flush()