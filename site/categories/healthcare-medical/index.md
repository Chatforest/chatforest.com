# Healthcare & Medical MCP Servers — 3 Reviews Covering FHIR, EHR, Drug Discovery, PubMed, Medical Imaging, Mental Health, and More

> Comprehensive reviews of 3 Healthcare & Medical MCP server categories — covering FHIR/EHR integration, drug discovery, PubMed, clinical trials, medical imaging, genomics, mental


We've reviewed **3 categories** of Healthcare & Medical MCP servers, evaluating over **85 individual servers** across electronic health records, drug discovery, medical research, imaging, genomics, mental health, and wellness tracking. Each review covers architecture patterns, star counts, tool inventories, known issues, and honest ratings.

Healthcare is the deepest and most mature vertical MCP category. FHIR proved to be the perfect complement to MCP — healthcare already had a standardized data format, so MCP servers could focus on the AI integration layer rather than data normalization. WSO2's FHIR server (98 stars) leads EHR integration with SMART-on-FHIR auth, while healthcare-mcp-public (101 stars) bundles FDA, PubMed, clinical trials, ICD-10, and DICOM into a single gateway. The OpenPharma initiative maintains 45 coordinated repositories — the largest organized MCP server collection for any industry. ChEMBL's 22-tool drug discovery server and multiple PubMed implementations show genuine demand from biomedical researchers. Innovaccer's HMCP extends the MCP protocol itself for HIPAA compliance — a signal that healthcare takes this technology seriously.

---

## Clinical & Medical Data

The clinical data landscape spans FHIR/EHR integration (6+ competing implementations), multi-source healthcare hubs (FDA, PubMed, ICD-10 bundled together), medical research (PubMed and ClinicalTrials.gov), drug databases (DrugBank 17,000+ compounds), medical imaging (DICOM/PACS), and healthcare standards (HIPAA-compliant protocol extensions). Vendor participation is strong — AWS, WSO2, Innovaccer, and LangCare all ship production-grade servers.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Healthcare & Medical](/reviews/healthcare-medical-mcp-servers/) | 4.0/5 | Cicatriiz/healthcare-mcp-public (101 stars, 9 tools — FDA/PubMed/clinical trials/ICD-10/DICOM), wso2/fhir-mcp-server (98 stars, SMART-on-FHIR auth), JackKuo666/PubMed-MCP-Server (104 stars, deep paper analysis), ChristianHinge/dicom-mcp (86 stars, 11 DICOM/PACS tools), JamesANZ/medical-mcp (75 stars, 15 tools, zero API keys), cyanheads/clinicaltrialsgov-mcp-server (58 stars, patient-to-trial matching) — 30+ servers |

## Pharmaceutical & Drug Discovery

The deepest vertical MCP category we have reviewed — 40+ servers with institutional backing from WSO2, Innovaccer, and the OpenPharma initiative (45 coordinated repositories covering FDA, EMA, DrugBank, ClinicalTrials, PubMed, CDC, and more). Drug discovery has end-to-end MCP coverage: ChEMBL (22 tools for compound search, target analysis, bioactivity, ADMET), DrugBank (17,430+ drugs with sub-10ms SQLite queries), and genomics (NCBI 31 tools across 9 categories). PubMed is the most replicated MCP server in healthcare with 5+ independent implementations.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Pharmaceutical & Healthcare](/reviews/pharmaceutical-healthcare-mcp-servers/) | 4.5/5 | Augmented-Nature/ChEMBL-MCP-Server (77 stars, 22 drug discovery tools), healthcare-mcp-public (102 stars, 9 tools), wso2/fhir-mcp-server (98 stars, FHIR CRUD), ChristianHinge/dicom-mcp (86 stars, PACS imaging), cyanheads/pubmed-mcp-server (66 stars, 7 tools + citation formatting), OpenPharma initiative (45 repos), Innovaccer HMCP (28 stars, protocol extension) — 40+ servers |

## Mental Health & Wellness

The most experimental subcategory — most servers have under 10 stars and are early-stage projects. Two paradigms exist: servers supporting human mental health (mood tracking, journaling, coping tools) and servers supporting AI agent wellbeing (therapeutic personas, digital rest). Oura Ring integration leads by adoption (37 stars). Zenify is the most comprehensive platform with RAG-powered conversations and suicide risk detection. mcp-wisdom provides 9 philosophical thinking tools from Stoic, Cognitive, and Mindfulness traditions. Privacy-first approaches dominate — multiple servers keep all data local with no external API calls.

| Review | Rating | Key Servers |
|--------|--------|-------------|
| [Mental Health & Wellness](/reviews/mental-health-wellness-mcp-servers/) | 3.0/5 | tomekkorbak/oura-mcp-server (37 stars, Oura Ring sleep/readiness data), ishpreet404/Zenify (10 stars, crisis detection + RAG chatbot), evangstav/personal-mcp (9 stars, health tracking), aplaceforallmystuff/mcp-wisdom (3 stars, 9 philosophical tools), mtct/journaling-mcp (5 stars, emotional analysis) — 15+ servers |

## Notable Gaps

Despite being the most mature vertical MCP category, healthcare has significant holes:

- **No official EHR vendor servers** — neither Epic nor Cerner has released an MCP server despite extensive FHIR APIs
- **No pharmacy workflow servers** — drug databases exist but nothing for e-prescribing or medication reconciliation
- **No clinical decision support engines** — no rule-based CDS beyond what EHR systems provide internally
- **No CBT/DBT therapy servers** — no evidence-based therapeutic tools with validated instruments (PHQ-9, GAD-7)
- **No clinical documentation** — no nursing notes, physician documentation, or medical transcription MCP servers
- **No medical device integration** — beyond DICOM, no IoMT (vital signs monitors, infusion pumps, wearables)
- **No crisis hotline integration** — no server connecting to 988 Suicide & Crisis Lifeline or equivalent services

