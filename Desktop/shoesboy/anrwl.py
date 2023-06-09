import random

print("묵찌빠 게임을 시작합니다.")

while True:
    user_choice = input("묵, 찌, 빠 중에서 하나를 선택하세요 (끝내려면 '끝'을 입력하세요): ")
    if user_choice == "끝":
        print("게임을 종료합니다.")
        break
    elif user_choice not in ("묵", "찌", "빠"):
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue

    # 컴퓨터가 무작위로 선택
    computer_choice = random.choice(["묵", "찌", "빠"])
    print(f"컴퓨터: {computer_choice}")

    # 묵찌빠 규칙 적용
    if user_choice == computer_choice:
        print("비겼습니다! 다시 선택해주세요.")
        continue
    elif user_choice == "묵":
        if computer_choice == "찌":
            print("컴퓨터가 이겼습니다!")
        elif computer_choice == "빠":
            print("당신이 이겼습니다!")
    elif user_choice == "찌":
        if computer_choice == "묵":
            print("당신이 이겼습니다!")
        elif computer_choice == "빠":
            print("컴퓨터가 이겼습니다!")
    elif user_choice == "빠":
        if computer_choice == "묵":
            print("컴퓨터가 이겼습니다!")
        elif computer_choice == "찌":
            print("당신이 이겼습니다!")
