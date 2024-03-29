# -*- coding: utf-8 -*-

import os
from assistantEVA._version import __version__

eva_logo = "\n" \
           " ███████╗██╗░░░██╗░█████╗░ \n" \
           " ██╔════╝██║░░░██║██╔══██╗ \n" \
           " █████╗░░╚██╗░██╔╝███████║ \n" \
           " ██╔══╝░░░╚████╔╝░██╔══██║ \n" \
           " ███████╗░░╚██╔╝░░██║░░██║ \n" \
           " ╚══════╝░░░╚═╝░░░╚═╝░░╚═╝ "

version_text = "" \
             " -----------------------------------------------\n" \
             " -  EVA  " + "v" + __version__ + "\n" \
             " -----------------------------------------------\n"
             
class OutputStyler:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    """
    Clear stdout
    """
    os.system('cls')

def console_print(text):
    """
    Application print with format.
    :param text: string
    """
    print(OutputStyler.CYAN + text + OutputStyler.ENDC)