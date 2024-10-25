import tkinter as tk
from tkinter import scrolledtext

class QCCGUI:
    def __init__(self, master):
        self.master = master
        master.title("Quantum Code Compiler")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.compile_button = tk.Button(master, text="Compile", command=self.compile_code)
        self.compile_button.pack(pady=5)

    def compile_code(self):
        source_code = self.text_area.get("1.0", tk.END)
        compiler = QuantumCodeCompiler()
        machine_code = compiler.compile(source_code)

        if machine_code:
            print("Compilation Successful!")
            print(machine_code)
        else:
            print("Compilation Failed. Check for errors.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = QCCGUI(root)
    root.mainloop()
