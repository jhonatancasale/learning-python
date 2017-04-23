def to_rna(strand):
    """
    Given a DNA strand, its transcribed RNA strand is formed by replacing
    each nucleotide with its complement:

    * `G` -> `C`
    * `C` -> `G`
    * `T` -> `A`
    * `A` -> `U`
    """


    complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A':'U'}

    transcribed_rna = ''.join([complement.get(nucleotide, '') for nucleotide in strand])
    return transcribed_rna if len(strand) == len(transcribed_rna) else ''
