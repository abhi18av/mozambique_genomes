import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def has_filt_vcf_in_name(string):
    if (string.find(".filt.vcf", -9) == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_filt_vcf_files = list(filter(lambda x:has_filt_vcf_in_name(x), all_files))
                                                                        

#for f in all_filt_vcf_files:
#    print(f)


def bgzip_filt_vcf(a_raw_vcf_file):

#bgzip -c G04868.filt.vcf > G04868.filt.vcf.gz
    
    filt_vcf_file_name = a_raw_vcf_file.split(".")[0] + ".filt.vcf.gz"

    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "bgzip -c " + \
          a_raw_vcf_file + \
          " > " + \
          filt_vcf_file_name + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_filt_vcf_files:
    bgzip_filt_vcf(a_file)

