---
title: "Bill Flag | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/quantity-information/bill-flag"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/quantity-information/bill-flag"
---

# Bill Flag

Each cost type associated with a phase is assigned a unit of measure and a quantity (if the unit of measure is not lump sum).
The unit of measure may be the same for all cost types or different for each cost type. In addition, there may be several phases pointing to the same contract item. Contract items (pay items) also have a unit of measure to which they are associated, as well as a quantity. All costs and progress on a job are accumulated at the phase/cost type level; however, job costs may be reported at many different levels: cost type, phase, job, contract item, or contract. When reporting anything that has been summarized more than at the cost type level, it makes sense to add all the dollars to get the totals, but it is probably not logical to add all of the units. They may not be in the same unit of measure, and even if they are, it would most likely result in duplicate counting of the same units.
The bill flag may be used to define which cost type’s units are to be totaled when summarizing information for determining progress complete in Job Billing Progress invoices. The standard programs in the accounting modules use the bill flag in the following instances:

- Progress Worksheets (Job Billing) — If you are using the option to include actual costs, the worksheet will display a line of units and a line of dollars. The Units line will total all units with a bill flag of Y for each phase and cost type linked to the contract item, regardless of the unit of measure. The dollars line will include all phases and cost types with either a Y or C flag setting. If the bill flag is N, neither units nor dollars will be included in the totals.

- Initialize Progress Invoices (Job Billing) — When initializing progress invoices with a lump sum unit of measure, the program calculates percent complete based on cost dollars to estimated or projected dollars only, using costs flagged Y or C. If not lump sum, the progress will be based on percent of units complete, totaling only the units with a bill flag of Y.

Note that these refer to progress billings in Job Billing only. The bill flag has no affect on whether costs will be included on T & M billings. That is determined by the setup of the T& M templates.
