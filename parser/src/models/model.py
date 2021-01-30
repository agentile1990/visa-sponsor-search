"""
Abstract base class for all database models
"""


class Model():
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def upsert(self, data):
        return None

    def list(self):
        return []

    def find(self, id):
        return None
