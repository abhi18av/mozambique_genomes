# Mozambique genomes


# trimmomatic

- To run this, we need to add https://github.com/timflutre/trimmomatic/blob/master/adapters/NexteraPE-PE.fa to the folder as well

- 

```
java -jar /opt/Trimmomatic-0.36/trimmomatic-0.36.jar PE -phred33 118_cat_R1.fastq.gz 118_cat_R2.fastq.gz 118_cat_R1.p.fastq.gz 118_cat_R1s.fastq.gz 118_cat_R2.p.fastq.gz 118_cat_R2s.fastq.gz ILLUMINACLIP:NexteraPE-PE.fa:2:30:10 LEADING:15 TRAILING:15 HEADCROP:7 SLIDINGWINDOW:4:15 MINLEN:36 


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

# unziping pared files
```
gunzip *.p.fastq.gz
```
# map_and_generate_sam_file
```
bwa mem -R "@RG\tID:PT000033\tSM:PT000033\tSM:xxx\tSM:Illumina" -M NC000962_3.fasta PT000033_1_trimmed_paired.fastq PT000033_2_trimmed_paired.fastq > PT000033.sam 

bwa mem -R "@RG\tID:118\tSM:118\tSM:Illumina" -M NC000962_3.fasta 118_R1.p.fastq 118_R2.p.fastq > 118.sam

bwa mem -R "@RG\tID:141\tSM:141\tSM:141\tSM:Illumina" -M NC000962_3.fasta 141_R1.p.fastq 141_R2.p.fastq > 141.sam && bwa mem -R "@RG\tID:205\tSM:205\tSM:205\tSM:Illumina" -M NC000962_3.fasta 205_R1.p.fastq 205_R2.p.fastq > 205.sam

bwa mem -R "@RG\tID:208\tSM:208\tSM:208\tSM:Illumina" -M NC000962_3.fasta 208_R1.p.fastq 208_R2.p.fastq > 208.sam

bwa mem -R "@RG\tID:227\tSM:227\tSM:xxx\tSM:Illumina" -M NC000962_3.fasta 227_R1.p.fastq 227_R2.p.fastq > 227.sam

bwa mem -R "@RG\tID:243\tSM:243\tSM:243\tSM:Illumina" -M NC000962_3.fasta 243_R1.p.fastq 243_R2.p.fastq > 243.sam

bwa mem -R "@RG\tID:316\tSM:316\tSM:316\tSM:Illumina" -M NC000962_3.fasta 316_R1.p.fastq 316_R2.p.fastq > 316.sam

bwa mem -R "@RG\tID:370\tSM:370\tSM:370\tSM:Illumina" -M NC000962_3.fasta 370_R1.p.fastq 370_R2.p.fastq > 370.sam && bwa mem -R "@RG\tID:509\tSM:509\tSM:509\tSM:Illumina" -M NC000962_3.fasta 509_R1.p.fastq 509_R2.p.fastq > 509.sam && bwa mem -R "@RG\tID:581\tSM:581\tSM:581\tSM:Illumina" -M NC000962_3.fasta 581_R1.p.fastq 581_R2.p.fastq > 581.sam && bwa mem -R "@RG\tID:751\tSM:751\tSM:751\tSM:Illumina" -M

NC000962_3.fasta 751_R1.p.fastq 751_R2.p.fastq > 751.sam && bwa mem -R "@RG\tID:894\tSM:894\tSM:894\tSM:Illumina" -M NC000962_3.fasta 894_R1.p.fastq 894_R2.p.fastq > 894.sam && bwa mem -R "@RG\tID:964\tSM:964\tSM:964\tSM:Illumina" -M NC000962_3.fasta 964_R1.p.fastq 964_R2.p.fastq > 964.sam && bwa mem -R "@RG\tID:1507\tSM:1507\tSM:1507\tSM:Illumina" -M NC000962_3.fasta 1507_R1.p.fastq 1507_R2.p.fastq > 1507.sam && bwa mem -R "@RG\tID:1689\tSM:1689\tSM:1689\tSM:Illumina" -M NC000962_3.fasta 1689_R1.p.fastq 1689_R2.p.fastq > 1689.sam && bwa mem -R "@RG\tID:1728\tSM:1728\tSM:xxx\tSM:Illumina" -M NC000962_3.fasta 1728_R1.p.fastq 1728_R2.p.fastq > 1728.sam

