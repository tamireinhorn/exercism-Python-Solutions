def round_scores(student_scores):
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """
    total = 0
    for score in student_scores:
        if score <= 40:
            total += 1
    return total


def above_threshold(student_scores, threshold):
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """
    total = []
    for score in student_scores:
        if score >= threshold:
            total.append(score)
    return total


def letter_grades(highest):
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.
    """
    interval_size = (highest - 40 ) // 4
    intervals = [41]
    for i in range(1,4):
        intervals.append(intervals[0] +  i * interval_size)
    return intervals


def student_ranking(student_scores, student_names):
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """
    ranking = [str(index+1) + '. ' + student_names[index] + ': ' + str(element)  for index, element in enumerate(student_scores)]
    return ranking


def perfect_score(student_info):
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."
    """
    for pair in student_info:
        if pair[1] == 100:
            return pair
    return []
