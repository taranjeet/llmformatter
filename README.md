# llmformatter

Get deterministic output in any format like json from any LLM.

## Installation

```bash
git clone git@github.com:taranjeet/llmformatter.git
cd llmformatter
python setup.py install
```

## Examples

### Example 1: Get output as json

```python
import openai
from llmformatter import llm_formatter

openai.api_key = "sk-..."

# get output as json which can be parsed
prompt = """You need to provide a single random question along with the correct answer related to Naruto. You will generate a question, four options, one correct, three wrong. The options should have no labels like A, B, C or D. Options should be unique and should not contain repetitive or same value. Correct answer must exist in the options."""

response_normal = openai.ChatCompletion.create(messages=[{"role": "user", "content": prompt}], model="gpt-3.5-turbo", temperature=0, top_p=1)
print(response_normal.choices[0].message.content)

"""
Question: What is the name of the technique that allows Naruto to create multiple shadow clones of himself?

Options:
- Rasengan
- Chidori
- Kage Bunshin no Jutsu
- Amaterasu

Correct answer: Kage Bunshin no Jutsu
"""

# notice how the above output is not json and parsing this will be difficult
# now let's use the llm_formatter to get the json output only

response_format = openai.ChatCompletion.create(messages=[{"role": "user", "content": llm_formatter(prompt, "json")}], model="gpt-3.5-turbo", temperature=0, top_p=1)
print(response_format.choices[0].message.content)
{
  "question": "What is the name of the village where Naruto was born?",
  "options": [
    "Konohagakure",
    "Sunagakure",
    "Kirigakure",
    "Iwagakure"
  ],
  "answer": "Konohagakure"
}

```

### Example 2: Get output as code

```python
import openai
from llmformatter import llm_formatter

openai.api_key = "sk-..."

# get output as code which can be written straightaway to a file and executed
prompt = "Write a python function to sum two numbers"

response_normal = openai.ChatCompletion.create(messages=[{"role": "user", "content": prompt}], model="gpt-3.5-turbo", temperature=0, top_p=1)
print(response_normal.choices[0].message.content)

"""
Here's a simple Python function that takes two numbers as input and returns their sum:

```python
def add_numbers(num1, num2):
    return num1 + num2
\```

You can call this function with any two numbers you want, like this:

```python
result = add_numbers(5, 7)
print(result)  # Output: 12
\```

In this example, we're passing the numbers 5 and 7 to the `add_numbers` function, which returns their sum (12). We're then printing the result to the console using the `print` function.

"""

# notice how the above output contains both code and text
# now lets use llm_formatter to only get the code output for above example

response_format = openai.ChatCompletion.create(messages=[{"role": "user", "content": llm_formatter(prompt, "code")}], model="gpt-3.5-turbo", temperature=0, top_p=1)
print(response_format.choices[0].message.content)

def sum_numbers(a, b):
    return a + b
```

## Available formats

### json

* Returns the format as json.
* Can be used as

```python
from llmformatter import llm_formatter

llm_formatter(prompt, "json")
```

### code

* Returns the format as code.
* Can be used as

```python
from llmformatter import llm_formatter

llm_formatter(prompt, "code")
```