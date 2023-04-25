"""Top-level package for llmformatter."""

__author__ = """Taranjeet Singh"""
__email__ = 'reachtotj@gmail.com'
__version__ = '0.1.0'


"""Main module."""


JSON_PROMPT_SUFFIX = """
Output should be only a valid JSON object. Dont include any other text or explanation.

Json:
"""

CODE_PROMPT_SUFFIX = """
Output should be a valid code. Remember this code will be used as it is directly in production, so it should work. Dont include any other text or explanation.

Code:"""


def llm_formatter(prompt, output_type):
    """
    Format the prompt according to output_type, so that
    output from LLM is in that format.
    """
    final_prompt = prompt
    if output_type.lower() == "json":
        final_prompt = f"""{prompt}\n{JSON_PROMPT_SUFFIX}"""
    elif output_type.lower() == "code":
        final_prompt = f"""{prompt}\n{CODE_PROMPT_SUFFIX}"""
    return final_prompt
