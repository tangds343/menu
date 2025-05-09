def show_menu():
    print("1. 选项一")
    print("2. 退出")

def main():
    while True:
        show_menu()
        choice = input("请输入选项：")
        if choice == "1":
            print("你选择了选项一")
        elif choice == "2":
            break
        else:
            print("无效选项")

if __name__ == "__main__":
    main()
