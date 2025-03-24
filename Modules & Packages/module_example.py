from MainPackage import my_main_script
from MainPackage.SubPackage import my_sub_script

if __name__ == "__main__":
    
    print("'module_example.py' is directly executed.\n")
    my_main_script.main_report()
    my_sub_script.sub_report()
