#!/usr/bin/env python3
"""11-schools_by_topic"""


def schools_by_topic(mongo_collection, topic):
    """Script that returns the list of school having a specific topic"""
    result = mongo_collection.find({'topic': topic})
    return result
