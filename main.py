from db_create import CreationBD
from parser import get_text_content

if __name__ == '__main__':
    appleinsider_bd = CreationBD()
    for text_element in get_text_content():
        appleinsider_bd.insert_line(text_element['link_news'],
                                    text_element['title'],
                                    text_element['content'])
    appleinsider_bd.print_table_bd()
