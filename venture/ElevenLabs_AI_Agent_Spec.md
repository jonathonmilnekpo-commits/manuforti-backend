# ElevenLabs Conversational AI Agent — Spec
## "Ask Procurement AI" — Andreas Alnes Voice Agent
**Statkraft Procurement AI Programme | March 2026**

---

## CONCEPT

Build a conversational AI agent that:
1. Uses a voice cloned from **Andreas Alnes** (or approved voice stand-in)
2. Can explain the Statkraft Procurement AI strategy
3. Answers questions about AI use cases, benefits, and roadmap
4. Delivers a 2-3 minute video introduction to the strategy
5. Can be embedded in presentations or SharePoint

---

## WHAT ELEVENLABS CAN DO (2026)

- **Voice Cloning:** Professional Voice Clone (PVC) from ~30 min of clean audio
- **Conversational AI 2.0:** Full dialogue agent with memory, personality, knowledge base
- **Multimodal:** Text + voice simultaneously
- **Custom knowledge base:** Upload PDFs/docs — agent answers from them
- **API integration:** Can connect to OpenClaw for deeper procurement queries
- **Video generation:** Combine with HeyGen/D-ID for talking head video

---

## TWO DELIVERABLES

### Deliverable 1: Strategy Introduction Video (3-5 min)

A scripted video where "Andreas" introduces the Procurement AI Strategy.

**Script outline:**
> "At Statkraft, we're at a turning point in how we manage procurement.
> The data is clear — 94% of procurement executives are already using AI every week.
> Companies like Equinor have saved $130 million in a single year.
> Shell is automating contract review. Vattenfall is transforming how they do category strategy.
> The question isn't whether to adopt procurement AI. The question is: how fast do we move?
> Here's our plan..."
> [walks through 5 key slides]

**Production:**
- Script written by Aiden
- ElevenLabs generates voice
- Combine with slide animations using HeyGen or D-ID
- Output: MP4, shareable via Teams/email

### Deliverable 2: Interactive Q&A Agent

A conversational agent colleagues can ask questions like:
- "What is spend classification and why does it matter?"
- "How does the supplier monitoring agent work?"
- "What data from SAP does the AI need?"
- "Is our data safe in the cloud?"
- "What's the ROI of the contract NLP scanner?"

**Tech stack:**
```
User question (text or voice)
       ↓
ElevenLabs Conversational AI 2.0
       ↓
Knowledge base: this strategy deck + SAP/Jaggaer integration plan
       ↓
Voice response (Andreas Alnes clone)
       ↓
[Optional] Escalate to OpenClaw agent for live data queries
```

---

## IMPLEMENTATION STEPS

### Step 1: Voice Clone (Andreas Alnes — requires consent)
1. Obtain consent from Andreas Alnes (mandatory — ElevenLabs TOS)
2. Record 30 min of clean audio in a quiet environment
3. Upload to ElevenLabs Professional Voice Clone
4. Test quality across different sentence types
5. Store voice ID securely in Statkraft secrets manager

### Step 2: Knowledge Base Setup
Upload these documents to ElevenLabs agent knowledge base:
- `Statkraft_Procurement_AI_Strategy_v2.pptx`
- `SAP_Jaggaer_AI_Integration_Plan.md`
- `Statkraft_Procurement_AI_Value_Model.xlsx` (summary MD version)
- FAQ document (20-30 common questions + answers)

### Step 3: Agent Configuration
```json
{
  "agent_name": "Statkraft Procurement AI Guide",
  "voice_id": "[Andreas_Alnes_PVC_ID]",
  "model": "eleven_turbo_v2_5",
  "language": "en",
  "system_prompt": "You are the Statkraft Procurement AI guide. Your role is to explain our AI strategy clearly and confidently to colleagues. You are knowledgeable, direct, and encouraging. Never discuss competitor-sensitive pricing or confidential negotiations. If asked about specific live data, say you will escalate to the live agent. Keep answers concise — under 90 seconds.",
  "knowledge_base": ["statkraft_ai_strategy", "sap_jaggaer_plan"],
  "first_message": "Hi, I'm here to answer your questions about Statkraft's Procurement AI programme. What would you like to know?"
}
```

### Step 4: Video Production (Strategy Introduction)
1. Generate audio via ElevenLabs API
2. Create slide animations in PowerPoint/Canva
3. Combine using HeyGen (talking head) or simple slide + voice overlay
4. Upload to Statkraft SharePoint / Teams channel
5. Embed link in strategy deck as QR code

---

## COST ESTIMATE

| Item | Cost |
|------|------|
| ElevenLabs Professional Plan | ~€330/month (~€4K/yr) |
| Professional Voice Clone | Included in Professional plan |
| HeyGen/D-ID for video | ~€50/month |
| **Total annual cost** | **~€4,600/yr** |

---

## IMPORTANT: CONSENT AND COMPLIANCE

- ⚠️ **MANDATORY:** Written consent from Andreas Alnes before voice cloning
- ⚠️ ElevenLabs requires identity verification for PVC
- ⚠️ Only use for internal/approved communications
- ✅ ElevenLabs Conversational AI data can be configured EU-residency
- ✅ No sensitive procurement data should be in the knowledge base

---

## ALTERNATIVE: Use a different voice

If Andreas Alnes consent is not obtained or desired, alternatives:
- Use Jonathon Milne's voice (as Manu Forti deliverable to Statkraft)
- Use a professional ElevenLabs Norwegian-accented voice
- Use a neutral British/American professional voice

---

*Prepared by Aiden | March 17, 2026 | Internal use*
