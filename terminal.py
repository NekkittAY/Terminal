import os
import inspect

class Terminal:
    def __init__(self):
        self.func = None

    def find(self,file,path):
        global direct
        for file0 in os.listdir(path):
            if file0 == file:
                direct = path+"\\"+file0
                break
            else:
                try:
                    new_path = path+"\\"+file0
                    self.find(file,new_path)
                except:
                    pass
        return direct

    def remove(self,path):
        for list1 in os.listdir(path):
            try:
                os.remove(path+"/"+list1)
            except:
                remove(path+"/"+list1)
        os.rmdir(path)
        return "deleted"

    def help(self):
        print("find       find file")
        print("remove     remove file")
        return "help       command list"

def Args(func):
    args = []
    sig = inspect.signature(functions[func])
    params = inspect.getfullargspec(functions[func])
    for i in range(len(sig.parameters)):
        arg = input(str(params[0][i+1])+": ")
        args.append(arg)
    return args

terminal = Terminal()
functions = {"find":terminal.find,
             "remove":terminal.remove,
             "help":terminal.help}

while True:
    func = input(">")
    args = Args(func)
    result = functions[func](*args)
    print(result)
