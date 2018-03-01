# PyMySQL-Driver

## Example
    import mysqld

    mysql_connection_params = {
        'host': '255.255.255.255',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'database_name',
        'charset': 'utf8'
    }
    db = mysqld.DB(**mysql_connection_params)
    query = 'SELECT * FROM `table` WHERE `column1` = %s AND `column2` = %s'
    query_data = ('foo', 'bar')
    data = db.array_query(query, query_data, with_fields)

## Methods

### run_query(query, data=False)
Only execute query, does not return anything.

### array_query(query, data=False, with_fields=False)
Return list of dicts with DB rows. Also returns the field names in the order they are specified in the database if the 'with_fields' flag is true.