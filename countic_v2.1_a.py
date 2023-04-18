import os
import time
import shutil
import glob
import json

user_home = os.path.expanduser("~")
print("Getting use path: " + user_home)

folder_path = user_home + "\\speedrunigt\\records"

files = sorted(glob.glob(os.path.join(folder_path, "*")), key=os.path.getmtime)
while True:
    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "enter_nether" in content:
                # Do something with the file that includes "enter_nether"
                for i, line in enumerate(content.split("\n")):
                    if "enter_nether" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("nether_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "enter_nether" is not in the current file name
                continue  # Continue processing files


    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "enter_bastion" in content:
                # Do something with the file that includes "enter_bastion"
                for i, line in enumerate(content.split("\n")):
                    if "enter_bastion" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("bastion_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "enter_bastion" is not in the current file name
                continue  # Continue processing files

    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "enter_fortress" in content:
                # Do something with the file that includes "enter_fortress"
                for i, line in enumerate(content.split("\n")):
                    if "enter_fortress" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("fortress_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "enter_fortress" is not in the current file name
                continue  # Continue processing files

    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "nether_travel" in content:
                # Do something with the file that includes "nether_travel"
                for i, line in enumerate(content.split("\n")):
                    if "nether_travel" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("blind_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "nether_travel" is not in the current file name
                continue  # Continue processing files

    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "enter_stronghold" in content:
                # Do something with the file that includes "enter_stronghold"
                for i, line in enumerate(content.split("\n")):
                    if "enter_stronghold" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("eye_spy_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "enter_stronghold" is not in the current file name
                continue  # Continue processing files

    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "enter_end" in content:
                # Do something with the file that includes "enter_end"
                for i, line in enumerate(content.split("\n")):
                    if "enter_end" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("ee_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "enter_end" is not in the current file name
                continue  # Continue processing files

    for file_path in reversed(files):
        with open(file_path, "r") as f:
            content = f.read()
            if "kill_ender_dragon" in content:
                # Do something with the file that includes "kill_ender_dragon"
                for i, line in enumerate(content.split("\n")):
                    if "kill_ender_dragon" in line:
                        line_num = int(i+1)
                        data = content.split("\n")[line_num].strip()
                        data = int(data[7:-1])
                        data = int(data + 10000)
                        m = int(data/60000)
                        s = int((data - m*60000)/1000)
                        s = str(s)
                        sl = len(s)
                        if sl == 1:
                            s = "0" + str(s)
                        dcm = int(data - int(s)*1000 - m*60000)
                        timea = str(str(m) + ":" + str(s) + "." + str(dcm))
                        print(timea)
                        with open("dragon_last_time.txt", "w") as count_file:
                            count_file.write(str(timea))
                break  # Stop processing files
            else:
                # Skip to the next file if "kill_ender_dragon" is not in the current file name
                continue  # Continue processing files

    print("Done processing files.")
    time.sleep(1)