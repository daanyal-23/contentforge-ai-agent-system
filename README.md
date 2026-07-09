# ContentForge AI — Self-Correcting Multi-Agent Content Generation System

A production-style AI agent system that transforms structured product data into high-quality content using LangGraph-powered multi-agent orchestration.

ContentForge AI combines specialized agents, validation gates, execution tracing, and targeted self-correction loops to generate reliable product pages, FAQs, and comparison content.

Unlike traditional sequential pipelines, failed outputs are automatically routed back to the responsible agent for regeneration using LangGraph conditional workflows.

## 🚀 Overview

ContentForge AI demonstrates a production-inspired agentic workflow architecture.

The system uses a shared LangGraph state machine where independent AI agents collaborate, validate outputs, recover from failures, and maintain full execution visibility through structured traces.

Given one product JSON, the system produces:

| Output File          | Description                                                            |
|----------------------|------------------------------------------------------------------------|
| product_page.json    | Structured product page using deterministic content blocks             |
| faq.json             | ≥ 15 validated Q&A items generated from grounded product facts             |
| comparison_page.json | Product A vs. Fictional Product B comparison (ingredients, benefits, price, verdict) |

Core capabilities:

✔ LangGraph StateGraph orchestration  
✔ Specialized multi-agent architecture  
✔ Conditional agent routing  
✔ Targeted self-correction loops  
✔ Agent execution tracing  
✔ Validation-driven regeneration  
✔ Strict JSON schema enforcement  
✔ Deterministic generation with LLM fallback  
✔ Automated test coverage

## ✅ Current Status

- Test Suite: 10/10 passing
- Agent Tracing: Enabled
- Self-Correction Loop: Implemented
- LangGraph Workflow: Active

### 🧠 Self-Correcting Agentic Architecture

The system uses LangGraph StateGraph to coordinate specialized agents through a shared PipelineState.

Architecture flow:

Input Product JSON
        ↓
Sanity Agent
        ↓
Facts Extractor Agent
        ↓
Generation Agents
        ↓
Validator Agent
        ↓
Conditional Router
        ↓
Pass → Renderer Agent

Fail → Responsible Agent Retry


Key capabilities:

- State-based agent communication
- Conditional routing decisions
- Targeted failed-agent retries
- Maximum retry protection
- Execution trace logging
- Validation feedback loops

## 📊 Agent Execution Trace

Every workflow execution produces an observable agent trace.

Example:

```text
[SanityAgent]
SUCCESS → Product schema validation completed

[FactsExtractorAgent]
SUCCESS → Product facts extracted

[QuestionGeneratorAgent]
SUCCESS → FAQ generated

[ValidatorAgent]
FAILED → FAQ validation failed

[LangGraphRouter]
RETRY → Routing retry to FAQAgent

[ValidatorAgent]
SUCCESS → Validation passed
```
This makes debugging, monitoring, and agent behavior analysis easier.

## 📦 Features
### 1. Multi-Agent Modular Architecture

The pipeline is divided into isolated agents:

| Agent                          | Responsibility                                                                 |
|--------------------------------|--------------------------------------------------------------------------------|
| **IngestAgent**                | Reads and normalizes the input product JSON                                    |
| **SanityAgent**                | Validates schema correctness and detects data issues                            |
| **FactsExtractorAgent**        | Converts the product into atomic, reusable factual units                        |
| **FAQAgent (Hybrid Generator)**        | Builds FAQs using a fixed template with sanitization and validation             |
| **ContentBlockAgent (Hybrid Generator)** | Generates a structured product page using a strict JSON template              |
| **ComparisonAgent (Hybrid Reasoning)** | Builds a fictional Product B and performs structured A/B comparison          |
| **RendererAgent**              | Writes all final JSON artifacts to disk                                         |


### 🔁 Hybrid Self-Correcting Generation Pipeline

All generation nodes follow this pattern:

- Primary path: Deterministic agent logic

- Fallback path: LLM-based generation (strict JSON prompts)

- Validation: Schema + content checks

- Retry loop: Graph re-enters generation if validation fails

This ensures:

- Predictable outputs

- Minimal LLM usage

- Repair of malformed or incomplete results

- Reduced hallucination risk through fact-grounded generation and validation

### ⚙️ Technology Stack
| Component              | Description                         |
| ---------------------- | ----------------------------------- |
| Python 3.10+           | Core runtime                        |
| **LangGraph**          | Agentic state-machine orchestration |
| LangChain (v1.1.3)     | Prompt + LLM abstraction            |
| OpenAI GPT-4o-mini     | JSON-locked fallback generation     |
| Pydantic               | Schema validation                   |
| python-dotenv          | Credential management               |
| Execution Trace Logger | Agent observability and debugging   |
| pytest                 | Test suite                          |


### 🧠 Deterministic Content Guarantees

