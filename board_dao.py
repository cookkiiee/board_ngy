import pymysql

class BorardDAO:

    def __init__(self):

        self.host = "localhost"
        self.user = "board_user"
        self.password = "board1234"
        self.database = "board_db"

    def get_connection(self):

        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset="utf8mb4"
        )
       
    def insert_board(self, title, content, writer):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO board
        (title, content, writer)
        VALUES
        (%s, %s, %s)
        """
        
        # sql = f"""
        #     INSERT INTO board
        #     (title, content, writer)
        #     VALUES
        #     ('{title}', '{content}', '{writer}')
        #     """

        # f-string → 출력문, 로그용
        # %s 파라미터 바인딩 → SQL용
        
        cursor.execute(
            sql,
            (title, content, writer)
        )

        conn.commit()
        cursor.close()
        conn.close()

        print("등록 완료")

    def select_all(self):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM board
        ORDER BY id DESC
        """

        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()

        return result

    def select_one(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        return result

    def delete_board(self, board_id):

        conn = self.get_connection()
        cursor = conn.cursor()

        sql = """
        DELETE
        FROM board
        WHERE id=%s
        """

        cursor.execute(sql, (board_id,))

        # 삭제된 행이 없으면
        if cursor.rowcount == 0:

            conn.rollback()
            cursor.close()
            conn.close()

            return False

        # 남아 있는 게시글 번호를 1번부터 다시 정렬
        cursor.execute("SET @num = 0")

        sql = """
        UPDATE board
        SET id = (@num := @num + 1)
        ORDER BY id ASC
        """

        cursor.execute(sql)

        # 현재 가장 큰 번호 확인
        sql = """
        SELECT MAX(id)
        FROM board
        """

        cursor.execute(sql)
        max_id = cursor.fetchone()[0]

        if max_id is None:
            next_id = 1
        else:
            next_id = max_id + 1

        # 다음 등록 번호 설정
        sql = f"""
        ALTER TABLE board
        AUTO_INCREMENT = {next_id}
        """

        cursor.execute(sql)

        conn.commit()
        cursor.close()
        conn.close()

        return True