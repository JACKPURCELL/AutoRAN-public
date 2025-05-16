from datasets import load_dataset



class HarmBench:
    def __init__(self):
        self.dataset = load_dataset("walledai/HarmBench", 'standard')
        self.result_list = self.dataset_preprocess()
        self.column_names = ["prompt", "context","category"]

    def dataset_preprocess(self):
        train_data = self.dataset["train"]
        result_list = []
        for item in train_data:
            # item["category"] = "N/A"
            result_list.append(item)

        return result_list


if __name__ == "__main__":
    advbench = HarmBench()
    result_list = advbench.dataset_preprocess()
    print(result_list)
    