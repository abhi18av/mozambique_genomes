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



def run_snippy(a_pair):

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

# snippy --cpus 4 --outdir G04868 --ref ./NC000962_3.gbk --R1 ./G04868_1.fastq.gz --R2 ./G04868_2.fastq.gz


    genome_name = file_location_inside_virtualbox + a_pair[0].split("_")[0]

    genome_1 = file_location_inside_virtualbox + a_pair[0]
    
    genome_2 = file_location_inside_virtualbox + a_pair[1]



    snippy_initial_command = "vagrant ssh -c \"snippy --cpus 4 --outdir "


    cmd = snippy_initial_command + \
            genome_name + \
            " --ref " + \
            file_location_inside_virtualbox + "NC000962_3.gbk" + \
            " --R1 " + \
            genome_1 + \
            " --R2 " + \
            genome_2 + \
            "\""


    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for a_pair in genome_pairs:
    run_snippy(a_pair)

