# Mozambique genomes

# I must make sure that I execute all the commands as a `centos` user 

# trimmomatic

- To run this, we need to add https://github.com/timflutre/trimmomatic/blob/master/adapters/NexteraPE-PE.fa to the folder as well

- 

```
java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33 118_cat_R1.fastq.gz 118_cat_R2.fastq.gz 118_cat_R1.p.fastq.gz 118_cat_R1.s.fastq.gz 118_cat_R2.p.fastq.gz 118_cat_R2.s.fastq.gz ILLUMINACLIP:NexteraPE-PE.fa:2:30:10 LEADING:15 TRAILING:15 HEADCROP:7 SLIDINGWINDOW:4:15 MINLEN:36 


```


```python
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


```

# bwa_index_reference_genome

```
bwa index NC000962_3.fasta
```

- output 

```sh
root@vaani /biodragon/vagrantBox/mozambique_genomes/lab master # vagrant ssh
Last login: Sat Apr  6 16:28:35 2019 from gateway
[root@localhost ~]# cd /vagrant/mozambique_genomes/lab/
[root@localhost lab]# bwa index NC000962_3.fasta
[bwa_index] Pack FASTA... 3.80 sec
[bwa_index] Construct BWT for the packed sequence...
[bwa_index] 10.19 seconds elapse.
[bwa_index] Update BWT... 3.99 sec
[bwa_index] Pack forward-only FASTA... 2.74 sec
[bwa_index] Construct SA from BWT and Occ... 5.58 sec
[main] Version: 0.7.12-r1039
[main] CMD: bwa index NC000962_3.fasta
[main] Real time: 74.667 sec; CPU: 26.326 sec


```

# unziping paired files

- Unzip all the paired files

```
gunzip *.p.fastq.gz
```
# map_and_generate_sam_file


```
bwa mem -R "@RG\tID:PT000033\tSM:PT000033\tSM:xxx\tSM:Illumina" -M NC000962_3.fasta PT000033_1_trimmed_paired.fastq PT000033_2_trimmed_paired.fastq > PT000033.sam 

```

```
bwa mem -R "@RG ID:118  SM:118  SM:Illumina" -M NC000962_3.fasta 118_R1.p.fastq 118_R2.p.fastq > 118.sam
```


```python

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


```

# samtools_faidx_reference_genome <<<<<

```
samtools faidx NC000962_3.fasta
 ```
                             

```python



```





# convert_sam_file_to_bam_file <<<<<

```
samtools view -bt NC000962_3.fasta.fai G04868.sam > G04868.bam
```

```python
# TODO convert_sam_file_to_bam_file <<<<<
# samtools view -bt NC000962_3.fasta.fai G04868.sam > G04868.bam

import os
import subprocess
import shutil



def has_sam_in_name(string):
    if (string.split(".")[-1] != "sam"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_sam_files = list(filter(lambda x:has_sam_in_name(x), all_files))
all_sam_files.remove('PT000033.sam')




def convert_sam_file_to_bam_file(a_sam_file):



# samtools view -bt NC000962_3.fasta.fai \
# G04868.sam \
# > G04868.bam

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    sam_file_name = file_location_inside_virtualbox +  a_sam_file.split(".")[0]
    bam_file_name = sam_file_name + ".bam"

    samtools_view_initial_command = "vagrant ssh -c \"samtools view -bt "
    reference_file = file_location_inside_virtualbox + "NC000962.fasta.fai "


    cmd = samtools_view_initial_command +  \
          reference_file + \
          file_location_inside_virtualbox + \
          a_sam_file + \
          " > " + \
          bam_file_name + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_sam_files:
    convert_sam_file_to_bam_file(f)



```

# samtools_index_sorted_bam 

```python
# TODO sort_bam_file <<<<<
# samtools sort G04868.bam -o G04868.sorted.bam

import os
import subprocess
import shutil



def has_bam_in_name(string):
    if (string.split(".")[-1] != "bam"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_bam_files = list(filter(lambda x:has_bam_in_name(x), all_files))




def sort_bam_files(a_bam_file):




# samtools sort G04868.bam -o G04868.sorted.bam


    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    bam_file_name = file_location_inside_virtualbox + a_bam_file.split(".")[0]
    sorted_bam_file_name = bam_file_name + ".sorted.bam"

    samtools_view_initial_command = "vagrant ssh -c \"samtools sort "


    cmd = samtools_view_initial_command +  \
          file_location_inside_virtualbox + \
          a_bam_file + \
          " -o " + \
          sorted_bam_file_name + "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_bam_files:
    sort_bam_files(f)


```


# samtools_index_sorted_bam <<<<<

```
samtools index G04868.sorted.bam
```

```python
# TODO samtools_index_sorted_bam <<<<<
# samtools index G04868.sorted.bam


import os
import subprocess
import shutil



def has_sorted_in_name(string):
    if (string.split(".")[-2] != "sorted"):
        #print("NO")
        return 0
    else:
        #print("YES")
        return 1



all_files = list(filter(lambda x: os.path.isfile(x), os.listdir()))

all_sorted_bam_files = list(filter(lambda x:has_sorted_in_name(x), all_files))




def index_sorted_bam_files(a_sorted_bam_file):




# samtools index G04868.sorted.bam

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"

    samtools_view_initial_command = "vagrant ssh -c \"samtools index "


    cmd = samtools_view_initial_command +  \
          file_location_inside_virtualbox + \
          a_sorted_bam_file + \
          "\""

    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



for f in all_sorted_bam_files:
    index_sorted_bam_files(f)



```


