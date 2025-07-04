# 🧠 AutoRAN: Weak-to-Strong Jailbreaking of Large Reasoning Models

**AutoRAN** is the first *automated weak-to-strong jailbreak attack framework* targeting large reasoning models (LRMs) such as GPT-o3, GPT-o4-mini, and Gemini-2.5-Flash. It uses less-aligned, weaker models to simulate reasoning patterns and craft narrative prompts that iteratively bypass safety filters.

<p align="center">
  <!-- Replace this with your actual figure -->
  <img src="figures/template_flow2-1.png" width="60%" alt="AutoRAN Overview"/>
</p>

> ⚠️ **Disclaimer**: This repository is intended for controlled security research and AI safety red-teaming only.



## 🔍 Key Features

- ⚙️ **Automated Multi-Turn Jailbreak** via iterative prompt refinement
- 🧩 **Narrative Templates** that frame malicious goals under plausible educational/ethical pretenses
- 🔁 **Refinement Strategies** using intermediate reasoning traces to evolve prompts
- 📈 **Near 100% Attack Success Rate** across commercial LRMs
- 🔬 Evaluated on **AdvBench**, **HarmBench**, and **StrongReject**



## 🛠️ Method Overview

AutoRAN follows a three-stage pipeline:

1. **Simulate Reasoning**: Use a weak model to mimic the victim's high-level CoT structure
2. **Generate Prompt**: Fill in a narrative template using simulated reasoning
3. **Refine Prompt**: Adjust based on intermediate reasoning and safety refusal patterns

<p align="center">
  <!-- Replace this with your actual pipeline figure -->
  <img src="figures/detailed_flow3-1.png" width="90%" alt="AutoRAN Pipeline"/>
</p>



<!-- ## 📙 Example 
<p align="center">
  <img src="figures/modify_example2-1.png" width="60%" alt="Attack Performance"/>
</p> -->

## 📊 Results
<p align="center">
  <!-- Replace this with your actual performance figure -->
  <img src="figures/try_times_plot-1.png" width="60%" alt="Attack Performance"/>
</p>

<!-- | Model          | AdvBench | StrongReject | HarmBench | Avg. Queries |
|----------------|----------|--------------|-----------|--------------|
| GPT-o3         | 100%     | 100%         | 100%      | ~1.0         |
| GPT-o4-mini    | 100%     | 100%         | 100%      | 1.35–1.70    |
| Gemini-2.5     | 100%     | 100%         | 100%      | ~1.0         | -->

<!-- <p align="center">
  <img src="figures/score-1.png" width="100%" alt="Judge"/>
</p> -->

## 📁 Running Records

You can find logs and results in the `/records` directory. For example:

```bash
ls -lh records/
```

---

## 🚀 Quickstart: Demo

```bash
# Clone the repository
git clone {THIS_REPO}
cd AutoRAN

# Install dependencies
pip install -r requirements.txt

# Apply for model access (see HuggingFace link)
# https://huggingface.co/huihui-ai/Qwen3-8B-abliterated/tree/main

# Start the model server (recommended: use tmux or screen)
vllm serve huihui-ai/Qwen3-8B-abliterated --tensor-parallel-size 4 --port 8000

# Edit the attack prompt in demo.py as needed
python demo.py

# Follow the command line instructions.
# You may need to copy questions to GPT-o3, GPT-o4 Mini, or Gemini 2.5-Flash/Pro,
# then paste the results back into the terminal as prompted.
```

---

## 🚀 Full Experiment Workflow

```bash
# Clone the repository
git clone {THIS_REPO}
cd AutoRAN

# Install dependencies
pip install -r requirements.txt

# Set up chat2api for automatic ChatGPT interaction:
# https://github.com/lanqian528/chat2api

# Apply for model access (see HuggingFace link)
# https://huggingface.co/huihui-ai/Qwen3-8B-abliterated/tree/main

# Start the model server (recommended: use tmux or screen)
vllm serve huihui-ai/Qwen3-8B-abliterated --tensor-parallel-size 4 --port 8000

# Run the main experiment script
python main.py
```

## 🧷 Disclaimer
This code is released for research and educational purposes only. It is intended to support the responsible evaluation of safety vulnerabilities in LLMs. Do not use this code to target real-world systems or to generate harmful outputs outside controlled environments.

## 📚 Citation
```bash
@misc{liang2025autoranweaktostrongjailbreakinglarge,
      title={AutoRAN: Weak-to-Strong Jailbreaking of Large Reasoning Models}, 
      author={Jiacheng Liang and Tanqiu Jiang and Yuhui Wang and Rongyi Zhu and Fenglong Ma and Ting Wang},
      year={2025},
      eprint={2505.10846},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2505.10846}, 
}
```
