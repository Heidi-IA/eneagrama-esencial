"""
Genera data/questions.json a partir de data/source.xlsx
Hoja: "Eneagrama Express"
Columnas: Número | Casilla | Afirmación | Tipo (E1..E9)
"""
import json
import openpyxl
from pathlib import Path

INPUT_XLSX = Path("data/source.xlsx")
OUTPUT_JSON = Path("data/questions.json")


def main():
    if not INPUT_XLSX.exists():
        raise FileNotFoundError(f"No se encontró {INPUT_XLSX}")

    wb = openpyxl.load_workbook(INPUT_XLSX)
    ws = wb["Eneagrama Express"]

    questions = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        num, casilla, texto, tipo = row
        if num is None or texto is None or tipo is None:
            continue
        tipo_str = str(tipo).strip()
        if tipo_str.startswith("E") and tipo_str[1:].isdigit():
            tipo_num = int(tipo_str[1:])
            if 1 <= tipo_num <= 9:
                questions.append({
                    "id": int(num),
                    "text": str(texto).strip(),
                    "type": tipo_num
                })

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(
        json.dumps({"questions": questions, "stats": {"total": len(questions)}},
                   ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print(f"OK: {len(questions)} preguntas generadas en {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
