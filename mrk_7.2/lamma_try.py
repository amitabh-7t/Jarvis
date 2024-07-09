from llama_index.llms.llama_api import LlamaAPI
api_key = "LL-njIR0xcZUjVmfA5m7BPEO9SUBRaxcysf2DQzJIeuvEGFdynsrtjqRcE5MmpqoHX4"
llm = LlamaAPI(api_key=api_key)
query:str = input("user :- ")

resp = llm.complete(query)
print(resp)