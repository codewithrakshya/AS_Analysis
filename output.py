import pandas as pd

def write_output_to_file(splicing_pattern_frequencies, output_file_path):
    df = pd.DataFrame.from_dict(splicing_pattern_frequencies, orient='index', columns=['Frequency'])
    df.index.name = 'Splicing Pattern'
    df.to_csv(output_file_path, sep='\t')
