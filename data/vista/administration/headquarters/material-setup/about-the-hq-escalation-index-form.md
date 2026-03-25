---
title: "About the HQ Escalation Index Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form"
---

# About the HQ Escalation Index Form

Use this form to set up state-defined indexes for oil price escalation/de-escalation.
Price indexes are used to track
 pricing fluctuations for the oil component of asphalt mixes over
 the life of a contract/job, thus helping to minimize cost risks.
Price indexes are set up by country and
 state and are not company-specific; therefore, if the same index applies to multiple
 companies, you must set up the finish material/component material combination as
 applicable for each company’s assigned material group (Material tab).
Note: The MS Oil Price Setup report provides an easy way
 to review the material setup for pricing indexes by state.
Once set up here, price indexes are applied to state
 jobs/projects (via JC Jobs, PM Projects, or MS Quotes) or
 customer jobs (MS Quotes) to track monthly increases/decreases
 in pricing. Using the MS Oil Price Escalation report, you can
 compare system data with state-supplied documents (e.g. change
 orders) to identify amounts owed to, or from, the state.
Note: In order to use this feature, you must set up a bill
 of materials (in IN Bill of Materials or IN Bill of Materials Override) for each
 finished good. Although a bill of materials will typically include all components that
 make up the finished material, for this feature, you are only required to include the
 oil component being escalated/de-escalated.
The Monthly Index tab allows you to set up the state-defined escalation pricing
 for the component material (e.g. the virgin oil used in the asphalt mix). You specify the date ranges to which pricing
 applies (e.g. weekly, monthly, etc.), the state-defined English/Metric prices and
 pricing factor (i.e. how much pricing must increase/decrease before an adjustment is
 applied), and the minimum days/amounts.
The Material tab allows you to set up the materials to which time-based
 escalation applies; that is, the finished good material (representing the mix design
 formula) and the component material (to which price escalation applies). A material/component combination may be set
 up multiple times for a single country/state/index (i.e. multiple companies use the same
 index), as long as the material group differs.
Note: You can also use HQ Materials
 (Escalation Price Index tab) to assign pricing indexes to applicable materials. For
 more information, see HQ Materials in Related Topics below.

[How the System Uses Pricing Indexes](/en/vista/vista/administration/headquarters/material-setup/how-the-system-uses-pricing-indexes#concept-7160--en__concept-7160)
[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)HQ Materials
[](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-jobs-form)JC Jobs
[](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form)PM Projects
[](/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quotes-form)MS Quotes
[](/en/vista/vista/job-resources/inventory/production/about-the-in-bill-of-materials-form)IN Bill of
 Materials
[](/en/vista/vista/job-resources/inventory/production/about-the-in-bill-of-materials-override-form)IN Bill of
 Materials Override
