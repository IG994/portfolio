# Isha Gulati: AI Product Portfolio

0→1 product builder who designs, builds, and evaluates conversational and agentic AI. These are hands-on prototypes I built (primarily in n8n) to take ideas from concept to working product.

## Projects

### 🩺 [MedMatch — Conversational AI Healthcare Navigation Agent](medmatch/)
A conversational agent that helps people find the right healthcare provider. It turns a plain-language request, such as “a primary care doctor near 10016 who takes Cigna”, into a ranked shortlist of relevant providers. Built with safety guardrails including emergency detection, no medical advice, and no actions without user approval. A human + LLM-as-judge evaluation framework tested performance across realistic scenarios, surfaced reliability gaps, and informed improvements.
*n8n · LangChain agent · OpenAI · structured output parsing · evaluation framework*

### 🎢 [NBCUniversal Theme Parks — Agentic AI Concierge](nbcu/)
An agentic AI concierge designed to make theme-park planning and booking easier. The prototype combines an inbound conversational agent that can book dining and other experiences, an MCP tools layer that connects the agent to park data, and an outbound engine that personalizes guest outreach across text, email, and ElevenLabs voice calls. Built as an NYU Stern MBA consulting project for NBCUniversal.
*n8n · OpenAI + Google Gemini · Model Context Protocol (MCP) · ElevenLabs · Lovable*

---

**Note:** These are prototypes. API keys, resource IDs, and any personal/test data have been redacted and replaced with placeholders; the data layers use sample data only. To run a workflow, add your own credentials in n8n.

**Contact:** [LinkedIn](https://linkedin.com/in/isha-gulati-nyu) · ig667@stern.nyu.edu
