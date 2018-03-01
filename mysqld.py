import MySQLdb

class DB:

    param = {}

    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.param['db'] = db
        self.param['host'] = host
        self.param['port'] = port
        self.param['user'] = user
        self.param['passwd'] = passwd
        self.param['charset'] = charset
        self.connect()

    def connect(self):
        self.conn = MySQLdb.connect(**self.param)

    def run_query(self, query, data=False):
        arglist = [query]
        if data:
            arglist.append(data)
        try:
            cursor = self.conn.cursor()
            cursor.execute(*arglist)
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(*arglist)
        return cursor

    def array_query(self, query, data=False, with_fields=False):
        cursor = self.run_query(query, data)
        data = cursor.fetchall()
        description = cursor.description
        fields = {x: description[x][0] for x in range(0, len(description))}
        fields_order = [x[0] for x in description]
        result = []
        for row in data:
            row_data = {}
            for field_number in fields:
                row_data[fields[field_number]] = row[field_number]
            result.append(row_data)
        if with_fields:
            return result, tuple(fields_order)
        else:
            return result