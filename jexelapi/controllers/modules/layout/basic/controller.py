from .db_model import {{ class_name }}_tbl

def {{ table_name }}_representation(item:{{ class_name }}_tbl):
    item_dict = item.__dict__
    return item_dict