# 디비 처리, 연결, 해제, 검색어 가져오기, 데이터 삽입
import pymysql

class DBHelper:
    '''
    멤버 변수 : 커넥션
    '''
    conn = None
    """
    생성자
    """

    def __init__(self):
        self.db_init()

        '''
        멤버 함수
        '''
    def db_init(self):
        self.conn = pymysql.connect(
                        host='localhost',
                        user='root',
                        password='mariadb',
                        database='pythonDB',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
        )

    def db_free(self):
        if self.conn:
            self.conn.close()

    # 검색 키워드 가져오기 => 웹에서 검색,
    def db_selectKeyword(self):
        # 커서 오픈
        # with => 닫기를 자동으로 처리하니까 => I/O 에 많이 사용
        rows = None
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM tbl_keyword;"
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        return rows

    def db_insertCrawlingData(self, title, price, area, contents, keyword):
        with self.conn.cursor() as cursor:
            # Read a single record
            sql = '''
                insert into `tbl_crawlingdata` (title, price, area, contents, keyword) 
                values( %s, %s, %s, %s, %s )
            '''
            cursor.execute(sql, (title, price, area, contents, keyword) )
        self.conn.commit()

# 단독으로 수행시에만 작동 => 테스크코드를 삽입해서 사용
if __name__ == '__main__':
    db = DBHelper()
    print(db.db_selectKeyword())
    print(db.db_insertCrawlingData('1','2','3','4','5'))
    db.db_free()
