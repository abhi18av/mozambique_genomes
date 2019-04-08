# TODO samtools_index_sorted_bam <<<<<
# samtools index G04868.sorted.bam


import os
import subprocess
import shutil



def has_sorted_in_name(string):
    if (string.split(".")[-2] != "sorted"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_sorted_bam_files = list(filter(lambda x:has_sorted_in_name(x), all_files))




def index_sorted_bam_files(a_sorted_bam_file):




# samtools index G04868.sorted.bam

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    samtools_view_initial_command = "vagrant ssh -c \"samtools index "


    cmd = samtools_view_initial_command +  \
          file_location_inside_virtualbox + \
          a_sorted_bam_file + \
          + "\""

    print(cmd)

    #os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_sorted_bam_files:
    index_sorted_bam_files(f)

