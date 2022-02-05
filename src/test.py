from src.naverblogbacker.utils import isEmptyDirectory
from src.naverblogbacker.blog import BlogCrawler

def main(myId, myPath):
    try:
        # 저장 경로가 빈 폴더가 아닌 경우 에러 발생
        if not isEmptyDirectory(dirPath=myPath):
            pass

        myBlog = BlogCrawler(targetId=myId, skipSticker=True, isDevMode=True)

        # myBlog.crawling(dirPath=myPath)

        print(f'[MESSAGE] Complete! your blog posts, the number of error posts is {BlogCrawler.errorPost}')

    except Exception as e:
        print(e)
        exit(-1)


if __name__ == '__main__':
    ans = True
    while ans:
        print("""
        1.Add a Student
        2.Delete a Student
        3.Look Up Student Record
        4.Exit/Quit
        """)
        ans = raw_input("What would you like to do? ")
        if ans == "1":
            print("\n Student Added")
        elif ans == "2":
            print("\n Student Deleted")
        elif ans == "3":
            print("\n Student Record Found")
        elif ans == "4":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")
    myId = input("Please, Enter your naver id : ")
    print(f'[MESSAGE] YOUR ID IS {myId}')

    myPath = input("Please, Enter empty folder path for saving yours : ")
    print(f'[MESSAGE] SAVE PATH IS {myPath}')

    main(myId, myPath)