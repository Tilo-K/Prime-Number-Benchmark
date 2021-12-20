from termcolor import cprint
import os, time

class Test:
    def __init__(self, name, runcmd, setupcmd=''):
        self.name = name
        self.runcmd = runcmd
        self.setupcmd = setupcmd
        self.time = -1
       
    def setup(self):
        if self.setupcmd == '':
            cprint('[*] No setup needed for ' + self.name, 'yellow')
            return
           
        cprint('[+] Setting up ' + self.name, 'green')
        os.system(self.setupcmd)
        
    def run(self):
        cprint('[+] Running ' + self.name, 'green')
        timeA = time.time()
        os.system(self.runcmd)
        timeB = time.time()
        
        self.time = round(timeB-timeA, 3)
        
        
def main():
    tests = []
    tests.append(Test('Python', 'python3 ./python/primes.py'))
    tests.append(Test('Javascript', 'node ./js/primes.js'))
    tests.append(Test('C', './c/build/primes.exe', 'gcc ./c/primes.c -o ./c/build/primes.exe'))
    
    for test in tests:
        test.setup()
        
    for test in tests:
        test.run()

    columns, lines = os.get_terminal_size()
    
    print('-'*columns)
    
    for test in tests:
        print(test.name, test.time, 's')
        
    print('-'*columns)

if __name__ == '__main__':
    main()