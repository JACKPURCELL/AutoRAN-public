🧠 AutoRAN: Weak-to-Strong Jailbreaking of Large Reasoning Models
AutoRAN is the first automated weak-to-strong jailbreak attack framework that targets large reasoning models (LRMs) such as GPT-o3, GPT-o4-mini, and Gemini-2.5-Flash. It leverages less-aligned, weak reasoning models to generate and iteratively refine narrative prompts that exploit reasoning traces in stronger models—breaking their safety alignment in just 1–2 turns.

<p align="center"> <img src="figures/template_flow2-1.png" width="80%" alt="AutoRAN Overview"/> </p>
📢 Note: This repository contains controlled research code for evaluating vulnerabilities in reasoning models. All content aligns with ethical and legal guidelines for red-teaming AI systems.

🔍 Key Features
Fully Automated Jailbreaks: AutoRAN requires no human intervention. It starts from a harmful query and constructs a successful jailbreak prompt autonomously.

Narrative Prompt Templates: Uses templated educational or advisory language to mask intent.

Iterative Prompt Refinement: Adapts based on victim model feedback (e.g., refusal reasoning or partial compliance).

Weak-to-Strong Reasoning Alignment: Simulates the target model’s reasoning steps using a weaker model to guide attack construction.

Evaluation Across Models: Demonstrated 100% success rate on GPT-o3, GPT-o4-mini, and Gemini-2.5-Flash across AdvBench, HarmBench, and StrongReject benchmarks.

🚀 Attack Pipeline
The AutoRAN framework follows a 3-step pipeline:

Reasoning Simulation: A weak model simulates the target model’s thought process for a harmful task.

Prompt Initialization: Populates a narrative template with the simulated reasoning.

Prompt Refinement: Uses the target model's response and reasoning trace to adapt prompts iteratively.

<p align="center"> <!-- Replace with your actual figure path --> <img src="figures/detailed_flow3-1.png" width="90%" alt="Attack Flow"/> </p>
📊 Results
AutoRAN achieves near 100% jailbreak success rates within a few queries. It significantly outperforms previous manual or single-shot attacks by adapting to victim model defenses dynamically.

<p align="center"> <!-- Replace with your actual figure path --> <img src="try_times_plot-1.png" width="80%" alt="Turn Distribution"/> </p>
Model	AdvBench	StrongReject	HarmBench	Avg. Queries
GPT-o3	100%	100%	100%	~1.0
GPT-o4-mini	100%	100%	100%	1.35–1.70
Gemini-2.5	100%	100%	100%	~1.0

🛠️ Setup & Usage
bash
Copy
Edit
# Clone the repo
git clone https://github.com/your-org/AutoRAN.git
cd AutoRAN

# Install dependencies
pip install -r requirements.txt

# Run AutoRAN on a test query
python run_attack.py --config configs/gpt_o3_advbench.yaml
📁 Project Structure
bash
Copy
Edit
AutoRAN/
├── configs/              # Benchmark + model configs
├── core/                 # AutoRAN logic: simulation, refinement, evaluation
├── templates/            # Narrative prompt templates
├── figures/              # Visualizations (add your figures here)
├── data/                 # Sample benchmark prompts
├── run_attack.py         # Entry point for running the attack
└── README.md
📌 Citation
If you use this code or build upon this work, please cite the paper:

mathematica
Copy
Edit
@article{AutoRAN2025,
  title={AutoRAN: Weak-to-Strong Jailbreaking of Large Reasoning Models},
  author={Anonymous},
  journal={NeurIPS},
  year={2025}
}
🧷 Disclaimer
This code is released for research and educational purposes only. It is intended to support the responsible evaluation of safety vulnerabilities in LLMs. Do not use this code to target real-world systems or to generate harmful outputs outside controlled environments.

