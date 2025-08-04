from transformers import RobertaTokenizer, T5ForConditionalGeneration

def load_model():
    from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base-multi-sum")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5-base-multi-sum")
    return tokenizer, model

def summarize_code(code, tokenizer, model):
    input_text = f"summarize this Python function: {code.strip()}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512)
    summary_ids = model.generate(
    input_ids, 
    max_length=100, 
    num_beams=4, 
    repetition_penalty=2.5, 
    early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
