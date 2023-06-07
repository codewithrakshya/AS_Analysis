import pysam

def read_bam_file(bam_file_path):
    bamfile = pysam.AlignmentFile(bam_file_path, "rb")
    return bamfile

def close_bam_file(bamfile):
    bamfile.close()
