from transformers import *
import torch
import numpy

gpu_available = torch.cuda.is_available()
print(gpu_available)

# number of GPUs I have:
num = torch.cuda.device_count()
print(f'I have {num} GPUs')

# current device index
idx = torch.cuda.current_device()
print(f'My current device has index {idx}')

# GPU's name
name = torch.cuda.get_device_name(idx)
print(f'My GPU is {name}')

dict_of_embeddings = {}
if __name__ == '__main__':
    #getting available device. Will get GPU if its available else will fall back to cpu
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    #list of the file names that need to be embedded. For now just using a sample file to get the embeddings.
    File_names=["bert_sentences.txt"]

    #load the pretrained model
    model = BertModel.from_pretrained('bert-base-multilingual-cased')
    model.to(device)
    model.eval()

    #load the tokenizer
#     tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    embeddings=[]

    for file in File_names:
        f = open(file)
        for line in f:

            tokenized_text = tokenizer.tokenize(line)
            #print(tokenized_text)
            tokens_ids = tokenizer.convert_tokens_to_ids(tokenized_text)
            #print(tokens_ids)
            segment_ids = [1] * len(tokens_ids)

            #converting python lists to torch tensors
            tokens_tensor = torch.tensor([tokens_ids])
            segments_tensors = torch.tensor([segment_ids])

            # Extract hidden states representation of the original sentence
            with torch.no_grad():
                encoded_hidden_states, _ = model(tokens_tensor.to(device), segments_tensors.to(device))
            # print(encoded_hidden_states)
            print(encoded_hidden_states.size())

for token in tokenized_text:
    if token not in dict_of_embeddings:
        dict_of_embeddings[token] = encoded_hidden_states[0][0].cpu().numpy()

with open('listfile.txt', 'w') as filehandle:
    for token in dict_of_embeddings:
        filehandle.write(token+" ")
        for val in dict_of_embeddings[token]:
            filehandle.write(str(val)+" ")
        filehandle.write("\n")
