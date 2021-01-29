"""
Abstract base class for all database models
"""


class Model():
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def list(self):
        return []
