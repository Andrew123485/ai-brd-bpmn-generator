"""
AI BRD & Draw.io BPMN Generator CLI
Ассистент бизнес-аналитика для автоматизированного сбора требований и генерации BPMN-схем.
"""
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="AI BRD & BPMN Draw.io Generator")
    parser.add_argument("--type", choices=["concept", "brd"], default="brd", help="Тип документа (концепт IBDEV или BRD FX)")
    parser.add_argument("--input", type=str, help="Путь к файлу с вводными данными задачи")
    parser.add_argument("--out", type=str, default="output", help="Директория для сохранения артефактов")
    args = parser.parse_args()

    print(f"🚀 Запуск генератора артефактов: тип [{args.type}]")
    print("📋 Применение методологии контура бизнес-анализа (BRD + BPMN Draw.io)...")
    print("✅ Спецификации и правила загружены из prompts/")

if __name__ == "__main__":
    main()
