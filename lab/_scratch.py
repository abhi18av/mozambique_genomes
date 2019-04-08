# TODO convert_sam_file_to_bam_file <<<<<
# samtools view -bt NC000962_3.fasta.fai G04868.sam > G04868.bam

import os
import subprocess
import shutil



def has_sam_in_name(string):
    if (string.split(".")[-1] != "sam"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_sam_files = list(filter(lambda x:has_sam_in_name(x), all_files))
all_sam_files.remove('PT000033.sam')




def convert_sam_file_to_bam_file(a_sam_file):



# samtools view -bt NC000962_3.fasta.fai \
# G04868.sam \
# > G04868.bam

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    sam_file_name = file_location_inside_virtualbox +  a_sam_file.split(".")[0]
    bam_file_name = sam_file_name + ".bam"

    samtools_view_initial_command = "vagrant ssh -c \"samtools view -bt "
    reference_file = file_location_inside_virtualbox + "NC000962.fasta.fai "


    cmd = samtools_view_initial_command +  \
          reference_file + \
          file_location_inside_virtualbox + \
          a_sam_file + \
          " > " + \
          bam_file_name + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_sam_files:
    convert_sam_file_to_bam_file(f)

