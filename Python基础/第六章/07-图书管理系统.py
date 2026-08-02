from abc import ABC,abstractmethod
import json
#书籍类

class Book:
    def __init__(self,book_id,title,author,total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.__available_num = total_num

    def borrow_book(self):
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        else:
            return False

    def return_book(self):
        self.__available_num += 1

    def get_available_num(self):
        return self.__available_num

#会员类,抽象类,只能被继承,不能被直接实例化,规定了子类必须实现那些方法,强制子类遵循统一的代码规范
#Python中的重新类需要继承abc模块中的ABC类
class Member(ABC):
    def __init__(self,member_id,name,password):
        self.name = name
        self.__password = password
        self.member_id = member_id
        self.__borrowed_books = []#借书列表

    def borrow_book(self,book:Book):
        #判断当前会员借阅数量是否达到限度
        if len(self.__borrowed_books) >=self.get_max_books():
            print("借阅失败,您的借阅数量已达到最大限制")
            return False
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}已借阅{book.title}")
            return True
        else:
            print(f"借阅失败,图书{book.title}已被借完")
            return False
    def return_book(self,book:Book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name}已成果归还图书{book.title}")
        else:
            print(f"归还失败,您未借阅图书{book.title}")
    def get_password(self):
        return self.__password
    def get_borrowed_books(self):
        return self.__borrowed_books
    #获取最大借阅数量,不同会员
    @abstractmethod
    def get_max_books(self):
        pass

class NormalMember(Member):
    def get_max_books(self):
        return 3

class VIPMember(Member):
    def __init__(self,member_id,name,password,vip_level):
        super().__init__(member_id,name,password)
        self.vip_level = vip_level


    def get_max_books(self):
        return 6+self.vip_level


#图书馆管理系统
class LibrarySystem ():
    def __init__(self):
        self.books = {}
        self.members = {}
        self.current_member:Member|None = None
        #加载数据
        self.load_books_data()
        self.load_members_data()

    def load_members_data(self):
        with open("data/members.json","r",encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']]=NormalMember(member['卡号'],member['姓名'],member['密码'])
                elif member['卡号'].startswith('V'):

                    self.members[member['卡号']]=VIPMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])
            print("加载会员数据成功")
    def load_books_data(self):

        with open("data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                self.books[book['编号']] = Book(book['编号'], book['标题'], book['作者'], book['数量'])
            print("书籍加载完毕")

    def login(self):
        while True:
            print()
            print("[登录]")
            member_id = input("请输入会员卡号:")
            password = input("请输入会员密码:")

            if member_id not in self.members:
                print("登陆失败,该会员卡号不存在")
                continue

            member = self.members[member_id]

            if password == member.get_password():
                self.current_member = member
                print(f"登录成功!欢迎您{member.name}")
                return True
            else:
                print("密码错误")
                continue


    def borrow_book(self):
        #1.展示当前图书的图书列表
        for book in self.books.values():
            print(f"编号,{book.book_id},标题:{book.title},作者:{book.author},总数:{book.total_num},可用:{book.get_available_num()}")
        #获取用户输入
        book_id = input("请输入要借阅的图书编号:")
        if book_id not in self.books:
            print("此编号不存在,请重新输入")
            return
        else:
            self.current_member.borrow_book(self.books[book_id])

    def return_book(self):
        #展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("已借阅的图书列表:")
        for book in borrowed_books:
            print(f"编号:{book.book_id},标题:{book.title}")


        #获取输入的编号
        book_id = input('请输入要归还的编号')
        if book_id not in self.books:
            print("此编号不存在,还书失败")
            return
        else:
            self.current_member.return_book(self.books[book_id])
    def show_borrowed_books(self):
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("已借阅的图书列表如下:")
            for book in borrowed_books:
                print(f"编号:{book.book_id},标题:{book.title}")
        else:
            print("您并未借阅任何一本图书!")


    def run(self):
        if self.login():
            while True:
                print('\n1:借阅图书')
                print('2:归还图书')
                print('3:查看借阅')
                print('4:退出系统')
                print()

                choice = input("请选择操作(1-4):")
                match choice:
                    case '1':
                        self.borrow_book()
                    case '2':
                        self.return_book()
                    case '3':
                        self.show_borrowed_books()
                    case '4':
                        print("退出系统,加纳")
                        break
                    case _:
                        print("无效选项,请重新选择")




if __name__ == '__main__':
    ls = LibrarySystem()
    ls.run()


