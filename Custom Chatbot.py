import torch

from transformers import AutoTokenizer, pipeline

model = "tiiuae/falcon-7b-instruct"

tokenizer= AutoTokenizer.from_pretrained(model)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype = torch.bfloat16,
    device_map = "auto",
    trust_remote_code=True
)

prompt = input("enter your prompt")

newline_token = tokenizer.encode("\n")[0]

my_name = "Ali"
your_name = input("enter your name")
dialog = []

while True:
    user_input = input("> ")
    dialog.append(f"{my_name}: {user_input}")
    prompt = "\n".join(dialog) + f"\n{your_name}: "
    sequences = pipeline(
        prompt,
        max_length=500,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        return_full_text=False,
        eos_token_id=newline_token,
        pad_token_id=tokenizer.eos_token_id,
    )
    print(sequences[0]['generated_text'])
    dialog.append("Bob: "+sequences[0]['generated_text'])
