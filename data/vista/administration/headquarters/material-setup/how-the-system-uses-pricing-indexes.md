---
title: "How the System Uses Pricing Indexes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/how-the-system-uses-pricing-indexes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/how-the-system-uses-pricing-indexes"
---

# How the System Uses Pricing Indexes

Once you have set up pricing indexes for each applicable
 state in the HQ Escalation Index form, you will need to activate pricing escalation for each applicable job or customer
 job.
This is
 done by checking the Apply Price Escalators box in JC Jobs (jobs), PM Projects
 (projects), or MS Quotes (jobs, customer jobs). In addition, you will need to make sure
 the finished material and the component material are set up on a bill of materials (in
 IN Bill of Materials or IN Bill of Materials Override).
When the finished material is sold to a job
 or customer job (via MS Ticket Entry), the MS Oil Price Escalation report determines
 pricing fluctuations based on the following:

- Bid Index – This is the monthly index entry (in
 HQ Escalation Index, Monthly Index tab) used as the 'starting point' for price
 escalation. You must have a Bid Index defined for each applicable job or
 customer job, based on the job or customer job's 'bid index date'. The bid index
 date will be either the Bid Index Date specified in MS Quotes (jobs or customer
 jobs) or the contract start month from JC Contracts/PM Projects (jobs, when no
 quote exists). For example, if you set up a quote for a job with a Bid Index
 Date of 01/15/09, you must also set up a monthly index entry that includes
 01/15/09 in the From/End Date range (e.g. 01/01/09 - 01/31/09).

- Bid Index Amount – This is the price
 (English and Metric) specified for the Bid Index month.

- Sale Date – This is the sale date
 specified in MS Ticket Entry. The system uses this date as the ‘place date’ (the
 date material was placed on the job), which is then used to determine the place
 index to use.

- Place Index – The additional monthly
 indexes—defined by each state—added each month (e.g., if the job start month is
 1/1/09, all monthly indexes set up after 1/09 will become that job’s placing
 indexes.). These are accumulative starting with the bid index.

- Place Index Amount – This is the
 price (English and Metric) specified for the Place Index month.

When you run the MS Oil Price Escalation
 report, it compares the current month’s index amount (place index amount) with the bid
 index amount and calculates the difference (increase or decrease). If the amount
 increases/decreases by the factor (specified for the bid index), the adjustment is shown
 on the report. For example, say the factor is 5%, the bid index amount is $632.00, and
 the current month’s index is $648.00, a difference of -16.00. Since the difference is
 less than 5% of the bid index amount (632.00 x .05 = 31.60), the adjustment would not be
 applied. If however, the current month’s index were $668.00, the adjustment (36.00)
 would be more than 5% of the bid index amount and would therefore be shown on the
 report.
