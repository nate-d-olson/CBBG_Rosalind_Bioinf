from collections import defaultdict


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


def parse_fasta(filename):
    """ parsing fasta file

    reads a fasta input file and returns a dict with
    with seq name as key and seq as value

    Args:
        filename: name of file with input data

    Returns:
        dict with seq name as key and seq as value

    Raises:
        IOError: An error occurred accessing the file.
    """

    dat = readdat(filename)

    seq_dict = defaultdict(str)
    for line in dat:
        if line.startswith('>'):
            name = line[1:]
        else:
            seq_dict[name] += line

    return seq_dict
