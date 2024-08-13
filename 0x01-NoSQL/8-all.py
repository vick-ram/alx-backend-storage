#!/usr/bin/env python3
"""8-all module"""

def list_all(mongo_collection):
    """Lists all documents in a collection"""
    return [docs for docs in mongo_collection.find()]
