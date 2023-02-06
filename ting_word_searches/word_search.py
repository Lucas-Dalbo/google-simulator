def find_lines(file, word):
    lines = []
    for line_id in (0, file["qtd_linhas"] - 1):
        line = file["linhas_do_arquivo"][line_id].lower()
        if line.find(word.lower()) >= 0:
            line_obj = {"linha": line_id + 1}
            lines.append(line_obj)
    return lines


def exists_word(word, instance):
    queue_len = instance.__len__()
    result = []
    for i in range(0, queue_len):
        file = instance.search(i)
        lines = find_lines(file, word)
        if len(lines) > 0:
            file_obj = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines,
            }
            result.append(file_obj)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
