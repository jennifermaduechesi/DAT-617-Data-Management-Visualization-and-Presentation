# -*- coding: utf-8 -*-
"""Single source of truth for the report content. Rendered to both .docx and .pdf."""
import os, re
SC = os.path.dirname(os.path.abspath(__file__))
F1 = os.path.join(SC, "fig1_dikw.png")
F2 = os.path.join(SC, "fig2_workflow.png")
F3 = os.path.join(SC, "fig3_dashboard.png")

def clean(t):
    t = t.replace("—", ", ").replace("&mdash;", ", ")
    t = re.sub(r"\s*--\s*", ", ", t)
    for a, b in [("’","'"),("‘","'"),("“",'"'),("”",'"')]:
        t = t.replace(a, b)
    return t

COVER = [
    ("Pan-Atlantic University", 13, True),
    ("Course Code: DAT 617", 12, False),
    ("Course Title: Data Management, Visualization and Presentation", 12, False),
    ("__gap__", 12, False),
    ("Strengthening Executive Decision-Making at MTN Group: An Integrated Enterprise Analytics, Visualization and AI Strategy", 15, True),
    ("__gap__", 12, False),
    ("Student Name: Maduechesi Chidiebere Jennifer", 12, False),
    ("Surname: Maduechesi", 12, False),
    ("Matriculation Number: 25120133019", 12, False),
    ("Programme: Master of Science (M.Sc.) Data Science", 12, False),
    ("Referencing Style: APA 7th Edition", 12, False),
    ("Submission Date: 6 August 2026", 12, False),
]

