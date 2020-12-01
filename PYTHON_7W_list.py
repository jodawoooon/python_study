
## 미션 1. 연락처 관리 프로그램

menu = ()
friends = []
while menu != 9:
    print("----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이 발견되지 않았음")
    elif menu == 4:
            old_name = input("변경하고 싶은 이름을 입력하시오: ")
            if old_name in friends:
                index = friends.index(old_name)
                new_name= input("새로운 이름을 입력하시오:")
                friends[index] = new_name
            else:
                print("이름이 발견되지 않았음")


## 미션 2. 연락처 관리 프로그램(함수)

def printList(list):
    print(list)

def addFriend(list, name):
    list.append(name)

def removeFriend(list, del_name):
    if del_name in list:
        list.remove(del_name)
    else:
        print("이름이 발견되지 않았음")

def changeName(list, old_name):
    if old_name in list:
        index = list.index(old_name)
        new_name= input("새로운 이름을 입력하시오:")
        list[index] = new_name
    else:
        print("이름이 발견되지 않았음")

def printOption():
    print("----------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")


menu = ()
friends = []
while menu != 9:
    printOption()
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        printList(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        addFriend(friends, name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        removeFriend(friends, del_name)
    elif menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        changeName(friends, old_name)

## 미션 3. tic-tac-toe 게임
        
board= [[' ' for x in range (3)] for y in range(3)]
while True:
        # 게임 보드를 그린다.
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "| "+ board[r][2])

        if (r != 2):
            print("---|---|---")
            # 사용자로부터 좌표를 입력받는다.
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))
    # 사용자가 입력한 좌표를 검사한다.
    if board[x][y] != ' ':
        print("잘못된 위치입니다. ")
        continue
    else:
        board[x][y] = 'X'
    #컴퓨터가 놓을 위치를 결정한다. 첫 번째로 발견하는 비어있는 칸에 놓는다.
    done =False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done=True
                break


## 미션 4. 순차탐색 프로그램

def search_fruits(list, name):
    for i in range(len(list)):
        if name == list[i]:
            print("TRUE")
            return 1

    print("FALSE")
    return -1



data = []
f = open("D:\data.txt", "r")

for line in f.readlines():
    data = line.split(", ")

fruits = input("과일명을 입력하시오 : ")
search_fruits(data, fruits)
