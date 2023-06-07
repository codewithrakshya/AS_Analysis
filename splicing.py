def analyze_cigar_strings(bamfile, max_reads=100):
    splicing_patterns = {}
    for i, read in enumerate(bamfile):
        if read.is_unmapped:
            continue

        cigar = read.cigarstring
        if not cigar or "N" not in cigar:
            continue

        splicing_pattern = ""
        for op, length in read.cigartuples:
            if op == 0 or op == 2:
                splicing_pattern += length * "M"
            elif op == 3:
                splicing_pattern += length * "N"

        if splicing_pattern in splicing_patterns:
            splicing_patterns[splicing_pattern] += 1
        else:
            splicing_patterns[splicing_pattern] = 1

        if i >= max_reads:
            break

    return splicing_patterns

def get_splicing_pattern_frequencies(splicing_patterns):
    total_reads = sum(splicing_patterns.values())
    splicing_pattern_frequencies = {}
    for splicing_pattern in splicing_patterns:
        frequency = splicing_patterns[splicing_pattern] / total_reads
        splicing_pattern_frequencies[splicing_pattern] = frequency

    return splicing_pattern_frequencies
