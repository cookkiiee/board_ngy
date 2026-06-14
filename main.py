from board_dao import *

board_dao = BorardDAO()

# 커넥션 테스트
# board_dao.get_connection()


while True:

    print("=" * 46)
    print("1.조회  2.목록  3.등록  4.내용  5.삭제  0.종료")
    print("=" * 46)

    menu = input("선택 > ")

    if menu == "1":

        num = input("조회 번호 : ")

        board = board_dao.select_one(num)

        if board:

            print()
            print("번호 :", board[0])
            print("제목 :", board[1])
            print("내용 :", board[2])
            print("작성자 :", board[3])
            print("작성일 :", board[4])

        else:

            print("해당 번호의 글이 없습니다.")


    elif menu == "2":

        boards = board_dao.select_all()

        print()
        print(f"{'번호':<6}{'제목':<20}{'작성자':<12}{'작성일'}")
        print("-" * 60)

        for board in boards:

            print(
                f"{board[0]:<6}"
                f"{board[1]:<20}"
                f"{board[3]:<12}"
                f"{board[4]}"
            )


    elif menu == "3":

        title = input("제목 : ")
        content = input("내용 : ")
        writer = input("작성자 : ")

        board_dao.insert_board(
            title,
            content,
            writer
        )


    elif menu == "4":

        num = input("내용 확인 번호 : ")

        board = board_dao.select_one(num)

        if board:

            print()
            print("제목 :", board[1])
            print("내용 :", board[2])

        else:

            print("해당 번호의 글이 없습니다.")


    elif menu == "5":

        num = input("삭제 번호 : ")

        result = board_dao.delete_board(num)

        if result:

            print("삭제 완료")

        else:

            print("해당 번호의 글이 없습니다.")


    elif menu == "0":

        print("프로그램 종료")
        break