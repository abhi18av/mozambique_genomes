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


    ["118_cat_R1.fastq.gz",
     "118_cat_R2.fastq.gz"],

    ["141_cat_R1.fastq.gz",
     "141_cat_R2.fastq.gz"],

    ["205_cat_R1.fastq.gz",
     "205_cat_R2.fastq.gz"],

    ["208_cat_R1.fastq.gz",
     "208_cat_R2.fastq.gz"],

    ["227_S3_L001_R1_001.fastq.gz",
     "227_S3_L001_R2_001.fastq.gz"],

    ["243_S5_L001_R1_001.fastq.gz",
     "243_S5_L001_R2_001.fastq.gz"],

    ["316_S5_L001_R1_001.fastq.gz",
     "316_S5_L001_R2_001.fastq.gz"],

    ["370_cat_R1.fastq.gz",
     "370_cat_R2.fastq.gz"],

    ["509_S6_L001_R1_001.fastq.gz",
     "509_S6_L001_R2_001.fastq.gz"],

    ["581_cat_R1.fastq.gz",
     "581_cat_R2.fastq.gz"],

    ["751_S8_L001_R1_001.fastq.gz",
     "751_S8_L001_R2_001.fastq.gz"],

    ["894_S9_L001_R1_001.fastq.gz",
     "894_S9_L001_R2_001.fastq.gz"],

    ["964_S10_L001_R1_001.fastq.gz",
     "964_S10_L001_R2_001.fastq.gz"],

    ["1507_cat_R1.fastq.gz",
     "1507_cat_R2.fastq.gz"],

    ["1689_cat_R1.fastq.gz",
     "1689_cat_R2.fastq.gz"],

    ["1728_cat_R1.fastq.gz",
     "1728_cat_R2.fastq.gz"],

    ["1866_cat_R1.fastq.gz",
     "1866_cat_R2.fastq.gz"],

    ["1869_cat_R1.fastq.gz",
     "1869_cat_R2.fastq.gz"],

    ["2065_cat_R1.fastq.gz",
     "2065_cat_R2.fastq.gz"],

    ["2078_S14_L001_R1_001.fastq.gz",
     "2078_S14_L001_R2_001.fastq.gz"],

    ["2136_cat_R1.fastq.gz",
     "2136_cat_R2.fastq.gz"],

    ["2235_cat_R1.fastq.gz",
     "2235_cat_R2.fastq.gz"],

    ["2330_S17_L001_R1_001.fastq.gz",
     "2330_S17_L001_R2_001.fastq.gz"],

    ["2368_cat_R1.fastq.gz",
     "2368_cat_R2.fastq.gz"],

    ["2422_cat_R1.fastq.gz",
     "2422_cat_R2.fastq.gz"],

    ["2440_S20_L001_R1_001.fastq.gz",
     "2440_S20_L001_R2_001.fastq.gz"],

    ["2449_cat_R1.fastq.gz",
     "2449_cat_R2.fastq.gz"],

    ["2683_cat_R1.fastq.gz",
     "2683_cat_R2.fastq.gz"],

    ["2721_cat_R1.fastq.gz",
     "2721_cat_R2.fastq.gz"],

    ["2852_S25_L001_R1_001.fastq.gz",
     "2852_S25_L001_R2_001.fastq.gz"],

    ["3026_S26_L001_R1_001.fastq.gz",
     "3026_S26_L001_R2_001.fastq.gz"],

    ["3033_cat_R1.fastq.gz",
     "3033_cat_R2.fastq.gz"],

    ["3141_cat_R1.fastq.gz",
     "3141_cat_R2.fastq.gz"],

    ["3185_cat_R1.fastq.gz",
     "3185_cat_R2.fastq.gz"],

    ["3376_cat_R1.fastq.gz",
     "3376_cat_R2.fastq.gz"]

    ]


# java -jar /opt/Trimmomatic-0.36.jar PE -phred33

# 118_cat_R1.fastq.gz
# 118_cat_R2.fastq.gz
# 118_cat_R1.p.fastq.gz
# 118_cat_R1.s.fastq.gz
# 118_cat_R2.p.fastq.gz
# 118_cat_R2.s.fastq.gz

# ILLUMINACLIP:NexteraPE-PE.fa:2:30:10 LEADING:15 TRAILING:15 HEADCROP:7 SLIDINGWINDOW:4:15 MINLEN:36

file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"


def run_trimmomatic(a_pair):

    genome_1 = file_location_inside_virtualbox + a_pair[0]
#    print(genome_1)
    genome_1_s =  file_location_inside_virtualbox + "".join(a_pair[0].split(".")[:-2]) + ".s.fastq.gz"
#    print(genome_1_s)
    genome_1_p = file_location_inside_virtualbox + "".join(a_pair[0].split(".")[:-2]) + ".p.fastq.gz"
#    print(genome_1_p)

    genome_2 = file_location_inside_virtualbox + a_pair[1]
#    print(genome_2)
    genome_2_s = file_location_inside_virtualbox +  "".join(a_pair[1].split(".")[:-2]) + ".s.fastq.gz"
#    print(genome_2_s)
    genome_2_p = file_location_inside_virtualbox +  "".join(a_pair[1].split(".")[:-2]) + ".p.fastq.gz"
#    print(genome_2_p)


# java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33
# 118_cat_R1.fastq.gz
# 118_cat_R2.fastq.gz
# 118_cat_R1.p.fastq.gz
# 118_cat_R1.s.fastq.gz
# 118_cat_R2.p.fastq.gz
# 118_cat_R2.s.fastq.gz
# LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36


    trimmomatic_location_and_params = "vagrant ssh -c \"java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33"

    illumina_string = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36\""

    cmd = trimmomatic_location_and_params + " " + \
          genome_1 + " " + \
          genome_2 + " " + \
          genome_1_p + " " + \
          genome_1_s + " " + \
          genome_2_p + " " + \
          genome_2_s + " " + \
          illumina_string

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_pair in genome_pairs:
    run_trimmomatic(a_pair)
