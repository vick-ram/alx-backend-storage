#!/usr/bin/env python3
"""10-update_topics module"""


def update_topics(mongo_collection, name, topics):
    mongo_collection.update_one(
        {'name': name},
        {'$set': {'topics': topics}}
    )
