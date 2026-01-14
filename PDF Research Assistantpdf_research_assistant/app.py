from ui import create_interface

if __name__ == "__main__":
    demo = create_interface()
    demo.launch(share=True, debug=False, server_name="0.0.0.0", server_port=7860)
