
def Open_File(Str_File,Mode):
    file = open(Str_File,Mode,encoding = 'utf-8')
    # print('Tên của file là: ', file.name)
    # print('File có đóng hoặc không?: ', file.closed)
    # print('Chế độ mở file: ', file.mode)
    if(Mode == 'r'):
        Temp_str = file.read()
        # print('nội dung file là: \n',Temp_str)
        file.close()
        return Temp_str

def Count_Word_Char (File_name):
    with open(File_name, encoding='utf-8') as file:
        text = file.read().strip().split()
        len_chars = sum(len(Word) for Word in text)
        len_Word  = len(text)
        print(f'Số từ trong file {File_name} là: {len_Word}')
        print(f'Số ký tự trong file {File_name}  là: {len_chars}')
def Count_Word_Unduplicate(File_name):
    with open(File_name, encoding='utf-8') as file:
        text = file.read().strip().split()
        list_Unduplicate = list(set(text))
        len_char_unduplicate = sum(len(Word) for Word in list_Unduplicate)
        print(f'Tổng số từ không trùng lặp trong file {File_name} là: {len(list_Unduplicate)}')
        print(f'Tổng số ký tự không trùng lặp trong file {File_name} là: {len_char_unduplicate}')

def Write_Data_File(File_name,Data_W):
    with open(File_name, 'a', encoding='utf-8') as f:
        f.write(' '+ Data_W)
        print(f'Đã ghi xong vào cuối file {File_name} với nội dung là : {Data_W}')

if __name__ == '__main__':
    # cau a :
    # Open_File('covid19.txt','r')
    #cau b:
    #cau c:
    Count_Word_Char('covid19.txt')
    #cau d:
    Count_Word_Unduplicate('covid19.txt')
    #cau e:
    str_one = input('Nhập nội dung cần ghi vào cuối file: ')
    Write_Data_File('covid19.txt',str_one)