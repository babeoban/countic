import os
import time
import shutil

k = 1

trupe = True

user_home = os.path.expanduser("~")
print("Getting use path: " + user_home)

folder_path = user_home + "\\speedrunigt\\records"

settings = {}
try:
    with open("settings.txt", "r") as f:
        settings_str = f.read()
    for line in settings_str.split("\n"):
        if not line:
            continue
        name, value = line.split("=")
        name = name.strip()
        value = int(value.strip())
        settings[name] = value
except:
    global nether
    global bastion
    global fortress
    global blind
    global eye_spy
    global ee
    global kill
    nether = 0
    bastion = 0
    fortress = 0
    blind = 0
    eye_spy = 0
    ee = 0
    kill = 0
    k=0

if k:
    nether = int(settings["nether"])
    bastion = int(settings["bastion"])
    fortress = int(settings["fortress"])
    blind = int(settings["blind"])
    eye_spy = int(settings["eye_spy"])
    ee = int(settings["ee"])
    kill = int(settings["kill"])

for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        os.remove(item_path)
    elif os.path.isdir(item_path):
        shutil.rmtree(item_path)
print("Removed all items in " + folder_path + " done!")

if not os.path.exists(folder_path):
    print(f"The folder {folder_path} does not exist.")
    time.sleep(5)
    quit()

while True:

    nether_travel_count = 0
    nether_count = 0
    stronghold_count = 0
    edn_count = 0
    bastion_count = 0
    fortress_count = 0
    kill_ender_dragon = 0

    sub_nether = 0
    sub_bastion = 0
    sub_fortress = 0
    sub_blind = 0
    sub_sh = 0
    sub_ee = 0
    sub_kill = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path + "\\" + filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                content = f.read()
                if "nether_travel" in content:
                    nether_travel_count += 1
                    if (blind):
                        for i, line in enumerate(content.split("\n")):
                            if "nether_travel" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < blind:
                                    sub_blind += 1
                if "enter_bastion" in content:
                    bastion_count += 1
                    if (bastion):
                        for i, line in enumerate(content.split("\n")):
                            if "enter_bastion" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < bastion:
                                    sub_bastion += 1                    
                if "enter_fortress" in content:
                    fortress_count += 1
                    if (fortress):
                        for i, line in enumerate(content.split("\n")):
                            if "enter_fortress" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < nether:
                                    sub_fortress += 1                    
                if "enter_nether" in content:
                    nether_count += 1
                    if (nether):
                        for i, line in enumerate(content.split("\n")):
                            if "enter_nether" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < nether:
                                    sub_nether += 1                    
                if "enter_stronghold" in content:
                    stronghold_count += 1
                    if (eye_spy):
                        for i, line in enumerate(content.split("\n")):
                            if "enter_stronghold" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < eye_spy:
                                    sub_sh += 1                    
                if "enter_end" in content:
                    edn_count += 1
                    if (ee):
                        for i, line in enumerate(content.split("\n")):
                            if "enter_end" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                min = int(data/60000)
                                if min < ee:
                                    sub_ee += 1   
                if "kill_ender_dragon" in content:
                    kill_ender_dragon += 1
                    if (kill):
                        for i, line in enumerate(content.split("\n")):
                            if "kill_ender_dragon" in line:
                                line_num = int(i+1)
                                data = content.split("\n")[line_num].strip()
                                data = int(data[7:-1])
                                data = int(data + 10000)
                                min = int(data/60000)
                                if min < kill:
                                    sub_kill += 1   
    
    if (blind):
        print("nether travel: " + str(sub_blind) + "/" + str(nether_travel_count))
        with open("blind.txt", "w") as count_file:
            count_file.write(str(sub_blind) + "/" + str(nether_travel_count))
    else:
        print("nether travel: " + str(nether_travel_count))
        with open("blind.txt", "w") as count_file:
            count_file.write(str(nether_travel_count))
    
    if (bastion):
        print("enter bastion: " + str(sub_bastion) + "/" +  str(bastion_count))
        with open("bastion.txt", "w") as count_file:
            count_file.write(str(sub_bastion) + "/" +  str(bastion_count))
    else:
        print("enter bastion: " + str(bastion_count))
        with open("bastion.txt", "w") as count_file:
            count_file.write(str(bastion_count))

    if(fortress):
        print("enter fortress: " + str(sub_fortress) + "/" + str(fortress_count))
        with open("fortress.txt", "w") as count_file:
            count_file.write(str(sub_fortress) + "/" + str(fortress_count))
    else:
        print("enter fortress: " + str(fortress_count))
        with open("fortress.txt", "w") as count_file:
            count_file.write(str(fortress_count))

    if(nether):
        print("enter nether: " + str(sub_nether) + "/" + str(nether_count))
        with open("nether.txt", "w") as count_file:
            count_file.write(str(sub_nether) + "/" + str(nether_count))
    else:
        print("enter nether: " + str(nether_count))
        with open("nether.txt", "w") as count_file:
            count_file.write(str(nether_count))

    if(eye_spy):
        print("enter stronghold: " + str(sub_sh) + "/" + str(stronghold_count))
        with open("stronghold.txt", "w") as count_file:
            count_file.write(str(sub_sh) + "/" + str(stronghold_count))
    else:
        print("enter stronghold: " + str(stronghold_count))
        with open("stronghold.txt", "w") as count_file:
            count_file.write(str(stronghold_count))

    if(ee):
        print("enter end: " + str(sub_ee) + "/" + str(edn_count))
        with open("edn.txt", "w") as count_file:
            count_file.write(str(sub_ee) + "/" + str(edn_count))
    else:
        print("enter end: " + str(edn_count))
        with open("edn.txt", "w") as count_file:
            count_file.write(str(edn_count))

    if (kill):
        print("ender dragon kills: " + str(sub_kill) + "/" + str(kill_ender_dragon))
        with open("dragon.txt", "w") as count_file:
            count_file.write(str(sub_kill) + "/" + str(kill_ender_dragon))
    else:
        print("ender dragon kills: " + str(kill_ender_dragon))
        with open("dragon.txt", "w") as count_file:
            count_file.write(str(kill_ender_dragon))

    time.sleep(1)

