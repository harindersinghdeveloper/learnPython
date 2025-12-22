import os

print(os.getcwd())
print(os.listdir())
print(os.listdir('C:\\Users\\harinder.singh'))

file_path = "C:\\Users\\harinder.singh\\Downloads"

for folder,sub_folders,files in os.walk(file_path):
    print(f"Folder :{folder}")
    print(f"     Sub-Folders:")
    for s_b in sub_folders:
        print(f"          {s_b}")
    print(f"     Files:")
    for s_f in files:
        print(f"          {s_f}")
