## AI Agents with ADK

### Introduction
<walkthrough-tutorial-duration duration="120"></walkthrough-tutorial-duration>

The world of Generative AI (GenAI) is evolving rapidly, and AI Agents are currently a hot topic. An AI agent is a smart computer program designed to act on your behalf, much like a personal assistant. It can perceive its digital environment, make decisions, and take actions to achieve specific goals without direct human control. Think of it as a proactive, autonomous entity that can learn and adapt to get things done.

At its core, an AI agent uses a large language model (LLM) as its "brain" to understand and reason. This allows it to process information from various sources, such as text, images, and sounds. The agent then uses this understanding to create a plan and execute a series of tasks to reach a predefined objective.

You can now easily build your own AI agents, even without deep expertise, due to ready-to-use frameworks like the  [Agent Development Kit](https://google.github.io/adk-docs/) (ADK). We will start this journey by constructing a personal assistant agent to help you with your tasks. Let's begin!

Before starting any Python project, it's good practice to create a virtual environment. This isolates the project's dependencies, preventing conflicts with other projects or the system's global Python packages. 




Before starting any Python project, it's good practice to create a virtual environment. This isolates the project's dependencies, preventing conflicts with other projects or the system's global Python packages. 

> aside positive
> 
> **Note:** We'll be using `uv` to create our virtual environment instead of the standard `venv` package. It's an incredibly fast Python package and project manager written in Rust.
> 
> If you're interested, you can learn more about it in the official  [uv documentation](https://docs.astral.sh/uv/).

#### **1. Create project directory and navigate into it:**

```bash
mkdir ai-agents-adk
cd ai-agents-adk
```

#### **2. Create and activate a virtual environment:**

```bash
uv venv --python 3.12
source .venv/bin/activate
```

You'll see (`ai-agents-adk`) prefixing your terminal prompt, indicating the virtual environment is active.

<img src="../img/lab2/aa915af1d8379132_1440.png" alt="aa915af1d8379132.png"  width="624.00" />

#### **3. Install adk page**

```bash
uv pip install google-adk
```