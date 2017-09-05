from diary import Diary

if __name__ == '__main__':
    diary = Diary()
    diary.file_read()
    diary.file_safe('2001-10-01','Hahaha nothing')
    diary.file_read()