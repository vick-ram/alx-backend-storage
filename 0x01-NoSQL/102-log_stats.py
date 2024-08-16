#!/usr/bin/env python3
from pymongo import MongoClient


def log_stats():
    """Connect to the MongoDB server"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    """Connect to the 'logs' database and 'nginx' collection"""
    nginx_collection = client.logs.nginx

    """Count total number of logs"""
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    """Define the list of methods to check"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    """Count number of logs for each method"""
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    """Count number of GET requests to /status"""
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{status_check_count} status check")
    """Aggregate to find the top 10 most present IPs"""
    print("IPs:")
    top_ips = nginx_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
