<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=210&section=header&text=Amruth%20Shyju&fontSize=70&fontColor=ffffff&animation=twinkling&fontAlignY=34&desc=Backend%20Engineer%20%C2%B7%20Real-Time%20Systems%20%C2%B7%20Multi-Tenant%20SaaS&descAlignY=56&descSize=18&descColor=c4b5fd" alt="Amruth Shyju" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=21&duration=2600&pause=900&color=C4B5FD&center=true&vCenter=true&width=860&height=52&lines=GPS+pipelines+that+stay+fast+under+load;Tenant+isolation%2C+RBAC%2C+and+ACID+writes;Queues+and+APIs+that+fail+loudly+and+recover" alt="Focus areas" />

**I build backend systems that stay correct when traffic, tenants, and failure show up at the same time.**

Node.js · TypeScript · Redis · MongoDB · India

</div>

<br/>

## Systems

<table>
<tr>
<td width="50%" valign="top">

### [Speedo](https://github.com/AmruthAmruth/Speedo)
*Live GPS fleet analytics*

High-frequency GPS events enter a BullMQ queue, a streaming haversine pass computes distance, speed, idling, and stoppages, and Socket.IO publishes the trip while it is still moving. That streaming path cut processing latency by **70%**. A single trip carries **200+** points without blocking the API.

`Node.js` · `TypeScript` · `BullMQ` · `Redis` · `Socket.IO`

</td>
<td width="50%" valign="top">

### [Stratify](https://github.com/AmruthAmruth/Stratify)
*Multi-tenant company platform*

One backend serves company, manager, employee, and super-admin surfaces, with tenant isolation across data, sessions, and config. Clean Architecture and TSyringe keep the domain independent of the framework. Zod guards every input, RBAC gates every route, and MongoDB multi-document transactions commit related writes together.

`TypeScript` · `MongoDB` · `Zod` · `Docker` · `AWS`

</td>
</tr>
</table>

<br/>

## How the work is shaped

| Concern | What I actually do |
|---|---|
| Real-time | Ingest GPS and domain events, broadcast with Socket.IO, keep the dashboard current |
| Integrity | Redis queues with retries, concurrency limits, and MongoDB transactions |
| Boundaries | Tenant isolation, role and permission matrices, validation at the edge |
| Delivery | Docker, Nginx, AWS, and GitHub Actions so the same system ships twice |

<br/>

<div align="center">

## Activity

*The last year of public contributions. The snake crosses the calendar on a loop.*

<img width="100%" src="https://raw.githubusercontent.com/AmruthAmruth/AmruthAmruth/main/assets/contributions.svg" alt="Contribution graph" />

<br/>

<img height="180" src="https://github-stats-extended.vercel.app/api?username=AmruthAmruth&amp;show_icons=true&amp;theme=tokyonight&amp;hide_border=true&amp;bg_color=0D1117&amp;title_color=C4B5FD&amp;icon_color=A78BFA&amp;text_color=CDD6F4" alt="GitHub stats" />
&nbsp;
<img height="180" src="https://github-stats-extended.vercel.app/api/top-langs/?username=AmruthAmruth&amp;layout=compact&amp;langs_count=6&amp;hide_border=true&amp;bg_color=0D1117&amp;title_color=C4B5FD&amp;text_color=CDD6F4" alt="Top languages" />

</div>

<br/>

## Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=ts,js,nodejs,express,mongodb,redis,docker,nginx,aws,linux,react,nextjs,tailwind,git&perline=7" alt="Stack" />

</div>

<br/>

<div align="center">

## Connect

Architecture reviews, distributed-systems conversations, and backend roles.

<br/>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amruth%20Shyju-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/amruthshyju/)
&nbsp;
[![Email](https://img.shields.io/badge/Email-amruthshyju%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amruthshyju@gmail.com)

<br/>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer&animation=twinkling" alt="" />

</div>
