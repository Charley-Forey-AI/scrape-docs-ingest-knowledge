---
title: "JC Detail Roll-up Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-detail-roll-up-codes-form"
---

# JC Detail Roll-up Codes Form

Use this form to set up specifications that control how you want job costs and contract revenue rolled up (summarized) in your Job Cost files.
Rolling up revenue and/or cost detail allows you to control the amount of disk space the system uses to store contract and/or job data. You may want to consider rolling up monthly detail once you have run all monthly reports (showing the revenue and cost detail you need for the month) and have closed the month in all subledgers.
Roll-ups summarize a series of related detail entries into a single summary record. For each roll-up code, you must specify to what level you want the cost or revenue detail rolled up. There are three levels available:

- Month – This level leaves one record per month, per phase/cost type.

- Month/Source – This level leaves one record per month, per phase/cost type, per source.

- Month/Source/Detail – This level is only available for 'cost' roll-ups, and summarizes as follows:

AP = One record per vendor
EM = One record per equipment
MS = One record per material
IN = One record per material
PR = One record per payroll date
JC = Compress only those transactions with nothing but units (e.g. transactions created in JC Progress Entry). All other JC transactions will not be compressed.

The source section allows you to specify the sources
 from which cost or revenue detail will be pulled during the roll-up process. Sources
 include AP, AR, EM, IN, JC, MS, and PR. If you elected to summarize detail at the
 'month' level, sources are not applicable and therefore, will be disabled. If you
 elected to summarize detail at the 'month/source' level, available sources will depend
 on the type of roll-up. For cost roll-ups, all sources are available. For revenue
 roll-ups, only AR and JC sources are available. If you elected to summarize detail at
 the 'month/source/detail' level (cost roll-ups only), all sources except for AR and JC
 are available.
Note: You can quickly select all available sources for a roll-up by clicking the Select All button. If you want to set all selected sources to N (unchecked), click the Clear All button.
The Last Month Offset controls the number of months prior to the last month closed in subledgers through which detail will be rolled up. For example, if you specify an offset of '12', and the last month closed in subledgers is 04/03, detail will be rolled up through 04/02.
Once you have set up all the necessary roll-up codes your company will use, you can then use them to initiate the actual roll-up process (in JC Detail Roll-Up).
