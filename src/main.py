import tkinter as tk
from tkinter import messagebox
import re
from pathlib import Path


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


def save_to_desktop():
    input_text = text_input.get("1.0", tk.END)
    cleaned_text = clean_and_merge_lines(input_text)

    # デスクトップパスを取得
    desktop = Path.home() / "Desktop"
    output_file = desktop / "cleaned_text.txt"

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        messagebox.showinfo(
            "保存完了", f"ファイルをデスクトップに保存しました:\n{output_file}"
        )
    except Exception as e:
        messagebox.showerror("保存エラー", f"ファイルの保存に失敗しました:\n{e}")


# UIの構築
root = tk.Tk()
root.title("タイムスタンプ削除ツール")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

label = tk.Label(
    frame, text="テキストを入力してください（タイムスタンプを削除します）:"
)
label.pack()

text_input = tk.Text(frame, height=20, width=80)
text_input.pack()

save_button = tk.Button(
    frame, text="整形してデスクトップに保存", command=save_to_desktop
)
save_button.pack(pady=10)

root.mainloop()
