import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def a_filt_vcf_in_name(string):
    if (string.find(".filt.vcf", -9) == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_filt_vcf_file = list(filter(lambda x:a_filt_vcf_in_name(x), all_files))
                                                                        

#for f in all_filt_vcf_file:
#    print(f)



def run_snpeff(a_filt_vcf_file):


#java -Xmx4g -jar /opt/snpEff/snpEff.jar -no-downstream -no-upstream -v -c /opt/snpEff/snpEff.config NC000962_3 G04868.filt.vcf > G04868.ann.vcf.gz

    ann_vcf_gz_file = a_filt_vcf_file.split(".")[0] + ".ann.vcf.gz"

    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "java -Xmx4g -jar /opt/snpEff/snpEff.jar -no-downstream -no-upstream -v -c /opt/snpEff/snpEff.config NC000962_3 " + \
          a_filt_vcf_file + \
          " > " + \
          ann_vcf_gz_file + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_filt_vcf_file:
    run_snpeff(a_file)
