
import gradio as gr
from pdf_parser import extract_sections
from critique_engine import generate_critique

def analyze_paper(pdf_file):
    sections = extract_sections(pdf_file)
    critique = generate_critique(sections)
    return critique["summaries"], critique["gaps"], critique["suggestions"]

with gr.Blocks() as demo:
    gr.Markdown("# Research Paper Critique Generator")
    with gr.Row():
        pdf_input = gr.File(label="Upload Research Paper (.pdf)", file_types=[".pdf"])
        analyze_btn = gr.Button("Analyze")
    
    with gr.Tab("Section Summaries"):
        summaries_output = gr.Textbox(lines=20, label="Summaries")

    with gr.Tab("Research Gaps"):
        gaps_output = gr.Textbox(lines=10, label="Identified Gaps")

    with gr.Tab("Suggestions"):
        suggestions_output = gr.Textbox(lines=10, label="Suggestions")

    analyze_btn.click(fn=analyze_paper, inputs=pdf_input,
                      outputs=[summaries_output, gaps_output, suggestions_output])

demo.launch()
