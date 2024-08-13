#!/usr/bin/env python3
"""101-students module"""


def top_students(mongo_collection):
    """Returns all students sorted by their average score"""
    students = mongo_collection.find()
    result = []
    for student in students:
        scores = [topic['score'] for topic in student.get('topics', [])]
        average_score = sum(scores) / len(scores) if scores else 0
        student['averageScore'] = average_score
        result.append(student)
        result.sort(key=lambda x: x['averageScore'], reverse=True)

        return result
