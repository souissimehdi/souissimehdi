<!-- ============================  HEADER  ============================ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:6DB33F,50:1B5E20,100:0D1117&text=Mohamed%20Mehdi%20Souissi&fontColor=ffffff&fontSize=46&fontAlignY=36&desc=Java%20%2F%20Spring%20Backend%20Expert%20%E2%80%A2%2014%2B%20years%20%E2%80%A2%20Generative%20AI%20explorer&descAlignY=58&descSize=17&animation=fadeIn" alt="header"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=21&duration=3000&pause=900&color=6DB33F&center=true&vCenter=true&width=700&lines=14%2B+years+of+Java+%26+Spring+backend+%E2%98%95;Microservices+%E2%80%A2+Kafka+%E2%80%A2+Event-driven+architecture+%E2%9A%A1;Distributed+systems+that+scale+%F0%9F%8C%90;Now+teaching+Spring+apps+to+think+%E2%80%94+LLMs%2C+RAG%2C+MCP+%F0%9F%A4%96" alt="typing intro"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Oracle_Certified-Java_SE_11_Developer-F80000?style=for-the-badge&logo=oracle&logoColor=white"/>
  <a href="https://www.linkedin.com/in/souissimedmehdi/"><img src="https://img.shields.io/badge/LinkedIn-souissimedmehdi-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:souissimedmehdi@yahoo.fr"><img src="https://img.shields.io/badge/Contact_me-6001D2?style=for-the-badge&logo=yahoo&logoColor=white"/></a>
</p>

---

## ☕ `new MohamedMehdiSouissi()`

```java
@Service
public class MohamedMehdiSouissi implements BackendEngineer, Architect, LifelongLearner {

    private final int yearsOfExperience = 14;   // and counting
    private final String certification  = "Oracle Certified Professional, Java SE 11 Developer";

    private final List<String> expertIn = List.of(
        "Java & the Spring ecosystem",
        "Microservices & distributed systems",
        "Event-driven architecture with Apache Kafka",
        "SQL / NoSQL data modeling",
        "AWS & serverless",
        "Technical leadership & code reviews");

    private final List<String> speaks = List.of(
        "Arabic (native)", "French (advanced)", "English (advanced)", "Java (fluent 😄)");

    @Scheduled(cron = "0 0 20 * * *")   // evenings & weekends
    void learnGenerativeAI() {
        explore("LLMs", "RAG", "MCP", "AI Agents");
        build("github.com/souissimehdi/spring-ia");
    }
}
```

---

## 🧠 How my GitHub works (a RAG pipeline, obviously)

```mermaid
flowchart TB
    subgraph S1 ["🔎 Retrieve"]
        direction LR
        Q([💡 New idea]) --> K{⚡ Semantic cache:<br/>solved something<br/>similar before?}
        K -->|hit| H([♻️ Reuse it,<br/>zero tokens])
        K -->|miss| T[🌍 Translate to<br/>Java & Spring] --> R[(🗄️ Vector store of<br/>14+ years of backend)] -->|top-k patterns:<br/>microservices · Kafka · AWS| P[🛡️ Filter out<br/>over-engineering]
    end
    subgraph S2 ["✨ Generate"]
        direction LR
        A[🧩 Augment with<br/>Spring AI docs] --> G[🤖 Generate code<br/>with Claude] --> C([✅ git push]) -. chat memory +<br/>semantic cache .-> M[(🧠 New experience<br/>back into the store)]
    end
    S1 --> S2
```

---

## 🎯 Areas of expertise

<table>
<tr>
<td width="50%" valign="top">

### ☕ Java & Spring
Modern Java (21) and the whole Spring ecosystem: Boot, Data JPA, Security, Batch,
Integration, MVC. Clean, testable and maintainable backend code.

### 🧩 Microservices & distributed systems
Domain-oriented microservices, shared domain models, configurable processes,
resilience and consistency across services.

### ⚡ Event-driven architecture
Asynchronous communication and distributed processing with **Apache Kafka**,
plus ActiveMQ, Mule ESB and Apache Camel integrations.

</td>
<td width="50%" valign="top">

### 🗄️ Data, SQL & NoSQL
PostgreSQL, MongoDB, Redis, Cassandra, Elasticsearch, MySQL, SQL Server.
Choosing the right store for each job.

