import os
import time
import shutil

user_home = os.path.expanduser("~")
print("Getting use path: " + user_home)

folder_path = user_home + "\\speedrunigt\\records"

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

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path + "\\" + filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                content = f.read()
                if "nether_travel" in content:
                    nether_travel_count += 1
                if "enter_bastion" in content:
                    bastion_count += 1
                if "enter_fortress" in content:
                    fortress_count += 1
                if "enter_nether" in content:
                    nether_count += 1
                if "enter_stronghold" in content:
                    stronghold_count += 1
                if "enter_end" in content:
                    edn_count += 1
                if "kill_ender_dragon" in content:
                    kill_ender_dragon += 1
    
    print("nether travel: " + str(nether_travel_count))
    print("enter bastion: " + str(bastion_count))
    print("enter fortress: " + str(fortress_count))
    print("enter nether: " + str(nether_count))
    print("enter stronghold: " + str(stronghold_count))
    print("enter end: " + str(edn_count))
    print("ender dragon kills: " + str(kill_ender_dragon))

    with open("blind.txt", "w") as count_file:
        count_file.write(str(nether_travel_count))
    with open("nether.txt", "w") as count_file:
        count_file.write(str(nether_count))
    with open("bastion.txt", "w") as count_file:
        count_file.write(str(bastion_count))
    with open("fortress.txt", "w") as count_file:
        count_file.write(str(fortress_count))
    with open("stronghold.txt", "w") as count_file:
        count_file.write(str(stronghold_count))
    with open("edn.txt", "w") as count_file:
        count_file.write(str(edn_count))
    with open("dragon.txt", "w") as count_file:
        count_file.write(str(kill_ender_dragon))

    time.sleep(1)

