def simple_tokenize(text, specials=True):
    begin, alpha, space, numeric, non_alpha = (0, 1, 2, 3, 4)
    tokens = []
    afters = []
    token_positions = []
    start_pos = 0
    end_pos = 0
    state = begin
    while end_pos < len(text):
        token = None
        state_changed = False
        prev_state = state
        if text[end_pos].isalpha() or text[end_pos] == '-':
            if not state in [begin, alpha]:
                state_changed = True
            state = alpha
        elif text[end_pos].isspace():
            if not state in [begin, space]:
                state_changed = True
            state = space
        elif text[end_pos].isnumeric():
            if not state in [begin, numeric]:
                state_changed = True
            state = numeric
        else:
            if state != begin:
                state_changed = True
            state = non_alpha
        if state_changed:
            if prev_state != space and (specials or prev_state != non_alpha):
                token = text[start_pos:end_pos]
                tokens.append(token)
                token_positions.append({'start_pos' : start_pos, 'end_pos' : end_pos})
                if state == space:
                    afters.append(' ')
                else:
                    afters.append('')
            start_pos = end_pos
        end_pos += 1

    token = text[start_pos:end_pos]
    tokens.append(token)
    token_positions.append({'start_pos' : start_pos, 'end_pos' : end_pos})
    afters.append('')
    return tokens, afters, token_positions

tokens, afters, token_positions  = simple_tokenize('name, account balance, total equity, assets, liabilities, last update date')

# if ',' in tokens:
#     new_tokens = []
#     new_token_positions = []
#     op = []
#     start_pos = -1
#     end_pos = -1
#     for index in range(len(tokens)):
#         if tokens[index] is ',':
#             end_pos = token_positions[index-1]['end_pos']
#             new_tokens.append(' '.join(op))
#             new_token_positions.append({'start_pos' : start_pos, 'end_pos' : end_pos})
#             # print(' For word :',' '.join(op),'start_pos : ', start_pos,'end_pos : ',end_pos)
#             start_pos = -1
#             end_pos = -1
#             op = []
#         else:
#             # print('\n',tokens[index], token_positions[index]['start_pos'])
#             if start_pos == -1:
#                 start_pos = token_positions[index]['start_pos']
#             op.append(tokens[index])
#
#         if index == len(tokens)-1:
#             new_tokens.append(' '.join(op))
#     print('\n----------------------------------First')
#     print(new_tokens)
#     print('------------------------------------')
#     print(new_token_positions)
#     print('------------------------------------')
#
#     # stripped = map(str.strip, tokens)
#     # print(' '.join(stripped).split(','))

wordlist = [{'text': ['account'], 'category': 'entity', 'id': '1', 'scope': '', 'datatype': ''}, {'text': ['account', 'creation', 'date'], 'category': 'property', 'id': '2', 'scope': '1', 'datatype': 'string'}, {'text': ['password'], 'category': 'property', 'id': '3', 'scope': '1', 'datatype': 'string'}]
