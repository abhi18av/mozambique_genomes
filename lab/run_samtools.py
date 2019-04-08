import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def has_sam_in_name(string):
    if (string.split(".")[-1] != "sam"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_sam_files = list(filter(lambda x:has_sam_in_name(x), all_files))
                                                                        




def run_samtools_view():

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    genome_name = a_pair[0].split("_")[0]

    genome_1_p = file_location_inside_virtualbox + a_pair[0]
#    print(genome_1_p)

    genome_2_p = file_location_inside_virtualbox + a_pair[1]
#    print(genome_2_p)

    bwa_initial_command = "vagrant ssh -c \"bwa mem -R \\\"@RG\\tID:"

    illumina_string = "\\tSM:Illumina\\\" -M " + file_location_inside_virtualbox + "NC000962_3.fasta "

    cmd = bwa_initial_command +  \
          genome_name +  \
          "\\tSM:" + \
          genome_name + \
          illumina_string + \
          genome_1_p + " " + \
          genome_2_p + " > " + \
          file_location_inside_virtualbox + \
          genome_name + ".sam\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_sam_files:
    run_(a_file)

