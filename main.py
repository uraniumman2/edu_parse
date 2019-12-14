from edu_parse import EduParse
from getpass import getpass

webdriver_path = "D:/EDU_PARS/chromedriver_win32/chromedriver.exe"


def print_hello():
    print("'''''''''''   '''''     ''''''   '''''     '''''")
    print(" ''''''''''    '''      '''''     '''       ''' ")
    print(" '''      '    '''     ''''''     '''       ''' ")
    print(" '''           '''    ''' '''     '''       ''' ")
    print(" '''======'    '''   '''  '''     '''       ''' ")
    print(" '''======,    '''  '''   '''     '''       ''' ")
    print(" '''           ''' '''    '''     '''       ''' ")
    print(" '''      '    ''''''     '''     ''''     '''' ")
    print(" ''''''''''    '''''      '''      '''''''''''  ")
    print("'''''''''''   ''''''     '''''      '''''''''   ")


if __name__ == '__main__':
    print_hello()
    iin_text = input("ИИН:")
    password_text = getpass("Пароль:")
    print(password_text)
    edu_parse_obj = EduParse(iin_text, password_text, webdriver_path)
    edu_parse_obj.parse()
