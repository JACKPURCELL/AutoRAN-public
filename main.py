
import subprocess
from openai import OpenAI
import time
import json
import openai
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig
import os
client = OpenAI()
from transformers import TextStreamer
from datasets import load_dataset
import re
import wandb
import json
import os
from tqdm import tqdm
from datetime import datetime

from util.gpt import ask_gpt


import strategy as strategy_class


import dataset as dataset_class





def select_samples(result_list, num_samples=5):
    category_samples = {}
    output_results = []
    for example in result_list:
        category = example["category"]
        if category not in category_samples:
            category_samples[category] = []
        if len(category_samples[category]) < num_samples:
            category_samples[category].append(example)
            output_results.append(example)
    return output_results


def main(output_file,name,backup_file,final_output_file):

    # Initialize wandb
    # date and time
    strategy_name = "HCoT_SM_T3_ONEJUDGE_QWQ"
    
    
    strategy = getattr(strategy_class, strategy_name)()
    wandb.init(project="qwen7b_attack", name=name)

    # Define wandb table
    column_names = strategy.column_names
    
    table = wandb.Table(columns=strategy.column_names)

    if os.path.exists(output_file):
        with open(output_file, "r", encoding="utf-8") as f:
            result_list = json.load(f)
        print(f"Load {len(result_list)} data...")
    else:
        print(f"File {output_file} Not exist!")
        return
   
    
    processed_results = []

    if os.path.exists(backup_file):
        with open(backup_file, "r", encoding="utf-8") as f:
            processed_results = json.load(f)
        print(f"Recover backup {len(processed_results)} Data...")
        processed_results = [result for result in processed_results if result is not None]
        for result in processed_results:
            # if isinstance(result["r1_answer_or_not"],str):
            #      result["r1_answer_or_not"] = False
            data = [result.get(column, None) for column in column_names]
            table.add_data(*data)
            

    try:
        for example in tqdm(result_list, desc="Processing Examples"):
            if any(res["prompt"] == example["prompt"] for res in processed_results):
                print("⏭️ Skip ", example["prompt"])
                continue  

            result = strategy.process_example(example)
            if result is None:
                continue
            processed_results.append(result)
         
            data = [result.get(column, None) for column in column_names]
            table.add_data(*data)
            wandb.log(result)

            if len(processed_results) % 2 == 0:
                with open(backup_file, "w", encoding="utf-8") as f:
                    json.dump(processed_results, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print(f"⚠️ Error occurred: {e}")
        print("🔄 Trying to upload processed data to wandb...")

        # Ensure partial data is not lost
        wandb.log({"Processed Table": table})
        wandb.finish()

        # Save to local even if exception occurs
        with open(backup_file, "w", encoding="utf-8") as f:
            json.dump(processed_results, f, indent=4, ensure_ascii=False)

        raise  # Re-raise exception for debugging

    # If all data processed successfully
    wandb.log({"Processed Table": table})
    wandb.finish()

    # Save final results locally
    with open(final_output_file, "w", encoding="utf-8") as f:
        json.dump(processed_results, f, indent=4, ensure_ascii=False)

    # Delete backup file (data has been fully saved)
    if os.path.exists(backup_file):
        os.remove(backup_file)

    print("✅ Processing complete, all data uploaded to wandb and saved locally!")




if __name__ == "__main__":
    print("@@@@@@@@@@@ advbench start")
    name = "advbench"
    output_file = "/home/ljc/data/AutoRAN/data/qwen3_8b_full_generate_advbench.json"
    backup_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_advbench_attack_backup.json" 
    final_output_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_advbench_attack_results.json" 
    main(output_file,name,backup_file,final_output_file)
    
    
    print("@@@@@@@@@@@ advbench done")
    print("@@@@@@@@@@@ strongreject start")
    name ="strongreject"
    output_file = "/home/ljc/data/AutoRAN/data/qwen3_8b_full_generate_strongreject.json"
    backup_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_strongreject_attack_backup.json"
    final_output_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_strongreject_attack_results.json"
    main(output_file,name,backup_file,final_output_file)
    print("@@@@@@@@@@@ strongreject done")
    
    print("@@@@@@@@@@@ harmbench start")
    name ="harmbench"
    output_file = "/home/ljc/data/AutoRAN/data/qwen3_8b_full_generate_harmbench.json"
    backup_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_harmbench_attack_backup.json"
    final_output_file = "/home/ljc/data/AutoRAN/data/output/qwen3_8b_harmbench_attack_results.json"
    main(output_file,name,backup_file,final_output_file)
    print("@@@@@@@@@@@ harmbench done")