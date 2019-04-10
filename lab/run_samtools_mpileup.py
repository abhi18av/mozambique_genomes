import shutil
import os


all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))


def has_sorted_bam_in_name(string):
    if (string.find("sorted.bam", -10) == -1):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_sorted_bam_files = list(filter(lambda x:has_sorted_bam_in_name(x), all_files))
                                                                        

#for f in all_sorted_bam_files:
#    print(f)


def run_samtools_mpileup(a_sorted_bam_file):


# samtools mpileup -Q 23 -d 2000 -C 50 -ugf NC000962_3.fasta G04868.sorted.bam | bcftools call -O v -vm -o G04868.raw.vcf
    
    vcf_file_name = a_sorted_bam_file.split(".")[0] + ".raw.vcf"

    samtools_mpileup_initial = "samtools mpileup -Q 23 -d 2000 -C 50 -ugf NC000962_3.fasta "


    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
	  samtools_mpileup_initial + \
          a_sorted_bam_file +  \
          " | bcftools call -O v -vm -o " + \
          vcf_file_name + \
          "\""

    print(cmd)

    #os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_file in all_sorted_bam_files:
    run_samtools_mpileup(a_file)
