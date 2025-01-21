from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
device = "cuda" # the device to load the model onto

#model_path = "/home/imc/桌面/Qwen1.5-72B/pythonProject/model/LLM-Research/Meta-Llama-3-8B-Instruct"
model_path = "/home/imc/桌面/aas_rag_generate/Qwen/Qwen2-7B"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

prompt = '''
你好，请问你是谁？
'''
messages = [
    {"role": "system", "content": ""},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)
input_ids = tokenizer.encode(text,return_tensors='pt')
attention_mask = torch.ones(input_ids.shape,dtype=torch.long,device=device)
generated_ids = model.generate(
    model_inputs.input_ids,
    attention_mask=attention_mask,
    max_new_tokens=512,
    pad_token_id=tokenizer.eos_token_id
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)



