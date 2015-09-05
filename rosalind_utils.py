def readdat(filename):
    """ Reading input file

    Reads lines in file and returns a list

    Args:
        filename: name of file with input data

    Returns:
        List of lines in the input file as strings

    Raises:
        IOError: An error occurred accessing the file.
    """

    try:
        open(filename, 'r')
    except:
        # TODO add error message
        raise

    with open(filename, 'r') as f:
        dat = map(str.strip, f.readlines())
    return dat


def parse_fasta(dat):
    pass
