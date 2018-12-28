def gen_dict(s: str) -> dict:
    if not s:
        return {}
    li = str(s).split(":")
    keys, values = li[0::2], li[1::2]
    if len(li) % 2:
        values.append("")
    return dict(zip(keys, values))
