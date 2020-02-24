# -*- coding: utf-8 -*-

from utils.console_utils import eva_logo, version_text, OutputStyler, clear, console_print

class consoleEVA:
    def __init__(self):
        self.logLineCount = 1
        self.logHistory = []
        pass
    
    def console_output(self, text):
        if self.logLineCount > 10:
            self.logLineCount = 1
            self.logHistory = []
        
        clear()
        
        console_print(version_text)
        console_print(eva_logo)     
        console_print("  NOTE: Say 'shut down' to quit EVA assistant")
        
        self.logLineCount += 1
        self.logHistory.append(text)
        
        print(OutputStyler.HEADER + '-------------- CHAT LOG --------------' + OutputStyler.ENDC)
        for line in self.logHistory:        
            print(OutputStyler.BOLD + '> ' + line + '\r' + OutputStyler.ENDC)