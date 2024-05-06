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

    def last_values(self):
        """
        Método de classe para retornar os 100 valores mais antigos pendentes tratativas.

        id_package, table_0, substatus_package, status_package, date. precisam ser definidas no banco de dados.
        """
        self.cursor_sql.execute("""
            SELECT id_package
            FROM table_0
            WHERE substatus_package IS NULL
            OR status_package IN ('station', 'on_route', 'unknown')
            ORDER BY date ASC
            LIMIT 100;
                                """)