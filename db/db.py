# MySQL DB initialization

from flask_mysqldb import MySQL
from flask_mysqldb import cursors, MySQLdb
import os


def db_init(mysql: MySQL):
    """ Check if the required schema exists and, if not, create and populate with the initial data """

    try:
        cur: cursors.BaseCursor = mysql.connection.cursor()
    except MySQLdb.OperationalError as e:
        print(f"MySQL Operational Error: {str(e)}. Please, fix the problem before starting the program!")
        exit(1)

    try:
        cur.execute(f"SELECT * FROM {mysql.app.config['MYSQL_DB']}.students LIMIT 1")
    except MySQLdb.DatabaseError as e:
        code = e.args[0]

        if code == 1146:
            # table 'students' does not exist
            _create_students_table(cur)
            _create_default_admin(cur)
            mysql.connection.commit()

def _create_students_table(cur: cursors.BaseCursor):
    with open(os.path.join('db', 'sql', 'init.sql')) as init_sql_file:
        script = init_sql_file.read()
        cur.execute(script)

def _create_default_admin(cur: cursors.BaseCursor, email = "admin@example.com", password = "admin"):
    res = cur.execute("INSERT INTO `students`(`Name`, `Email`, `Password`, `Role`) VALUES ('Admin',%s,%s,'ADMIN')", [email, password])
