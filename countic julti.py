import json
import time
import os

user_home = os.path.expanduser("~")
print("Getting use path:" + user_home)
profile_path = user_home + "\.Julti\selectedprofile.txt"

if not os.path.exists(profile_path):
    print(f"\.Julti\selectedprofile.txt does not exist")
    time.sleep(5)
    quit()
print("Getting profile path: " + profile_path)
with open(profile_path, 'r') as f:
    profile = f.read()
data_path = user_home + "\.Julti\profiles\\" + profile + ".json"
if not os.path.exists(profile_path):
    print(f"\.Julti\profiles\\" + profile + ".json does not exist")
    time.sleep(5)
    quit()
print("Getting active profile: " + data_path)

with open(data_path, 'r') as f:
    data = json.load(f)

log_file_paths = [inst + '\\logs\\latest.log' for inst in data['lastInstances']]
print("Getting logs file path")
print(log_file_paths)

while True:
    total_nether_count = 0
    total_stronghold_count = 0
    total_edn_count = 0
    total_bastion_count = 0
    total_fortress_count = 0
    
    for log_file_path in log_file_paths:
        nether_count = 0
        stronghold_count = 0
        edn_count = 0
        bastion_count = 0
        fortress_count = 0
        
        with open(log_file_path, 'r') as f:
            for line in f:
                if "We Need to Go Deeper" in line:
                    nether_count += 1
                if "Eye Spy" in line:
                    stronghold_count += 1    
                if "The End?" in line:
                    edn_count += 1
                if "Those Were the Days" in line:
                    bastion_count += 1
                if "A Terrible Fortress" in line:
                    fortress_count += 1
        nether_count //= 2
        total_nether_count += nether_count
        stronghold_count //= 2
        total_stronghold_count += stronghold_count
        edn_count //= 2
        total_edn_count += edn_count
        bastion_count //= 2
        total_bastion_count += bastion_count
        fortress_count //= 2
        total_fortress_count += fortress_count
        
        print("The phrase 'We Need to Go Deeper' appears", nether_count, "times in the file", log_file_path)
        print("The phrase 'Eye Spy' appears", stronghold_count, "times in the file", log_file_path)
        print("The phrase 'Eye Spy' appears", stronghold_count, "times in the file", log_file_path)
        print("The phrase 'Those Were the Days' appears", bastion_count, "times in the file", log_file_path)
        print("The phrase 'A Terrible Fortress' appears", fortress_count, "times in the file", log_file_path)
    
    print("The phrase 'We Need to Go Deeper' appears", total_nether_count, "times in all log files.")
    print("The phrase 'Eye Spy' appears", total_stronghold_count, "times in all log files.")
    print("The phrase 'The End?' appears", total_edn_count, "times in all log files.")
    print("The phrase 'Those Were the Days' appears", total_bastion_count, "times in all log files.")
    print("The phrase 'A Terrible Fortress' appears", total_fortress_count, "times in all log files.")
    
    with open("nether.txt", "w") as count_file:
        count_file.write(str(total_nether_count))

    with open("stronghold.txt", "w") as count_file:
        count_file.write(str(total_stronghold_count))

    with open("edn.txt", "w") as count_file:
        count_file.write(str(total_edn_count))
    
    with open("bastion.txt", "w") as count_file:
        count_file.write(str(total_bastion_count))
    
    with open("fortress.txt", "w") as count_file:
        count_file.write(str(total_fortress_count))

    time.sleep(1)
