import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def has_filt_vcf_gz_in_name(string):
    if (string.find(".filt.vcf.gz", -12) == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_filt_vcf_gz_files = list(filter(lambda x:has_filt_vcf_gz_in_name(x), all_files))
                                                                        

#for f in all_filt_vcf_gz_files:
#    print(f)



def run_tabix(a_filt_vcf_gz_file):

#tabix -p vcf G04868.filt.vcf.gz
    

    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "tabix -p vcf " + \
          a_filt_vcf_gz_file + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_filt_vcf_gz_files:
    run_tabix(a_file)
