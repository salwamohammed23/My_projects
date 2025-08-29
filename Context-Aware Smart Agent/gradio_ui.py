import gradio as gr

from agent.agent import run_agent

# --- Enhanced Gradio Interface ---
interface = gr.Interface(
    fn=run_agent,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your question here...\nTo add context use format: Question||Context\nExample: What's France's capital||Speaking about a European country"
    ),
    outputs="text",
    title="🤖 Context-Aware Smart Agent",
    description="""
    Advanced system for understanding complex questions:
    - Supports external context using ||
    - Automatically get the answer from context
    - Answers directly or searches when needed
    """,
    examples=[
        ["العاصمة السعودية هي الرياض||ما هي عاصمة مصر؟"],
        ["العاصمة السعودية هي الرياض||ما هي عاصمة السعودية؟"],
        ["عاصمة مصر هي القاهرة||ما هي عملة مصر؟"],
        ["طقس القاهرة اليوم مشمس||ما هي عاصمة مصر؟"],
        
    ]
)
