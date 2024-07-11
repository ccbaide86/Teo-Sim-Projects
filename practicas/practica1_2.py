# Arboles de Huffman con Flet

import flet as ft
import heapq
import os
from collections import defaultdict, Counter

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def calculate_frequency(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return Counter(text)

def build_huffman_tree(frequencies):
    heap = [Node(freq, symbol) for symbol, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_huffman_codes(node, code=''):
    if node is None:
        return {}
    
    if node.left is None and node.right is None:
        return {node.symbol: code}
    
    codes = {}
    codes.update(generate_huffman_codes(node.left, code + '0'))
    codes.update(generate_huffman_codes(node.right, code + '1'))
    
    return codes

def compress_file(file_path, output_path, huffman_codes):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    encoded_text = ''.join([huffman_codes[char] for char in text])
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(encoded_text)
    
    return encoded_text

def save_codes(huffman_codes, codes_path):
    with open(codes_path, 'w', encoding='utf-8') as codes_file:
        for symbol, code in huffman_codes.items():
            codes_file.write(f'{symbol}:{code}\n')

def main(page: ft.Page):
    page.title = "Arlobes de Huffman"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    utils_dir = os.path.join(script_dir, 'utils')
    output_file_path = os.path.join(utils_dir, 'compressed_file.txt')
    codes_file_path = os.path.join(utils_dir, 'huffman_codes.txt')

    def on_compress(e):
        input_file_path = file_input.value
        frequencies = calculate_frequency(input_file_path)
        huffman_tree = build_huffman_tree(frequencies)
        huffman_codes = generate_huffman_codes(huffman_tree)
        
        compress_file(input_file_path, output_file_path, huffman_codes)
        save_codes(huffman_codes, codes_file_path)
        
        result_text.value = f"Archivo comprimido guardado en: {output_file_path}\nCódigos de Huffman guardados en: {codes_file_path}"
        page.update()
    
    file_input = ft.TextField(label="Ruta del archivo", width=300)
    compress_button = ft.ElevatedButton(text="Comprimir", on_click=on_compress)
    result_text = ft.Text(value="")

    title = ft.Container(
        content=ft.Text("Compresión de Archivos con Árboles de Huffman",  weight=ft.FontWeight.BOLD, size=20),
        border=ft.border.all(1, ft.colors.TRANSPARENT),
        padding=8,
    )
    
    page.add(
        ft.Column([
            title,
            file_input,
            compress_button,
            result_text
        ])
    )

ft.app(target=main)
