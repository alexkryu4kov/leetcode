def unzip_sequence(seq: str) -> str:
    stack = []
    current_string = ''
    current_number = None

    for elem in seq:
        if elem == '[':
            stack.append({
                'num': current_number, 's': current_string}
            )
            current_string = ''
            current_number = None
        elif elem == ']':
            tmp_map = stack.pop()
            if not tmp_map['num']:  # чтобы обойти кейс, когда по умолчанию не указывается 1 (взято из тестового кейса)
                current_string = tmp_map['s'] + current_string
            else:
                current_string = tmp_map['s'] + current_string * tmp_map['num']
        elif elem.isdigit():
            current_number = int(elem)
        else:
            current_string += elem
    return current_string


assert unzip_sequence('ab[cd]e') == 'abcde'
assert unzip_sequence('a2[c3[de]]') == 'acdededecdedede'
