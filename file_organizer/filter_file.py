def filter_files(directory, all_extentions):

    filtered_files = (
        []
    )  # список, в котором будут храниться файлы с фильтруемыми расширениями
    files = []  # список, в котором будут храниться слова, разделённые знаком "."
    separated_names = list(
        map(lambda file: file.split("."), directory)
    )  # список, в котором будут храниться все наименования в папке (directory), разделённые знаком "."
    for separated_file_name in separated_names:
        for file_name_part in separated_file_name:
            if file_name_part in all_extentions:
                files.append(separated_file_name)
    for separated_file_name in files:
        filtered_files.append(".".join(separated_file_name))
    return filtered_files
