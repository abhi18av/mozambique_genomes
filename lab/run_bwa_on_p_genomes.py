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


genome_pairs = [

["118_cat_R1.p.fastq",
"118_cat_R2.p.fastq"],

["141_cat_R1.p.fastq",
"141_cat_R2.p.fastq"],

["1507_cat_R1.p.fastq",
"1507_cat_R2.p.fastq"],

["1689_cat_R1.p.fastq",
"1689_cat_R2.p.fastq"],

["1728_cat_R1.p.fastq",
"1728_cat_R2.p.fastq"],

["1866_cat_R1.p.fastq",
"1866_cat_R2.p.fastq"],

["1869_cat_R1.p.fastq",
"1869_cat_R2.p.fastq"],

["205_cat_R1.p.fastq",
"205_cat_R2.p.fastq"],

["2065_cat_R1.p.fastq",
"2065_cat_R2.p.fastq"],

["2078_S14_L001_R1_001.p.fastq",
"2078_S14_L001_R2_001.p.fastq"],

["208_cat_R1.p.fastq",
"208_cat_R2.p.fastq"],

["2136_cat_R1.p.fastq",
"2136_cat_R2.p.fastq"],

["2235_cat_R1.p.fastq",
"2235_cat_R2.p.fastq"],

["227_S3_L001_R1_001.p.fastq",
"227_S3_L001_R2_001.p.fastq"],

["2330_S17_L001_R1_001.p.fastq",
"2330_S17_L001_R2_001.p.fastq"],

["2368_cat_R1.p.fastq",
"2368_cat_R2.p.fastq"],

["2422_cat_R1.p.fastq",
"2422_cat_R2.p.fastq"],

["243_S5_L001_R1_001.p.fastq",
"243_S5_L001_R2_001.p.fastq"],

["2440_S20_L001_R1_001.p.fastq",
"2440_S20_L001_R2_001.p.fastq"],

["2449_cat_R1.p.fastq",
"2449_cat_R2.p.fastq"],

["2683_cat_R1.p.fastq",
"2683_cat_R2.p.fastq"],

["2721_cat_R1.p.fastq",
"2721_cat_R2.p.fastq"],

["2852_S25_L001_R1_001.p.fastq",
"2852_S25_L001_R2_001.p.fastq"],

["3026_S26_L001_R1_001.p.fastq",
"3026_S26_L001_R2_001.p.fastq"],

["3033_cat_R1.p.fastq",
"3033_cat_R2.p.fastq"],

["3141_cat_R1.p.fastq",
"3141_cat_R2.p.fastq"],

["316_S5_L001_R1_001.p.fastq",
"316_S5_L001_R2_001.p.fastq"],

["3185_cat_R1.p.fastq",
"3185_cat_R2.p.fastq"],

["3376_cat_R1.p.fastq",
"3376_cat_R2.p.fastq"],

["370_cat_R1.p.fastq",
"370_cat_R2.p.fastq"],

["509_S6_L001_R1_001.p.fastq",
"509_S6_L001_R2_001.p.fastq"],

["581_cat_R1.p.fastq",
"581_cat_R2.p.fastq"],

["751_S8_L001_R1_001.p.fastq",
"751_S8_L001_R2_001.p.fastq"],

["894_S9_L001_R1_001.p.fastq",
"894_S9_L001_R2_001.p.fastq"],

["964_S10_L001_R1_001.p.fastq",
"964_S10_L001_R2_001.p.fastq"]


     ]





# bwa mem -R "@RG \
#       ID:118  
#       SM:118  
#       SM:Illumina" -M NC000962_3.fasta 
#       118_R1.p.fastq 
#       118_R2.p.fastq 
#       > 118.sam"




def run_bwa(a_pair):

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



for a_pair in genome_pairs:
    run_bwa(a_pair)

