from langchain.tools import Tool
from typing import Any

from llms.llm import llm
# --- Context Presence Judge Tool ---
def build_context_presence_tool(llm: Any, prompt_path: str) -> Tool:
    """
    Creates a tool that evaluates whether a user query contains sufficient context.

    This tool:
    - Loads a prompt template from a file
    - Formats the template with user input
    - Uses an LLM to judge context adequacy
    - Returns a ready-to-use Tool object

    Args:
        llm (Any): The language model instance to use for evaluation
        prompt_path (str): Path to the prompt template file

    Returns:
        Tool: Configured tool for context presence evaluation

    Raises:
        FileNotFoundError: If the prompt template file doesn't exist
        ValueError: If the prompt template is malformed

    Example:
        >>> judge_tool = build_context_presence_tool(llm, "prompts/context_check.txt")
        >>> judge_tool.run("What's the capital?||Speaking about France")
    """
    try:
        # Load prompt template with explicit encoding and error checking
        with open(prompt_path, "r", encoding="utf-8") as file:
            prompt_template = file.read().strip()

            if not prompt_template:
                raise ValueError("Prompt template file is empty")

            if "{input}" not in prompt_template:
                raise ValueError("Prompt template must contain '{input}' placeholder")

        def judge_context_presence(input_text: str) -> str:
            """
            Evaluates whether the input contains sufficient context.

            Args:
                input_text (str): User input to evaluate

            Returns:
                str: LLM's judgment about context adequacy
            """
            try:
                formatted_prompt = prompt_template.replace("{input}", input_text)
                response = llm(formatted_prompt)
                return response.strip()
            except Exception as e:
                return f"Error evaluating context: {str(e)}"

        return Tool.from_function(
            func=judge_context_presence,
            name="ContextPresenceJudge",
            description="""Evaluates whether user queries contain sufficient context.
            Use this when you need to determine if additional context is required
            to properly answer a question.""",
            handle_tool_error=True
        )

    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt template file not found at {prompt_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to create context judge tool: {str(e)}")


# Make sure this prompt file exists with appropriate content
context_tool = build_context_presence_tool(llm, prompt_path="prompts/context_judge_prompt.txt")






   
