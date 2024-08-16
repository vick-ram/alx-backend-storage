#!/usr/bin/env python3
"""101-students module"""


def top_students(mongo_collection):
    """Returns all students sorted by their average score"""
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
