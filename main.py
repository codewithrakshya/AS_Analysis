from alignment import read_bam_file, close_bam_file
from splicing import analyze_cigar_strings, get_splicing_pattern_frequencies
from visualization import plot_splicing_patterns
from statistics import calculate_std_deviation
from output import write_output_to_file

def main():
    # Read the BAM file
    bamfile = read_bam_file("/content/test.bam")

    # Analyze CIGAR strings and get splicing patterns
    splicing_patterns = analyze_cigar_strings(bamfile, max_reads=90)

    # Calculate splicing pattern frequencies
    splicing_pattern_frequencies = get_splicing_pattern_frequencies(splicing_patterns)

    # Perform statistical analysis
    std_deviation = calculate_std_deviation(splicing_pattern_frequencies)

    # Visualize splicing patterns
    plot_splicing_patterns(splicing_pattern_frequencies)

    # Close the BAM file
    close_bam_file(bamfile)

    # Write the output to a file
    write_output_to_file(splicing_pattern_frequencies, "/path/to/output.tsv")

if __name__ == "__main__":
    main()
