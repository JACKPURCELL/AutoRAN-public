import re
from tqdm import tqdm
import json


# Define datasets and models
datasets = ['advbench', 'strongreject', 'harmbench']
models = ['geminiflash', 'o3', 'o4mini']

replace_dict = {
    'advbench': 'AdvBench',
    'strongreject': 'StrongReject',
    'harmbench': 'HarmBench',
    'geminiflash': 'Gemini 2.5-Flash',
    'o3': 'ChatGPT o3',
    'o4mini': 'ChatGPT o4-mini'
}
# Prepare to collect data for CSV
csv_data = []

# Function to analyze a specific dataset and model
def analyze_data(dataset, model):
    # Construct the file path based on dataset and model
    file_path = f'/home/ljc/data/AutoRAN/final_3/qwen3_7b_{dataset}_attack_{model}_judge_3.json'
    file_path_new = f'/home/ljc/data/AutoRAN/records/qwen3_8b_{dataset}_attack_{model}.json'
    # Load the JSON list from the file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Process each example
    for example in tqdm(data):
        if "judge" in example:
            del example["judge"]
        if "stage" in example:
            del example["stage"]
        if "new_judge" in example:
            #rename the keys
            example["local_judge"] = example["new_judge"]
            del example["new_judge"]
      
      
    with open(file_path_new, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data analysis for {dataset} with model {model} completed. Results saved to {file_path_new}.")
    
    

if __name__ == "__main__":
    for dataset in datasets:
        
        for model in models:
            print(f"@@@@@@@@@@@ {dataset} {model} start")
            analyze_data(dataset, model)
    # analyze_data_path()