# snippy_command <<<<<

```
snippy --cpus 4 --outdir G04868 --ref ./NC000962_3.gbk --R1 ./G04868_1.fastq.gz --R2 ./G04868_2.fastq.gz
```


```python

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




```

# unzip all gzipped genomes to a different folder


```python
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

   zipped_genome =  "/vagrant/mozambique_genomes/lab/" + a_genome

   unzipped_genome = "/vagrant/mozambique_genomes/lab/" + "spotyping/" + a_genome.split(".")[0] + ".fastq" 

   cmd = "vagrant ssh -c \"" + \
           "gzip -dc " + \
           zipped_genome + \
           " > " + \
           unzipped_genome + \
           "\""

   print(cmd)


```

# SpoTyping 

https://github.com/xiaeryu/SpoTyping-v2.0/tree/master/SpoTyping-v2.0-commandLine

from inside the virtualbox 

```
python2.7 SpoTyping.py ./118_cat_R1.fastq ./118_cat_R2.fastq
```

```python
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



```

# snippy_core 

```
snippy-core PT000033 PT000049 PT000050 PT000271 PT000279

```

```python
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


all_dirs =  [f for f in os.listdir() if os.path.isdir(f)]
all_dirs.remove('spotyping')
all_dirs.remove('uploaded')


dir_string = " "
for a_dir in all_dirs:
    dir_string =  dir_string + " " + a_dir



def run_snippy_core():

    file_location_inside_virtualbox = "/vagrant/mozambique_genomes/lab/"



    cmd = "vagrant ssh -c \"cd /vagrant/mozambique_genomes/lab/ && " + \
          "snippy-core " + \
          dir_string + \
          "\""


    print(cmd)

    os.system(cmd)

    print("\n $$$$$$$$$$ \n")



run_snippy_core()


```

# tabix 

```

tabix -p vcf G04868.filt.vcf.gz

```

NOTE: Tabix completed but gives an error every time - still there is a `*tbi` file for every genome
```
[E::get_intv] failed to parse TBX_VCF, was wrong -p [type] used?
The offending line was: "bash: vcfutils.pl: command not found"
bash: line 1:  4689 Segmentation fault      (core dumped) tabix -p vcf 581.filt.vcf.gz
```

# TODO need to fine tune the path of root for important tools

From the virtualbox image `centos` user 

```
/opt/Rexe:/opt/velvet-stats:/opt/Bandage:/opt/velvet/contrib/VelvetOptimiser-2.2.4:/opt/snippy/bin:/opt/snippy/binaries/linux/:/opt/snippy/binaries/noarch:/opt/bcftools/misc:/opt/Trimmomatic-0.36:/opt/artemis:/opt/bcftools:/opt/bwa:/opt/htslib:/opt/GenomeAnalysisTK-3.8-0-ge9d806836:/opt/samtools:/opt/Trimmomatic-0.36:/opt/FastQC:/opt/seaview:/opt/jmodeltest2-2.1.9r20160115/dist:/opt/velvet:/opt/SPAdes-3.10.1-Linux/bin:/opt/prokka/bin:/opt/prokka/binaries/common:/opt/prokka/binaries/linux:/opt/PAGIT/bin/:/opt/PAGIT/bin/pileup_v0.5/:/opt/PAGIT/bin/pileup_v0.5/ssaha2:/opt/PAGIT/bin/pileup_v0.5/:/opt/PAGIT/IMAGE/:/opt/PAGIT/ABACAS:/opt/PAGIT/ICORN/:/opt/PAGIT/RATT/:/opt/Rexe:/opt/velvet-stats:/opt/Bandage:/opt/velvet/contrib/VelvetOptimiser-2.2.4:/opt/snippy/bin:/opt/snippy/binaries/linux/:/opt/snippy/binaries/noarch:/opt/bcftools/misc:/opt/Trimmomatic-0.36:/opt/artemis:/opt/bcftools:/opt/bwa:/opt/htslib:/opt/GenomeAnalysisTK-3.8-0-ge9d806836:/opt/samtools:/opt/Trimmomatic-0.36:/opt/FastQC:/opt/seaview:/opt/jmodeltest2-2.1.9r20160115/dist:/opt/velvet:/opt/SPAdes-3.10.1-Linux/bin:/opt/prokka/bin:/opt/prokka/binaries/common:/opt/prokka/binaries/linux:/opt/PAGIT/bin/:/opt/PAGIT/bin/pileup_v0.5/:/opt/PAGIT/bin/pileup_v0.5/ssaha2:/opt/PAGIT/bin/pileup_v0.5/:/opt/PAGIT/IMAGE/:/opt/PAGIT/ABACAS:/opt/PAGIT/ICORN/:/opt/PAGIT/RATT/:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/home/centos/.local/bin:/home/centos/bin

```

# adding M.Canettii genomes

```


rclone copy onedrive-abhi:mozambique-genomes/lab/m_canetti/Mcanettii_R1.fastq.gz . -vv
rclone copy onedrive-abhi:mozambique-genomes/lab/m_canetti/Mcanettii_R2.fastq.gz . -vv
rclone copy onedrive-abhi:mozambique-genomes/lab/m_canetti/NC002945_4.gb . -vv
rclone copy onedrive-abhi:mozambique-genomes/lab/m_canetti/NC015848.fasta . -vv

```