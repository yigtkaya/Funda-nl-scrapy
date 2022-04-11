# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3 #sqlite3 for database

class FundanlPipeline:

    def __init__(self):
        self.conn = sqlite3.connect("spider")
        self.curr = self.conn.cursor()
        self.create_table()
    # creating table for the scraped data.
    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS houses(
         urls TEXT,
         price TEXT,
         m2 REAL,
         address TEXT,
         roomNumber TEXT
        )""")

    def process_item(self, item, spider):
        self.curr.execute("""INSERT OR IGNORE INTO houses VALUES(?,?,?,?,?)""",
                          (item['urls'], item['price'], item["m2"], item["address"], item["roomNumber"]))
        self.conn.commit()
        return item
