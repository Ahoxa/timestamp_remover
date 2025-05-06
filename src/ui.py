import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from formatter import clean_and_merge_lines


def start_ui():
    def save_to_desktop():
        input_text = text_input.get("1.0", tk.END)
        cleaned_text = clean_and_merge_lines(input_text)

        desktop = Path.home() / "Desktop"
        output_file = desktop / "cleaned_text.txt"

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(cleaned_text)
            messagebox.showinfo("保存完了", f"ファイルを保存しました:\n{output_file}")
        except Exception as e:
            messagebox.showerror("保存エラー", f"保存に失敗しました:\n{e}")

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
