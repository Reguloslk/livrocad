from interface.tela_principal import TelaPrincipal
import tkinter as tk


def main():
    root = tk.Tk()
    app = TelaPrincipal(root)
    root.mainloop()


if __name__ == "__main__":
    main()
