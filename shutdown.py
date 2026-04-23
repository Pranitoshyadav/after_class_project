import os
import sys

def shutdown(option="system"):
    if option == "program":
        print("Shutting down the program...")
        sys.exit()
    elif option == "system":
        print("Shutting down the computer...")
        # Windows shutdown command
        os.system("shutdown /s /t 1")
    else:
        print("Invalid option. Use 'program' or 'system'.")

shutdown()