- Same input → same output (timestamps excluded)

- No external data or API calls

- No invented facts

- Fictional Product B derived only from Product A

- Hard schema enforcement at validation stage

#### The system ensures:

- always exactly 15 FAQs

- no empty answers

- answers grounded only in facts_json

- auto-fallback for missing values

### 📋 Validation Rules
#### Product Page

- All required blocks present

- Titles must not be empty

- Values must reflect facts only

#### FAQ

- Exactly 15 FAQs

- Numeric IDs ("1" → "15")

- No empty answers

- Answers derived strictly from facts

#### Comparison Page

- Product B derived deterministically

- Price comparison formatted as:
```bash
"A_only": ["A price: X INR"]
"B_only": ["B price: Y INR"]
"common": ["currency: INR"]
```

Verdict must be one of:

- Product A is cheaper

- Product B is cheaper

- Both priced equally


## 🗂 Project Structure
```bash
contentforge-ai-agent-system/
│
├── run.py                     # Entry point (LangGraph-based pipeline)
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── docs/
│   └── projectdocumentation.md
│
├── examples/
│   └── product_glowboost.json # Sample input
│
├── out/                       # Generated outputs
│   ├── product_page.json
│   ├── faq.json
│   └── comparison_page.json
│
├── src/
│   ├── graph.py               # LangGraph StateGraph orchestration
│   ├── state.py               # Typed PipelineState (shared state)
│   ├── models.py              # ProductModel + schemas
│   ├── langchain_orchestrator.py  # LLM fallback + JSON repair
│   ├── orchestrator.py        # Sequential pipeline implementation
│   ├── utils.py
│   │
│   └── agents/
│       ├── ingest_agent.py
│       ├── sanity_agent.py
│       ├── facts_extractor_agent.py
│       ├── validator_agent.py
│       ├── renderer_agent.py
│       ├── comparison_agent.py
│       ├── content_block_agent.py
│       ├── question_generator_agent.py
│       └── template_engine_agent.py
│
├── tests/
│   ├── test_pipeline.py       # Updated to use LangGraph
│   ├── test_blocks.py
│   ├── test_facts.py
│   ├── test_questions.py
│   ├── test_product_page.py
│   ├── test_comparison.py
│   ├── test_templates.py
│   └── conftest.py


```

## 📄 Input Format

Your input file must be a JSON file with product details, for example:
```bash
{
  "name": "GlowBoost Vitamin C Serum",
  "ingredients": ["Vitamin C", "Hyaluronic Acid", "Glycerin"],
  "benefits": ["Brightening", "Fades dark spots", "Hydration"],
  "usage": "Apply 2–3 drops in the morning before sunscreen.",
  "safety": "Mild tingling in some users; patch test recommended.",
  "price": { "amount": 699, "currency": "INR" }
}
```
## ⚙️ Installation & Setup
### 1️⃣ Clone Repository

```bash
git clone https://github.com/daanyal-23/contentforge-ai-agent-system
cd contentforge-ai-agent-system
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create a .env file:
```bash
OPENAI_API_KEY=your_key
```
## ▶️ Running the System

### Generate all Outputs 
```bash
python run.py --input examples/product_glowboost.json
```
Outputs will appear in:
```bash
/out/product_page.json
/out/faq.json
/out/comparison_page.json
```

## 🧩 Key Design Principles
1. Modularity

Each agent does exactly one task.

2. Determinism

Same input → same output.

3. Agentic orchestration

State + routing + retries

4. Validation-first

Pydantic schema enforcement prevents invalid JSON.

5. Maintainability

Clear separation of concerns, testable units, clean orchestration.

## 🧪 Testing

The project includes tests covering:

- Fact extraction

- Question generation

- Product page rendering

- Comparison logic

- End-to-end pipeline

- Template correctness

- Block generation

## Run all tests:
```bash
python -m pytest -q
```

#### Expected output:
```bash
10 passed in X.XXs
```
## 📝 Assumptions

- Input follows the given product schema.

- Output must be purely machine-readable JSON.

- System must remain modular (each agent = one responsibility).

- No hallucinations or invented facts beyond allowed fictional transformations.

## 🌱 Future Improvements

- Persistent workflow memory
- Batch product processing
- Human approval checkpoints
- FastAPI deployment layer
- LangSmith observability integration

## 🏗 Engineering Highlights

This project demonstrates:

- LangGraph-based agent orchestration
- Feedback-driven self-correction
- Observable agent execution
- State-based workflow design
- Production-style validation patterns
- Modular and testable AI components

## 🙌 Final Notes

Everything here follows an engineering-first mindset: clean modules, predictable behavior, and no hidden magic. It stays readable, testable, and extensible.

If you have any questions about the structure or implementation, feel free to explore the docs/ folder or the individual agent files under src/agents/.