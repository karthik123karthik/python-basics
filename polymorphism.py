# poly means many and morphism means forms
# duck typing

class Laptop:

    def code(self, ide):
        ide.execute()  # pyhton only focus on execute func

class Pycharm:

    def execute(self):
        print("Compiling the program")
        print("Running the program")

class Vscode:

    def execute(self):
        print("Running the code")
        print("printing the output")


ide = Pycharm()
l1 = Laptop()
l1.code(ide)