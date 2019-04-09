import os


# TODO first we unzip the gzipped genomes to this folder


all_genomes  = [


    "118_cat_R1.fastq.gz",
     "118_cat_R2.fastq.gz",

    "141_cat_R1.fastq.gz",
     "141_cat_R2.fastq.gz",

    "205_cat_R1.fastq.gz",
     "205_cat_R2.fastq.gz",

    "208_cat_R1.fastq.gz",
     "208_cat_R2.fastq.gz",

    "227_S3_L001_R1_001.fastq.gz",
     "227_S3_L001_R2_001.fastq.gz",

    "243_S5_L001_R1_001.fastq.gz",
     "243_S5_L001_R2_001.fastq.gz",

    "316_S5_L001_R1_001.fastq.gz",
     "316_S5_L001_R2_001.fastq.gz",

    "370_cat_R1.fastq.gz",
     "370_cat_R2.fastq.gz",

    "509_S6_L001_R1_001.fastq.gz",
     "509_S6_L001_R2_001.fastq.gz",

    "581_cat_R1.fastq.gz",
     "581_cat_R2.fastq.gz",

    "751_S8_L001_R1_001.fastq.gz",
     "751_S8_L001_R2_001.fastq.gz",

    "894_S9_L001_R1_001.fastq.gz",
     "894_S9_L001_R2_001.fastq.gz",

    "964_S10_L001_R1_001.fastq.gz",
     "964_S10_L001_R2_001.fastq.gz",

    "1507_cat_R1.fastq.gz",
     "1507_cat_R2.fastq.gz",

    "1689_cat_R1.fastq.gz",
     "1689_cat_R2.fastq.gz",

    "1728_cat_R1.fastq.gz",
     "1728_cat_R2.fastq.gz",

    "1866_cat_R1.fastq.gz",
     "1866_cat_R2.fastq.gz",

    "1869_cat_R1.fastq.gz",
     "1869_cat_R2.fastq.gz",

    "2065_cat_R1.fastq.gz",
     "2065_cat_R2.fastq.gz",

    "2078_S14_L001_R1_001.fastq.gz",
     "2078_S14_L001_R2_001.fastq.gz",

    "2136_cat_R1.fastq.gz",
     "2136_cat_R2.fastq.gz",

    "2235_cat_R1.fastq.gz",
     "2235_cat_R2.fastq.gz",

    "2330_S17_L001_R1_001.fastq.gz",
     "2330_S17_L001_R2_001.fastq.gz",

    "2368_cat_R1.fastq.gz",
     "2368_cat_R2.fastq.gz",

    "2422_cat_R1.fastq.gz",
     "2422_cat_R2.fastq.gz",

    "2440_S20_L001_R1_001.fastq.gz",
     "2440_S20_L001_R2_001.fastq.gz",

    "2449_cat_R1.fastq.gz",
     "2449_cat_R2.fastq.gz",

    "2683_cat_R1.fastq.gz",
     "2683_cat_R2.fastq.gz",

    "2721_cat_R1.fastq.gz",
     "2721_cat_R2.fastq.gz",

    "2852_S25_L001_R1_001.fastq.gz",
     "2852_S25_L001_R2_001.fastq.gz",

    "3026_S26_L001_R1_001.fastq.gz",
     "3026_S26_L001_R2_001.fastq.gz",

    "3033_cat_R1.fastq.gz",
     "3033_cat_R2.fastq.gz",

    "3141_cat_R1.fastq.gz",
     "3141_cat_R2.fastq.gz",

    "3185_cat_R1.fastq.gz",
     "3185_cat_R2.fastq.gz",

    "3376_cat_R1.fastq.gz",
     "3376_cat_R2.fastq.gz"

    ]

  

for a_genome in all_genomes:

   zipped_genome =  "../" + a_genome

   unzipped_genome =  "./" + a_genome.split(".")[0] + ".fastq" 

   cmd =   "gzip -dc " + \
           zipped_genome + \
           " > " + \
           unzipped_genome 

   print(cmd)
   os.system(cmd)
