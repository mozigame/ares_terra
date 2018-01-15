import com.bc.cp.util.mysql_util as mysql_util


def get_all_data():
    conn = mysql_util.get_conn()
    if conn is None:
        print('--> get mysql conn failed!')
        return
    cursor = conn.cursor()
    sql = 'select id,name from tab1'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(str(result))


if __name__ == '__main__':
    get_all_data()
