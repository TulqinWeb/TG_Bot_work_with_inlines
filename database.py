import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.conn.cursor()

    def get_all_regions(self):
        self.cur.execute("""SELECT * FROM regions""")
        regions = dict_fetchall(self.cur)
        return regions

    def get_countries_by_region(self, region_id):
        self.cur.execute("""SELECT * FROM countries WHERE region_id= ?""", (region_id,))
        countries = dict_fetchall(self.cur)
        return countries

    def get_all_jobs(self):
        self.cur.execute("""SELECT * FROM jobs""")
        jobs = dict_fetchall(self.cur)
        return jobs

    def get_employee_by_job(self, job_id):
        self.cur.execute("""SELECT * FROM employees WHERE job_id= ?""", (job_id,))
        employees = dict_fetchall(self.cur)
        return employees


def dict_fetchall(cursor):
    columns = [i[0] for i in cursor.description]
    print(columns)
    return [dict(zip(columns, row)) for row in cursor.fetchall()]
