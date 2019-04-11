import os
import subprocess
import shutil


#######
# SCRATCH

# all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


# for f in all_files:
#     subprocess.call(["rclone","copy", f , "onedrive-abhi:ena-genomes", "-vv"])

#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv


#######



#rclone copy ERR036201_1.fastq.gz onedrive-abhi:ena-genomes -vv

def has_xls_in_name(string):
    if (string.find("xls") == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))
all_xls_files = list(filter(lambda x:has_xls_in_name(x), all_files))


for f in all_xls_files:
    subprocess.call(["rclone","copy", f , "onedrive-abhi:mozambique-genomes/lab/spotyping", "-vv"])
    shutil.move(f,"./uploaded/")


