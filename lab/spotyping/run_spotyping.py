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


    ["118_cat_R1.fastq",
     "118_cat_R2.fastq"],

    ["141_cat_R1.fastq",
     "141_cat_R2.fastq"],

    ["205_cat_R1.fastq",
     "205_cat_R2.fastq"],

    ["208_cat_R1.fastq",
     "208_cat_R2.fastq"],

    ["227_S3_L001_R1_001.fastq",
     "227_S3_L001_R2_001.fastq"],

    ["243_S5_L001_R1_001.fastq",
     "243_S5_L001_R2_001.fastq"],

    ["316_S5_L001_R1_001.fastq",
     "316_S5_L001_R2_001.fastq"],

    ["370_cat_R1.fastq",
     "370_cat_R2.fastq"],

    ["509_S6_L001_R1_001.fastq",
     "509_S6_L001_R2_001.fastq"],

    ["581_cat_R1.fastq",
     "581_cat_R2.fastq"],

    ["751_S8_L001_R1_001.fastq",
     "751_S8_L001_R2_001.fastq"],

    ["894_S9_L001_R1_001.fastq",
     "894_S9_L001_R2_001.fastq"],

    ["964_S10_L001_R1_001.fastq",
     "964_S10_L001_R2_001.fastq"],

    ["1507_cat_R1.fastq",
     "1507_cat_R2.fastq"],

    ["1689_cat_R1.fastq",
     "1689_cat_R2.fastq"],

    ["1728_cat_R1.fastq",
     "1728_cat_R2.fastq"],

    ["1866_cat_R1.fastq",
     "1866_cat_R2.fastq"],

    ["1869_cat_R1.fastq",
     "1869_cat_R2.fastq"],

    ["2065_cat_R1.fastq",
     "2065_cat_R2.fastq"],

    ["2078_S14_L001_R1_001.fastq",
     "2078_S14_L001_R2_001.fastq"],

    ["2136_cat_R1.fastq",
     "2136_cat_R2.fastq"],

    ["2235_cat_R1.fastq",
     "2235_cat_R2.fastq"],

    ["2330_S17_L001_R1_001.fastq",
     "2330_S17_L001_R2_001.fastq"],

    ["2368_cat_R1.fastq",
     "2368_cat_R2.fastq"],

    ["2422_cat_R1.fastq",
     "2422_cat_R2.fastq"],

    ["2440_S20_L001_R1_001.fastq",
     "2440_S20_L001_R2_001.fastq"],

    ["2449_cat_R1.fastq",
     "2449_cat_R2.fastq"],

    ["2683_cat_R1.fastq",
     "2683_cat_R2.fastq"],

    ["2721_cat_R1.fastq",
     "2721_cat_R2.fastq"],

    ["2852_S25_L001_R1_001.fastq",
     "2852_S25_L001_R2_001.fastq"],

    ["3026_S26_L001_R1_001.fastq",
     "3026_S26_L001_R2_001.fastq"],

    ["3033_cat_R1.fastq",
     "3033_cat_R2.fastq"],

    ["3141_cat_R1.fastq",
     "3141_cat_R2.fastq"],

    ["3185_cat_R1.fastq",
     "3185_cat_R2.fastq"],

    ["3376_cat_R1.fastq",
     "3376_cat_R2.fastq"]

    ]




def run_spotyping(a_pair):

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/spotyping/"


    genome_1 = file_location_inside_virtualbox + a_pair[0]

    genome_2 = file_location_inside_virtualbox + a_pair[1]

# python2.7 SpoTyping.py ./118_cat_R1.fastq ./118_cat_R2.fastq

    cmd =  "vagrant ssh -c \" " + \
            "python2.7 SpoTyping.py " + \
            genome_1 + \
            " " + \
            genome_2 + \
            "\""


    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_pair in genome_pairs:
    run_spotyping(a_pair)

