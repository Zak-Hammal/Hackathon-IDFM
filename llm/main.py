from llm.llm_management import LLMConfiguration
from llm.prompts import prompt_test

llm_config = LLMConfiguration()

input = "I am a human"
response = llm_config.llm.invoke(prompt_test.format(input = input))

print(response)
