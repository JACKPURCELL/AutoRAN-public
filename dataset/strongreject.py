from datasets import load_dataset

class StrongReject:
    def __init__(self):
        self.dataset = load_dataset("walledai/StrongREJECT")
        self.result_list = self.dataset_preprocess()
        self.column_names = ["prompt", "category"]    
    def dataset_preprocess(self):
        # 假设我们只关注 train 拆分（如果还有其他拆分，如 test、validation，可根据需求修改）
        train_data = self.dataset["train"]

        # 2. 获取所有不同的 category
        categories = list(set(train_data["category"]))
        print("All categories:", categories)

        # 3. 针对每个 category 选取前 20 条数据
        category_samples = {}
        for cat in categories:
            # 通过 filter 筛选出当前 category 的数据
            cat_subset = train_data.filter(lambda x: x["category"] == cat)
            # 只取前 20 条
            category_samples[cat] = cat_subset


        result_list = []

        for cat, dataset in category_samples.items():
            # 将列式数据转为行式
            for example in dataset:
                example["category"] = cat  # 保存 category 到 example 中
                result_list.append(example)
        
        return result_list



    def select_samples(self, num_samples=5):
        category_samples = {}
        output_results = []
        for example in self.result_list:
            category = example["category"]
            if category not in category_samples:
                category_samples[category] = []
            if len(category_samples[category]) < num_samples:
                category_samples[category].append(example)
                output_results.append(example)
        return output_results