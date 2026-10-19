

def format_size(size_byte):
    if size_byte == 0:
        return "0 B"
    size_name = ("B","KB","MB","GB","TB")
    i =0

    while size_byte >= 1024 and i < len(size_name) - 1:
        size_byte /= 1024.0
        i += 1
    return f"{size_byte:.2f} {size_name[i]}"
