def string_compression(string):
    new_string = []
    cur = string[0]
    cur_count = 1
    for i in range(1, len(string)):
        s = string[i]
        if cur == s:
            cur_count += 1
        elif cur is not s:
            new_string.append(cur)
            new_string.append(str(cur_count))
            cur = s
            cur_count = 1
    new_string.append(cur)
    new_string.append(str(cur_count))

    new_string = ''.join(new_string)
    return new_string if len(new_string) < len(string) else string




compressed_string = string_compression("aaabbbc")
print(compressed_string)
