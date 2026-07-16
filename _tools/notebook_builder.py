import json
import sys
from pathlib import Path

def create_notebook(markdown_content, filepath):
    cells = []
    for block in markdown_content.split('---CELL---'):
        block = block.strip()
        if not block:
            continue
        if block.startswith('CODE:'):
            code = block[5:].strip()
            cells.append({
                "cell_type": "code",
                "metadata": {},
                "source": [code],
                "outputs": []
            })
        else:
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": [block]
            })

    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
    print(f"Created: {path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python notebook_builder.py <output_path>")
        print("Reads markdown from stdin, split by ---CELL---")
        sys.exit(1)
    content = sys.stdin.read()
    create_notebook(content, sys.argv[1])
