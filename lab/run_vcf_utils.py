import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def has_raw_vcf_in_name(string):
    if (string.find(".raw.vcf", -8) == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_raw_vcf_files = list(filter(lambda x:has_raw_vcf_in_name(x), all_files))
                                                                        

#for f in all_raw_vcf_files:
#    print(f)

def run_vcf_utils(a_raw_vcf_file):


#vcfutils.pl varFilter -d 10 -D 2000 G04868.raw.vcf > G04868.filt.vcf
    
    filt_vcf_file_name = a_raw_vcf_file.split(".")[0] + ".filt.vcf"

    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "vcfutils.pl varFilter -d 10 _d 2000 " + \
          a_raw_vcf_file + \
          " > " + \
          filt_vcf_file_name + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_raw_vcf_files:
    run_vcf_utils(a_file)
