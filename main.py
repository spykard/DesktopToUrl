import sys
import os

if __name__== "__main__": 
    if len(sys.argv) < 2:
        sys.exit("The directory path must be passed as an argument in a Windows format: ...\...\...")
    elif len(sys.argv[1].split("\\")) < 2:
        sys.exit("The directory path must be passed as an argument in a Windows format: ...\...\...")
  
    mode = input(".DESKTOP to .URL or .URL to .DESKTOP [0/1] ")
    count = 0
    
    direntry_obj = os.scandir(sys.argv[1])
    if mode == "0":  # .DESKTOP to .URL
        for entry in direntry_obj:
            if entry.is_file():
                if entry.name.endswith(".desktop") or entry.name.endswith(".DESKTOP"):
                    f_from = open(entry.path, 'r')
                    t_from = f_from.read().split("\n")
                    f_to = open(entry.path[:-8] + ".url", 'w')
                    
                    if len(t_from) > 4 and t_from[0] == "[Desktop Entry]":
                        f_to.write("[InternetShortcut]")
                        f_to.write("\n" + t_from[4] + "\n")

                    count += 1
                    f_from.close()
                    f_to.close()
    elif mode == "1":  # .URL to .DESKTOP
        for entry in direntry_obj:
            if entry.is_file():
                if entry.name.endswith(".url") or entry.name.endswith(".URL"):
                    f_from = open(entry.path, 'r')
                    t_from = f_from.read().split("\n")
                    f_to = open(entry.path[:-4] + ".desktop", 'w')
                                      
                    if len(t_from) > 1 and t_from[0] == "[InternetShortcut]":
                        f_to.write("[Desktop Entry]")
                        f_to.write("\nEncoding=UTF-8")
                        f_to.write("\nName=" + entry.name[:-4])
                        f_to.write("\nType=Link")
                        f_to.write("\n" + t_from[1] + "\n")

                    count += 1
                    f_from.close()
                    f_to.close()
    else:
        sys.exit("Invalid mode")
    
    print("Completed conversion of", count, "files")