# Isha Gulati — AI Product Portfolio

0→1 product builder who designs, builds, and **evaluates** conversational and agentic AI — not just specs it. These are hands-on prototypes I built (primarily in n8n) to take ideas from concept to working product.

## Projects

### 🩺 [MedMatch — Conversational AI Healthcare Navigation Agent](medmatch/)
A conversational agent that turns a plain-language request ("a primary care doctor near 10016 who takes Cigna") into a ranked provider shortlist — with real safety guardrails (emergency detection, no medical advice, no silent actions). Includes a **human + LLM-as-judge evaluation** across test cases that surfaced reliability gaps and drove fixes.
*n8n · LangChain agent · OpenAI · structured output parsing · evaluation framework*

### 🎢 [NBCUniversal Theme Parks — Agentic AI Concierge](nbcu/)
An AI concierge for theme-park guests. Guests chat with it to book dining and experiences, and it can also reach out to them proactively across text, email, and AI voice calls. An MCP tools layer connects the agent to live park data (reservations, schedules, availability) so it can make real bookings — not just talk. Built as a Stern MBA consulting prototype for NBCUniversal.
*n8n · OpenAI + Google Gemini · Model Context Protocol (MCP) · ElevenLabs · Lovable*

### 🧵 [TailorMe - AI-Powered Custom Tailoring Agent](tailor-agent/)
An AI agent that helps turn an idea for a custom outfit into something a tailor can actually make. Inspired by the still-common practice of working with small, independent tailors in countries like India, TailorMe takes a simple brief like “I need an outfit for a wedding” and turns it into a structured, tailor-ready design spec. It helps define the style, generates original design concepts, and estimates measurements from clothes you already own, while clearly flagging uncertainty and what needs to be confirmed at a fitting.
*Python · structured spec extraction · size-chart estimation · generate-don't-scrape guardrails*

---

**Note:** These are prototypes. API keys, resource IDs, and any personal/test data have been redacted and replaced with placeholders; the data layers use sample data only. To run a workflow, add your own credentials in n8n.

**Contact:** [LinkedIn](https://linkedin.com/in/isha-gulati-nyu) · ig667@stern.nyu.edu
