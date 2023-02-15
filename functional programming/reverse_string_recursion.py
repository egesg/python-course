def string_reversal(example):
    if len(example) == 0:
        return example
    else:
        return string_reversal(example[1:]) + example[0]

example = "reversal"
reversed_example = string_reversal(example)

print(reversed_example)
# lasrever