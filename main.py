from board_dao import *

board_dao = BorardDAO()

# 커넥션 테스트
# board_dao.get_connection()


while True:

    print("=" * 40)
    print("1.목록 2.등록 3.내용 4.삭제 0.종료")
    print("=" * 40)

    menu = input("선택 > ")

    if menu == "0":
        break
    elif menu == "1": # 게시판 select * from board
        boards = board_dao.select_all()
        print(boards)

        for board in boards:
            print(board[0],
                  board[1],
                  board[3],
                  board[4])
            

print("게시판 종료")