#!/usr/bin/env osascript
tell application "Mail"
    set newMessage to make new outgoing message with properties {subject:"JSHP Transformer Product 1 Report - v15 Final", content:"Please find attached the completed Product 1 supplier analysis report for JSHP Transformer (JiangSu HuaPeng Transformer Co., Ltd.).

Report Summary:
• Overall Risk Rating: MEDIUM (48/100)
• Recommendation: APPROVE WITH CONDITIONS
• 9-slide executive deck following canonical v15 template
• All mandatory elements included (risk gauge, financial metrics, 2x2 matrix, radar chart, ESG assessment)

Key Findings:
- World's largest Medium Power Transformer producer
- 57-year track record with zero catastrophic failures
- Only Chinese company in top 10 North American transformer brands
- 100% China-based manufacturing requires geopolitical risk mitigation

The report has been validated for 100% template compliance.

Best regards,
Manu Forti Intelligence

---
Source: Manu Forti Intelligence | Confidential | March 2026"}
    tell newMessage
        make new to recipient at end of to recipients with properties {address:"Jonathon.Milne137@gmail.com"}
        make new attachment with properties {file name:"/Users/jonathonmilne/.openclaw/workspace/JSHP_Transformer_Product1_v15_Final.pptx"}
        send
    end tell
end tell