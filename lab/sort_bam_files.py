# TODO sort_bam_file <<<<<
# samtools sort G04868.bam -o G04868.sorted.bam

import os
import subprocess
import shutil



def has_bam_in_name(string):
    if (string.split(".")[-1] != "bam"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_bam_files = list(filter(lambda x:has_bam_in_name(x), all_files))




def sort_bam_files(a_bam_file):




# samtools sort G04868.bam -o G04868.sorted.bam


    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    bam_file_name = file_location_inside_virtualbox + a_bam_file.split(".")[0]
    sorted_bam_file_name = bam_file_name + ".sorted.bam"

    samtools_view_initial_command = "vagrant ssh -c \"samtools sort "


    cmd = samtools_view_initial_command +  \
          file_location_inside_virtualbox + \
          a_bam_file + \
          " -o " + \
          sorted_bam_file_name + "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_bam_files:
    sort_bam_files(f)

