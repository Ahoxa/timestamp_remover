import re


def clean_and_merge_lines(text: str) -> str:
    # タイムスタンプを削除
    text = re.sub(r"\b\d{1,2}:\d{2}\b", "", text)

    # 各行を整形して意味のまとまりを保つ
    lines = text.splitlines()
    merged = ""
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if (
            merged
            and not merged.endswith(("。", "！", "？", "\n"))
            and not stripped[0].isdigit()
        ):
            merged += stripped
        else:
            merged += "\n" + stripped
    return merged.strip()
