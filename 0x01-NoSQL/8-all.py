#!/usr/bin/env python3
"""8-all module"""

def list_all(mongo_collection):
    return [docs for docs in mongo_collection.find()]
