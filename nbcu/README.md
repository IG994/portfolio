# NBCUniversal Theme Parks — Agentic AI Concierge (Prototype)

An agentic AI concierge for theme-park guests: guests can plan a trip, book dining and experiences, and get proactively reached out to about relevant offers — in natural language, across chat, text, email, and voice. A guest can say *"find me a dinner reservation near the kids' area on Saturday and add the character breakfast,"* and the agent interprets the request, checks availability through its tools, confirms, and books.

Built as a graduate consulting project (NYU Stern Tech MBA) for **NBCUniversal Theme Parks**, and presented to NBCUniversal stakeholders. **My role:** I designed and prototyped the agentic concierge — the conversation design, the n8n agent/tool workflows, and the multichannel (including ElevenLabs voice) outreach. *(Team project — adjust this line to your exact contribution.)*

---

## The problem

Planning and navigating a theme-park visit is high-friction: guests juggle reservations, dining, ride schedules, add-ons, and offers across disconnected apps and channels. The concierge turns that into a single conversation — and can also reach *out* to guests at the right moment, on the channel they actually use.

## What it does

- **Understands natural-language requests** and holds a stateful, multi-turn conversation (session memory).
- **Takes real actions through tools** — looks up users, reservations, dining, experiences, schedules, and add-ons, and writes back confirmations (bookings, add-ons).
- **Recommends and books** experiences and dining, returning a structured reply plus suggested follow-up prompts to keep the guest moving.
- **Reaches out proactively** — for a marketing campaign, it picks each guest's *preferred channel*, personalizes a script from their history, and delivers it via text, email, or an **ElevenLabs voice call**.
- **Never acts silently** — bookings/add-ons happen on explicit confirmation.

## Architecture

Built in **n8n** as three complementary workflows:

```
                       ┌─────────────────────────────────────────┐
                       │  (1) MCP Tools Layer                     │
                       │  Google Sheets exposed as agent tools:   │
                       │  users · reservations · dining ·         │
                       │  experiences · schedule · add-ons ·      │
                       │  campaigns · bookings                    │
                       └───────────────┬─────────────────────────┘
                                       │ (Model Context Protocol)
           inbound                     │                      outbound
┌──────────────────────────────┐      │      ┌──────────────────────────────────┐
│ (3) Interactive Concierge     │◄─────┴─────►│ (2) Outbound Multichannel Engine │
│ Webhook chat agent            │             │ Route by channel → personalize   │
│ OpenAI + Gemini + memory      │             │ script from campaign + history → │
│ books / recommends →          │             │ send text / email / ElevenLabs   │
│ structured JSON + follow-ups  │             │ voice call                       │
└──────────────────────────────┘             └──────────────────────────────────┘
```

1. **MCP tools layer** (`workflow/01-mcp-tools-layer.json`) — an MCP server exposing the data model (reservations, users, dining, experiences, schedules, add-ons, campaigns, bookings) as callable tools, so any agent can read and write park data through one interface.
2. **Interactive concierge agent** (`workflow/03-interactive-concierge-agent.json`) — a webhook-triggered conversational agent (OpenAI + Google Gemini) with session memory that answers guests, recommends and books experiences/dining, and returns a structured `response_message` + `suggested_followup_prompts`.
3. **Outbound multichannel engine** (`workflow/02-outbound-multichannel-engine.json`) — routes each guest by preferred channel, generates a personalized script from the active campaign and the guest's past conversations, and delivers it via text, email, or an ElevenLabs voice call.

**Stack:** n8n (orchestration) · OpenAI (GPT-4.1-mini) + Google Gemini · Model Context Protocol (MCP) · ElevenLabs (voice) · Google Sheets (prototype data layer) · Lovable (frontend prototype).

## Honest scope & limitations

- **Prototype / proof-of-concept**, not a production system — built to demonstrate the experience and architecture.
- **Prototype data only.** The data layer is a Google Sheet with sample park data we modeled; it is **not** connected to any real NBCUniversal system and contains no real guest data.
- **Team project.** Built with a Stern MBA consulting team; see the role note above.
- **Credentials redacted.** API keys, resource IDs (ElevenLabs agent/phone, Google Sheet), and a test phone number have been replaced with placeholders (`REDACTED` / `YOUR_…`). To run it, add your own credentials in n8n.

## Files

- `workflow/01-mcp-tools-layer.json` — MCP server exposing park data as tools
- `workflow/02-outbound-multichannel-engine.json` — channel routing + personalized text/email/voice outreach
- `workflow/03-interactive-concierge-agent.json` — webhook conversational booking agent
- `docs/` — workflow canvas screenshots *(add your n8n canvas image here)*
