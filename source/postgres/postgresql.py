class Postsql:
    def __init__(self):
        import psycopg2
        from data import scts
        self.conn = psycopg2.connect(
            dbname = scts.dbname,
            user = scts.user,
            password = scts.password,
            host = scts.host
        )
        self.cursor_sql = self.conn.cursor()