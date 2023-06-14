def file_name(file_dir):
    List_file=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.wav':
                    List_file.append(os.path.join(root, file))
    return List_file
