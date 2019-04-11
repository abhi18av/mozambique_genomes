# TODO snippy_command <<<<<
# snippy --cpus 4 --outdir G04868 --ref ./NC000962_3.gbk --R1 ./G04868_1.fastq.gz --R2 ./G04868_2.fastq.gz



import shutil
import os

# # TODO create pairs of genomes based on same first name

# all_files = [f for f in os.listdir() if  os.path.isfile(f)]



# def has_fastq_in_name(string):
#     if (string.find("fastq") == -1):
#         #print("NO")
#         return 0
#     else:
#         #print("YES")
#         return 1


# all_fastq_files = list(filter(lambda x:has_fastq_in_name(x), all_files))


all_dirs =  [f for f in os.listdir() if os.path.isdir(f)] 
all_dirs.remove('spotyping')
all_dirs.remove('uploaded')


dir_string = " "
for a_dir in all_dirs:
    dir_string =  dir_string + " " + a_dir



def run_snippy_core():

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"



    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "snippy-core " + \
          dir_string + \
          "\""


    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



run_snippy_core()

