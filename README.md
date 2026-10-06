# Isha Gulati — AI Product Portfolio

0→1 product builder who designs, builds, and **evaluates** conversational and agentic AI — not just specs it. These are hands-on prototypes I built (primarily in n8n) to take ideas from concept to working product.

## Projects

### 🩺 [MedMatch — Conversational AI Healthcare Navigation Agent](medmatch/)
A conversational agent that turns a plain-language request ("a primary care doctor near 10016 who takes Cigna") into a ranked provider shortlist — with real safety guardrails (emergency detection, no medical advice, no silent actions). Includes a **human + LLM-as-judge evaluation** across test cases that surfaced reliability gaps and drove fixes.
*n8n · LangChain agent · OpenAI · structured output parsing · evaluation framework*

### 🎢 [NBCUniversal Theme Parks — Agentic AI Concierge](nbcu/)
An agentic concierge for theme-park guests: an inbound conversational agent that books dining and experiences, an **MCP tools layer** over the park data model, and an **outbound multichannel engine** that personalizes outreach across text, email, and **ElevenLabs voice calls**. Built as a Stern MBA consulting prototype for NBCUniversal.
*n8n · OpenAI + Google Gemini · Model Context Protocol (MCP) · ElevenLabs · Lovable*

---

**Note:** These are prototypes. API keys, resource IDs, and any personal/test data have been redacted and replaced with placeholders; the data layers use sample data only. To run a workflow, add your own credentials in n8n.

**Contact:** [LinkedIn](https://linkedin.com/in/isha-gulati-nyu) · ig667@stern.nyu.edu