bwa mem -R "@RG\tID:1866\tSM:1866\tSM:1866\tSM:Illumina" -M NC000962_3.fasta 1866_R1.p.fastq 1866_R2.p.fastq > 1866.sam

bwa mem -R "@RG\tID:1869\tSM:1869\tSM:1869\tSM:Illumina" -M NC000962_3.fasta 1869_R1.p.fastq 1869_R2.p.fastq > 1869.sam

bwa mem -R "@RG\tID:2065\tSM:2065\tSM:2065\tSM:Illumina" -M NC000962_3.fasta 2065_R1.p.fastq 2065_R2.p.fastq > 2065.sam

bwa mem -R "@RG\tID:2078\tSM:2078\tSM:2078\tSM:Illumina" -M NC000962_3.fasta 2078_R1.p.fastq 2078_R2.p.fastq > 2078.sam && bwa mem -R "@RG\tID:2136\tSM:2136\tSM:2136\tSM:Illumina" -M NC000962_3.fasta 2136_R1.p.fastq 2136_R2.p.fastq > 2136.sam && bwa mem -R "@RG\tID:2235\tSM:2235\tSM:2235\tSM:Illumina" -M NC000962_3.fasta 2235_R1.p.fastq 2235_R2.p.fastq > 2235.sam && bwa mem -R "@RG\tID:2330\tSM:2330\tSM:2330\tSM:Illumina" -M NC000962_3.fasta 2330_R1.p.fastq 2330_R2.p.fastq > 2330.sam && bwa mem -R "@RG\tID:2368\tSM:2368\tSM:2368\tSM:Illumina" -M NC000962_3.fasta 2368_R1.p.fastq 2368_R2.p.fastq > 2368.sam && bwa mem -R "@RG\tID:2422\tSM:2422\tSM:2422\tSM:Illumina" -M NC000962_3.fasta 2422_R1.p.fastq 2422_R2.p.fastq > 2422.sam && bwa mem -R "@RG\tID:2440\tSM:2440\tSM:2440\tSM:Illumina" -M NC000962_3.fasta 2440_R1.p.fastq 2440_R2.p.fastq > 2440.sam && bwa mem -R "@RG\tID:2449\tSM:2449\tSM:2449\tSM:Illumina" -M NC000962_3.fasta 2449_R1.p.fastq 2449_R2.p.fastq > 2449.sam && bwa mem -R "@RG\tID:2683\tSM:2683\tSM:2683\tSM:Illumina" -M NC000962_3.fasta 2683_R1.p.fastq 2683_R2.p.fastq > 2683.sam && bwa mem -R "@RG\tID:2721\tSM:2721\tSM:2721\tSM:Illumina" -M NC000962_3.fasta 2721_R1.p.fastq 2721_R2.p.fastq > 2721.sam && bwa mem -R "@RG\tID:2852\tSM:2852\tSM:2852\tSM:Illumina" -M NC000962_3.fasta 2852_R1.p.fastq 2852_R2.p.fastq > 2852.sam && bwa mem -R "@RG\tID:3033\tSM:3033\tSM:3033\tSM:Illumina" -M NC000962_3.fasta 3033_R1.p.fastq 3033_R2.p.fastq > 3033.sam && bwa mem -R "@RG\tID:3141\tSM:3141\tSM:3141\tSM:Illumina" -M NC000962_3.fasta 3141_R1.p.fastq 3141_R2.p.fastq > 3141.sam && bwa mem -R "@RG\tID:3185\tSM:3185\tSM:3185\tSM:Illumina" -M NC000962_3.fasta 3185_R1.p.fastq 3185_R2.p.fastq > 3185.sam && bwa mem -R "@RG\tID:3376\tSM:3376\tSM:3376\tSM:Illumina" -M NC000962_3.fasta 3376_R1.p.fastq 3376_R2.p.fastq > 3376.sam


bwa mem -R "@RG\tID:G00118\tSM:G00118\tSM:xxx\tSM:Illumina" -M NC000962_3.fasta G00118_R1.p.fastq G00118_R2.p.fastq > G00118.sam 

```

 