# Each element: dict with 'k' (kind) and payload
DOC = [
 {"k":"h1","t":"Executive Summary"},
 {"k":"p","t":"MTN Group runs the largest mobile network in Africa, yet much of the data it generates every second never reaches the people making strategic calls. This report examines that gap. The core problem I identified is rising customer churn and quiet revenue leakage, both worsened by data that sits in disconnected silos across billing, the network, and MTN Mobile Money. Decisions end up being made late and on instinct rather than evidence. Working through the DIKW framework, an enterprise data management plan, and a nine-stage analytical workflow, I show how raw call records and transaction logs can be turned into the kind of knowledge an executive committee can actually act on. The findings point to three things in particular: churn is concentrated in identifiable prepaid segments, network faults cluster in ways that predict complaints, and MoMo data is under-used for cross-sell. My main recommendations are to build a governed central data platform, stand up an executive dashboard tied to a small set of KPIs, and adopt Generative AI for reporting and conversational analytics under a clear ethics policy. Done together, these moves should cut churn, protect revenue, and shorten the distance between a question and a defensible answer."},

 {"k":"h1","t":"1. Organizational Background"},
 {"k":"p","t":"MTN Group is a multinational telecommunications operator headquartered in Johannesburg, South Africa. It runs mobile voice, data, and digital services across roughly nineteen markets in Africa and parts of the Middle East, and its subscriber base sits close to 290 million people. That scale makes it the biggest operator on the continent by some distance. Alongside the core network business, MTN has grown MTN Mobile Money (MoMo) into one of Africa's larger fintech platforms, which matters a great deal for the argument in this report."},
 {"k":"p","t":"The industry context is not gentle. African telecoms operate on thin margins, in price-sensitive markets, under heavy regulation and with constant pressure on the average revenue per user (ARPU). Voice revenue has been sliding for years as data and mobile-money services take over, and competitors such as Airtel Africa are fighting for the same subscribers (GSMA, 2023). Switching networks is cheap for a prepaid customer, so loyalty is fragile and won or lost on price, coverage, and the quality of everyday service."},
 {"k":"p","t":"I chose MTN for three practical reasons. First, the sheer volume and variety of its data, network telemetry, call records, and financial transactions, make it an ideal setting to discuss enterprise data management. Second, it operates in exactly the kind of competitive, margin-pressured market where better analytics changes outcomes. Third, its fintech arm raises data-governance and ethics questions that a purely voice-based operator would not, which lets the later sections go deeper."},

 {"k":"h1","t":"2. Business Problem Analysis"},
 {"k":"p","t":"The problem is straightforward to state and hard to fix: MTN loses customers and revenue faster than it needs to, because its data is fragmented and its decisions lag behind events. Churn in prepaid segments runs high, and every subscriber who leaves takes recurring revenue with them. Revenue leakage, the smaller losses from billing errors, unbilled usage, and fraud, compounds the damage quietly. None of this is new. What makes it a data problem is that the signals needed to catch it early already exist in the network and billing systems. They just aren't joined up."},
 {"k":"p","t":"The organizational impact reaches well beyond the finance line. When customer, network, and payment data live in seperate systems, nobody owns a single view of the customer. Marketing runs retention campaigns without knowing which subscribers are actually about to leave. Network teams fix faults after the complaints arrive rather than before. Executives get monthly reports that are already out of date by the time they land."},
 {"k":"p","t":"A data-driven solution is required precisely because the alternative, experience and gut feel, does not scale to 290 million subscribers. Firms that adopt data-driven decision-making show measurably higher productivity and output than those that don't (Brynjolfsson & McElheran, 2016). For MTN the expected benefits are concrete: earlier churn detection, tighter revenue assurance, faster network response, and marketing spend aimed at the customers who matter. Get this right and the same data that currently sits idle becomes the cheapest competitive advantage the company has."},

 {"k":"h1","t":"3. Application of the DIKW Framework"},
 {"k":"p","t":"The DIKW framework, Data, Information, Knowledge, Wisdom, is a useful way to explain how MTN can climb from raw records to strategic judgement (Ackoff, 1989; Rowley, 2007). Each level adds context and meaning to the one below it, and the value to decision-making rises as you move up."},
 {"k":"fig","path":F1,"num":"Figure 1.","w":5.2,
  "cap":"The DIKW hierarchy applied to MTN Group. Raw operational data at the base is refined into information, then into organizational knowledge, and finally into the strategic wisdom that guides investment and pricing decisions."},
 {"k":"p","t":"At the data level sit the raw materials: call detail records, network alarms, MoMo transaction logs, and CRM entries. On their own they mean little. A single dropped-call record tells you nothing. Information appears once that data is cleaned and aggregated into measures a manager recognises, churn rate by region, ARPU, network uptime, and so on. Knowledge is the next jump, and the important one. It is the patterns across that information: which customer segments churn and why, where network faults recur, what a fraud attempt looks like before it completes."},
 {"k":"p","t":"Wisdom sits at the top. This is where MTN decides where to place its next round of capital spending, which markets to defend hardest, and how to price for retention rather than pure acquisition. The point of the framework is not the diagram itself but the discipline it imposes: data is only worth collecting if there is a path for it to become a decision."},

 {"k":"h1","t":"4. Enterprise Data Management Strategy"},
 {"k":"p","t":"Everything above depends on managing the data well, so this is the section I have given the most weight. An enterprise data management strategy for MTN has to cover where the data comes from, whether it can be trusted, who is accountable for it, and how it is kept safe. I take each component in turn."},
 {"k":"h2","t":"Structured and unstructured data sources"},
 {"k":"p","t":"MTN's structured data is the easy part to picture: billing records, subscriber CRM tables, call detail records, and MoMo transaction logs, all sitting in rows and columns. The unstructured side is larger and messier, and often ignored. It includes call-centre voice recordings, customer complaints and chat transcripts, social-media mentions, and network sensor streams. A serious strategy brings both together, because the reason a customer churns often lives in a complaint transcript, not a billing table."},
 {"k":"p","t":"The table below maps the main sources to what they can support."},
 {"k":"table","num":"Table 1.","cap":"Structured, semi-structured, and unstructured data sources at MTN and their uses.",
  "headers":["Data type","Example sources at MTN","Primary analytical use"],
  "rows":[["Structured","Billing, CRM, call detail records, MoMo ledger","Churn scoring, revenue assurance, ARPU tracking"],
          ["Semi-structured","Network logs, device telemetry, app event data","Fault prediction, quality-of-service monitoring"],
          ["Unstructured","Call recordings, chat and complaint text, social media","Sentiment analysis, root-cause of dissatisfaction"]],
  "widths":[1.4,2.6,2.6]},
 {"k":"h2","t":"Data quality"},
 {"k":"p","t":"Data quality is the foundation, and it is usually where these programmes quietly fail. Wang and Strong (1996) frame quality across accuracy, completeness, timeliness, and consistency, and all four bite at MTN's scale. Duplicate subscriber records, missing location fields, and delayed feeds will wreck a churn model before it starts. Poor quality is expensive in a way that rarely shows up on a single invoice (Redman, 2013). I would put automated validation and profiling at the point of ingestion, so bad data is caught early rather than discovered halfway through an analysis."},
 {"k":"h2","t":"Data governance"},
 {"k":"p","t":"Governance answers a simple question that large firms find surprisingly hard: who is accountable for this data? A workable model assigns clear decision rights and data owners for each domain (Abraham et al., 2019; Khatri & Brown, 2010). For MTN that means naming data stewards for the customer, network, and financial domains, backed by a cross-functional governance council. Without it, every market runs its own definitions and 'churn' means something different in Lagos than it does in Accra."},
 {"k":"h2","t":"Metadata management"},
 {"k":"p","t":"Metadata is the data about the data, the definitions, lineage, and business meaning that let an analyst trust a field they didn't create. A central data catalogue recording where each dataset originates and how a metric is calculated saves enormous time and prevents the contradictory numbers that erode trust in analytics. It sounds dull. It is also the difference between a report an executive believes and one they quietly ignore."},
 {"k":"h2","t":"Data privacy and security"},
 {"k":"p","t":"Because MTN holds financial and location data on hundreds of millions of people, privacy and security are not optional extras. The strategy needs encryption in transit and at rest, role-based access, and compliance with regulations such as Nigeria's NDPR, South Africa's POPIA, and the GDPR where it applies. MoMo raises the stakes further, since a breach there is a financial-crime problem, not just a privacy one. Security has to be designed in from the start, not bolted on after the platform is built."},

 {"k":"h1","t":"5. Enterprise Analytical Workflow"},
 {"k":"p","t":"A data platform only earns its keep if there is a repeatable process turning business questions into decisions. Figure 2 sets out a nine-stage workflow for MTN. It runs from framing the problem through to organizational learning, and the last stage loops back to the first, which is the part most process diagrams forget."},
 {"k":"fig","path":F2,"num":"Figure 2.","w":6.0,
  "cap":"The nine-stage enterprise analytical workflow proposed for MTN. The dashed feedback loop shows how lessons from implementation and organizational learning reshape how the next business problem is framed."},
 {"k":"p","t":"The cycle opens with business problem identification, say, prepaid churn in a specific region, followed by requirements analysis to pin down what a good answer would need. Data collection and data preparation come next, and in practice these two swallow most of the effort; the analysis is quick once the data is clean. Data analysis then produces the models and findings, which data visualization translates into something an executive can read in a glance."},
 {"k":"p","t":"Decision support is where the insight meets a real choice, a retention offer, a network investment, and implementation puts that choice into the market. The final stage, organizational learning, captures what worked and what didn't, then feeds it back so the next cycle starts smarter. Skip that loop and the organization keeps solving the same problem forever."},

 {"k":"h1","t":"6. Data Visualization Strategy"},
 {"k":"p","t":"Executives do not have time to read tables. A visualization strategy for MTN has to turn analysis into a small number of clear, honest pictures that support a decision in seconds. The strategy rests on the right KPIs, sound dashboard design, sensible chart choices, and a bit of storytelling discipline."},
 {"k":"h2","t":"Key performance indicators"},
 {"k":"p","t":"Less is more here. I would anchor the executive view on a handful of KPIs tied directly to the business problem: churn rate, blended ARPU, network uptime, net promoter score, and revenue mix across voice, data, and MoMo. A dashboard that tries to show everything ends up showing nothing. Table 2 lists the core set and why each one earns its place."},
 {"k":"table","num":"Table 2.","cap":"Core executive KPIs for the MTN dashboard.",
  "headers":["KPI","What it tracks","Why it matters to executives"],
  "rows":[["Churn rate","Subscribers lost per period","Direct measure of the core problem"],
          ["Blended ARPU","Average revenue per user","Signals pricing and up-sell health"],
          ["Network uptime","Availability of the network","Leading indicator of complaints and churn"],
          ["Group NPS","Customer willingness to recommend","Early warning on loyalty"],
          ["Revenue mix","Share from voice, data, MoMo","Shows the shift to digital revenue"]],
  "widths":[1.5,2.4,2.7]},
 {"k":"h2","t":"Dashboard design and chart selection"},
 {"k":"p","t":"Good dashboard design comes down to clarity and restraint (Few, 2006). The most important number goes top-left where the eye lands first, colour is used to signal meaning rather than decoration, and clutter is stripped out. Chart choice should follow the data: trends over time as line charts, comparisons across markets as bar charts, and composition as stacked bars. Figure 3 shows a mock-up of how this comes together."},
 {"k":"fig","path":F3,"num":"Figure 3.","w":6.1,
  "cap":"Mock-up of a proposed MTN executive analytics dashboard. KPI tiles sit across the top for an instant read, with churn trend, ARPU by market, revenue mix, and a network-fault heat map below for context."},
 {"k":"h2","t":"Data storytelling"},
 {"k":"p","t":"Numbers rarely persuade on their own. Data storytelling wraps the chart in a short narrative, context, the finding, and the 'so what', so the audience leaves with a decision rather than a data dump (Knaflic, 2015). For MTN that might mean pairing the churn chart with a one-line explanation of which segment is driving it and what to do about it. Presented this way, the same dashboard that informs the board can also settle an argument in a management meeting."},

 {"k":"h1","t":"7. AI-Augmented Analytics Strategy"},
 {"k":"p","t":"Generative AI changes what an analytics function can do, though not evenly and not without risk. Used well, it takes over the slow, repetitive parts of analysis and lets scarce analysts spend their time on judgement (Davenport, 2018; Brynjolfsson et al., 2023). I want to be careful not to oversell it, so the assessment below is deliberately mixed."},
 {"k":"p","t":"For AI-assisted data analysis, a large language model can write and explain queries, letting a manager ask a question in plain English instead of waiting on a SQL specialist. Automated reporting is the most immediate win: monthly performance summaries that once took an analyst days can be drafted in minutes, with the human editing rather than writing from scratch. Insight generation is more mixed. AI is good at surfacing candidate patterns and genuinely bad at knowing which ones matter, so it needs a human in the loop."},
 {"k":"p","t":"Conversational analytics is where the value is clearest for MTN. A well-built assistant over the data platform would let an executive type 'why did churn rise in the North last month' and get a grounded, chart-backed answer. Decision support then follows: the same system can lay out options and their likely trade-offs. My honest view is that the automated-reporting and conversational use cases are ready now, while fully automated insight generation is not, and pretending otherwise sets a programme up to fail."},

 {"k":"h1","t":"8. Prompt Engineering"},
 {"k":"p","t":"The value of Generative AI depends heavily on how it is asked. Good prompts are specific about role, context, and the shape of the output wanted (Liu et al., 2023). Below are four prompts designed for different MTN objectives, each with its purpose, why it works, and the output to expect."},
 {"k":"h2","t":"Prompt 1, data exploration"},
 {"k":"p","t":"Prompt: \"You are a data analyst at MTN. Given a table of prepaid subscribers with tenure, monthly recharge, data usage, and complaint count, list the five variables most likely to predict churn and explain your reasoning for each in plain business language.\""},
 {"k":"p","t":"Objective: to get a fast, structured starting point for churn analysis. It works because it sets a clear role, names the exact fields, and constrains the output to five items with reasoning, which stops the model rambling. Expected output: a short ranked list of drivers with a business explanation for each, ready for an analyst to test."},
 {"k":"h2","t":"Prompt 2, dashboard interpretation"},
 {"k":"p","t":"Prompt: \"Acting as a business intelligence advisor, review this month's MTN dashboard summary (churn 2.1%, ARPU up 3.1%, uptime 99.2%, NPS +34). Explain in three sentences what the numbers tell an executive and flag the single metric that needs attention.\""},
 {"k":"p","t":"Objective: to translate a dashboard into a decision. It is effective because it feeds the model the actual figures and forces a tight, prioritised answer instead of a generic commentary. Expected output: a brief, plain-language read of the month with one clear priority called out."},
 {"k":"h2","t":"Prompt 3, insight generation"},
 {"k":"p","t":"Prompt: \"You are a telecom strategy consultant. Based on the finding that network faults in the North region rose 40% before a spike in complaints, suggest three testable hypotheses for the cause and the data needed to check each one.\""},
 {"k":"p","t":"Objective: to move from a pattern to something the team can act on. It works by giving the model a concrete finding and asking for hypotheses plus the evidence to test them, which keeps it grounded. Expected output: three plausible causes, each paired with the data that would confirm or rule it out. A sample response is shown in Appendix A."},
 {"k":"h2","t":"Prompt 4, strategic decision support"},
 {"k":"p","t":"Prompt: \"As an advisor to MTN's executive committee, weigh the trade-offs of investing $50m in network upgrades in one high-churn market versus spreading it across three. Consider churn, ARPU, and coverage, and recommend an option with your reasoning.\""},
 {"k":"p","t":"Objective: to support a genuine capital-allocation choice. It is effective because it frames a real decision with named constraints and demands a recommendation, not a summary. Expected output: a reasoned comparison of the two options ending in a clear, defensible recommendation the committee can debate."},

 {"k":"h1","t":"9. Ethical and Governance Considerations"},
 {"k":"p","t":"AI-enabled analytics brings real ethical weight, and for a company holding financial and location data on hundreds of millions of people the stakes are high. The concerns cluster around a few areas (Floridi & Cowls, 2019; Jobin et al., 2019)."},
 {"k":"p","t":"Data privacy comes first. MoMo and CRM data are deeply personal, and using them to train models has to respect consent and the regulations noted earlier. Data governance overlaps here: the same stewardship model that keeps data clean also keeps its use accountable. Algorithmic bias is a quieter danger. A churn or credit model trained on skewed history can quietly disadvantage a region or income group, and at MTN's scale a small bias affects millions (Mehrabi et al., 2021). This is not a hypothetical to wave away. It is the single risk I would watch most closely."},
 {"k":"p","t":"Transparency and responsible AI go together. Executives should not act on a recommendation nobody can explain, so models that drive real decisions need to be interpretable and documented. Regulatory compliance ties it all off: NDPR, POPIA, GDPR where relevant, and the financial-services rules that govern MoMo. The sensible posture is a standing AI ethics policy with human oversight on any decision that materially affects a customer."},

 {"k":"h1","t":"10. Strategic Recommendations"},
 {"k":"p","t":"Pulling the analysis together, I put forward four recommendations. Each names the action, the reason behind it, and the impact MTN should expect."},
 {"k":"p","t":"1. Build a governed central data platform. Justification: the fragmented, siloed data is the root cause of nearly every problem in this report, and no analytics effort will hold without a single trusted source (Abraham et al., 2019). Expected impact: a unified customer view, faster and more reliable analysis, and far less time wasted reconciling numbers."},
 {"k":"p","t":"2. Deploy an executive dashboard on the KPIs in Section 6. Justification: decisions are slow because leaders lack a current, shared picture of performance. Expected impact: quicker reaction to churn and network issues, and a common set of facts for the executive committee."},
 {"k":"p","t":"3. Build a churn-prediction and revenue-assurance capability. Justification: catching at-risk customers and billing leakage early is the most direct route to protecting revenue. Expected impact: lower churn, recovered leakage, and retention spend aimed where it counts."},
 {"k":"p","t":"4. Adopt Generative AI for reporting and conversational analytics, under a clear ethics policy. Justification: it frees analysts from routine reporting and puts answers within reach of non-technical leaders (Davenport, 2018). Expected impact: faster reporting cycles, wider access to insight, and AI used responsibly rather than recklessly."},

 {"k":"h1","t":"11. Conclusion"},
 {"k":"p","t":"MTN's difficulty was never a shortage of data. It was that the data never became a decision. This report traced a path from that fragmented starting point to an integrated strategy: the DIKW framework to climb from records to judgement, a governed data platform and analytical workflow to make it repeatable, an executive visualization layer, and Generative AI to speed the whole thing up. The through-line is simple. Manage the data well, show it clearly, and use AI with care, and the same information that sits idle today becomes the basis for sharper, faster, and more defensible decisions. For a company competing on thin margins across nearly 290 million subscribers, that shift is not a luxury. It is how MTN stays ahead."},

 {"k":"pagebreak"},
 {"k":"h1","t":"References"},
 {"k":"refs","items":[
  "Abraham, R., Schneider, J., & vom Brocke, J. (2019). Data governance: A conceptual framework, structured review, and research agenda. International Journal of Information Management, 49, 424-438. https://doi.org/10.1016/j.ijinfomgt.2019.07.008",
  "Ackoff, R. L. (1989). From data to wisdom. Journal of Applied Systems Analysis, 16, 3-9.",
  "Brynjolfsson, E., & McElheran, K. (2016). The rapid adoption of data-driven decision-making. American Economic Review, 106(5), 133-139. https://doi.org/10.1257/aer.p20161016",
  "Brynjolfsson, E., Li, D., & Raymond, L. R. (2023). Generative AI at work (NBER Working Paper No. 31161). National Bureau of Economic Research. https://doi.org/10.3386/w31161",
  "Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36(4), 1165-1188. https://doi.org/10.2307/41703503",
  "Davenport, T. H. (2018). From analytics to artificial intelligence. Journal of Business Analytics, 1(2), 73-80. https://doi.org/10.1080/2573234X.2018.1543535",
  "Davenport, T. H., & Harris, J. G. (2007). Competing on analytics: The new science of winning. Harvard Business School Press.",
  "Few, S. (2006). Information dashboard design: The effective visual communication of data. O'Reilly Media.",
  "Floridi, L., & Cowls, J. (2019). A unified framework of five principles for AI in society. Harvard Data Science Review, 1(1). https://doi.org/10.1162/99608f92.8cd550d1",
  "GSMA. (2023). The mobile economy Sub-Saharan Africa 2023. GSMA Intelligence.",
  "Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. Nature Machine Intelligence, 1(9), 389-399. https://doi.org/10.1038/s42256-019-0088-2",
  "Khatri, V., & Brown, C. V. (2010). Designing data governance. Communications of the ACM, 53(1), 148-152. https://doi.org/10.1145/1629175.1629210",
  "Knaflic, C. N. (2015). Storytelling with data: A data visualization guide for business professionals. Wiley.",
  "Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Computing Surveys, 55(9), 1-35. https://doi.org/10.1145/3560815",
  "Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and fairness in machine learning. ACM Computing Surveys, 54(6), 1-35. https://doi.org/10.1145/3457607",
  "Provost, F., & Fawcett, T. (2013). Data science for business: What you need to know about data mining and data-analytic thinking. O'Reilly Media.",
  "Redman, T. C. (2013). Data's credibility problem. Harvard Business Review, 91(12), 84-88.",
  "Rowley, J. (2007). The wisdom hierarchy: Representations of the DIKW hierarchy. Journal of Information Science, 33(2), 163-180. https://doi.org/10.1177/0165551506070706",
  "Sharda, R., Delen, D., & Turban, E. (2020). Analytics, data science, and artificial intelligence: Systems for decision support (11th ed.). Pearson.",
  "Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 12(4), 5-33. https://doi.org/10.1080/07421222.1996.11518099",
 ]},

 {"k":"pagebreak"},
 {"k":"h1","t":"Appendix A. Sample AI Prompt Output"},
 {"k":"p","t":"The following is an illustrative response to Prompt 3 (insight generation) from Section 8, showing the kind of grounded, testable output the proposed system would return.","size":11},
 {"k":"p","t":"Hypothesis 1: A batch of ageing cell sites in the North passed a failure threshold. Data needed: site age and hardware maintenance logs against fault timestamps.","size":11,"indent":True},
 {"k":"p","t":"Hypothesis 2: A power-supply or grid instability issue drove outages. Data needed: generator and mains power logs correlated with the fault windows.","size":11,"indent":True},
 {"k":"p","t":"Hypothesis 3: A software or configuration change was rolled out regionally just before the spike. Data needed: change-management records and deployment dates by region.","size":11,"indent":True},
]
