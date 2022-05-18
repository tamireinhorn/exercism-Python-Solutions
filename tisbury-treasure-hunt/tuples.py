def get_coordinate(record):
    """

    :param record: tuple - a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """

    :param coordinate: str - a string map coordinate
    :return:  tuple - the string coordinate seperated into its individual components.
    """

    return (coordinate[0], coordinate[1])
 

def compare_records(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: bool - True if coordinates match, False otherwise.
    """

    return azara_record[1] == rui_record[1][0] + rui_record[1][1]


def create_record(azara_record, rui_record):
    """

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return:  tuple - combined record, or "not a match" if the records are incompatible.
    """
    answer = "not a match"
    if compare_records(azara_record, rui_record):
        answer = (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
    return answer


def clean_up(combined_record_group):
    """

    :param combined_record_group: tuple of tuples - everything from both participants.
    :return: string of tuples separated by newlines - everything "cleaned". Excess coordinates and information removed.
    """
    report = []
    for index, information in enumerate(combined_record_group):
        tupla = (information[0], information[2], information[3], information[4])
        
        report.append(str(tupla) + "\n")
     
    
    report = ''.join(report)

    return report
    