### ☁️ AWS & serverless
S3, Lambda, Step Functions, the AWS SDK, and now **Bedrock** for generative AI.

### 🧭 Technical leadership
Architecture and design decisions, code reviews, mentoring, Agile/Scrum
ceremonies, estimation and Git flow strategy.

</td>
</tr>
</table>

---

## 🤖 Side quest: Generative AI with Spring

<table>
<tr>
<td width="60%" valign="top">

### 🌱 [spring-ia](https://github.com/souissimehdi/spring-ia)

**Spring Boot 4 + Spring AI 2** talking to **Anthropic Claude on AWS Bedrock**, grown
commit by commit from a hello-world endpoint into a full RAG stack with semantic caching:

- 💬 `ChatClient`, prompt templates, advisors, streaming
- 🧱 Structured output → records, lists, maps
- 🧠 Per-user chat memory persisted with JDBC
- 📚 RAG: **Tika → chunking → Titan embeddings → Qdrant**
- 🌐 Web-search RAG with **Tavily**
- 🛡️ Query translation and **PII masking**
- ⚡ **Semantic caching**: similar questions are answered from the cache, with no LLM call (Redis, then Qdrant)

</td>
<td width="40%" valign="top">

```text
   question
      │
      ▼
 ┌───────────┐  hit
 │  cache?   │─────▶ cached answer
 └─────┬─────┘ miss
       ▼
 ┌───────────┐
 │ translate │ pre-retrieval
 └─────┬─────┘
       ▼
 ┌───────────┐
 │  Qdrant   │ top-k chunks
 └─────┬─────┘
       ▼
 ┌───────────┐
 │ mask PII  │ post-retrieval
 └─────┬─────┘
       ▼
 ┌───────────┐
 │  Claude   │ grounded answer
 └───────────┘
```

</td>
</tr>
</table>

```diff
+ ✅ ChatClient · prompts · advisors · structured output
+ ✅ Chat memory (JDBC)
+ ✅ RAG with Qdrant · advanced RAG (pre/post-retrieval, web search)
+ ✅ Semantic caching — Redis, then Qdrant
! 🔄 Tool calling — letting LLMs call Java methods
! 🔄 Model Context Protocol (MCP) — clients & servers
- ⏳ AI evaluators · observability (Prometheus, Grafana, OpenTelemetry)
- ⏳ A real-world AI agent
```

---

## 🛠️ Tech stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,spring,kafka,aws,postgres,mongodb,redis,cassandra,elasticsearch,mysql&theme=dark" alt="tech icons 1"/>
  <br/>
  <img src="https://skillicons.dev/icons?i=docker,maven,gradle,jenkins,git,idea,eclipse,postman,python&theme=dark" alt="tech icons 2"/>
</p>

| Domain | Technologies |
|---|---|
| **Backend** | Java 21 · Spring Boot 4 · Spring Framework 6 · Spring Data JPA · Spring Security · Spring Batch · Spring Integration |
| **Architecture** | Microservices · Distributed systems · Event-driven architecture · Design patterns |
| **Messaging** | Apache Kafka · ActiveMQ · Zookeeper · Mule ESB · Apache Camel |
| **Data** | PostgreSQL · MongoDB · Redis · Cassandra · Elasticsearch · MySQL · SQL Server |
| **Cloud** | AWS S3 · Lambda · Step Functions · Bedrock · AWS SDK |
| **Generative AI** | Spring AI · Claude · RAG · Qdrant · embeddings · semantic caching · MCP |
| **Workflow / BPM** | Camunda · BPMN 2.0 · Quartz Scheduler |
| **Quality & DevOps** | JUnit · Selenium · SonarQube · Jenkins · Docker · Git flow |

---

## 📊 GitHub stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=souissimehdi&show_icons=true&theme=github_dark&hide_border=true&title_color=6DB33F&icon_color=6DB33F&include_all_commits=true" alt="stats"/>
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=souissimehdi&layout=compact&theme=github_dark&hide_border=true&title_color=6DB33F" alt="top languages"/>
</p>

---

<p align="center">
  <code>while (curious) { learn(); build(); share(); git push; }</code>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=110&color=0:0D1117,50:1B5E20,100:6DB33F&section=footer" alt="footer"/>
</p>
