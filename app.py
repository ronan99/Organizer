import sys, ctypes
sys.path.append('./')
from helpers.organizer import *
from helpers.admin_request import is_admin

if __name__ == "__main__":
    # if is_admin():
        dir_path = input("Digite o caminho ou pressione enter para ser o diretório atual a ser organizado!\n")
        print(organize_junk(dir_path))
    # else:
        # Re-run the program with admin rights
        # ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    