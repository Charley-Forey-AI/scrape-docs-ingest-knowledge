---
title: "Enable Billing for Work Completed in Job Billing | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders/enable-billing-for-work-completed-in-job-billing"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-billing-sm-job-work-orders/enable-billing-for-work-completed-in-job-billing"
---

# Enable Billing for Work Completed in Job Billing

You can bill for work completed on a job-related SM work order
 using the Job Billing module.
The Job Billing module allows you to create billings
 manually or by initialization. It is generally easier and more efficient to initialize
 billings for work completed; however, you can manually enter billings in JB T&M Bill
 Edit. If you elect to use manual entry, you must associate bill lines with the
 appropriate cost detail using JB T&M Bill JCDetail by Seq.If you elect to use
 initialization to generate invoices for job-related SM work orders, you must
 complete the following setup requirements to ensure proper billing.

1. In JB T&M Template Setup:

1. For each template that you will assign to jobs associated with SM work
 orders, include all the sources that update Job Cost for work completed
 (see table below for an example).Seq
 #
Type
Desc
AP
EM
IN
JC
MS
PR
Sum
 Opt
Sort
 Level

10
S-Source
AP
X

1
1

20
S-Source
EM

X

1
1

30
S-Source
IN/JC/MS

X
X
X

1
1

40
S-Source
PR

X
1
1

1. For each applicable source on a template, set up all cost types that
 you will use on job-related SM work orders.

1. In JC Contracts, assign a Bill Type of T&M (preferred) or
 Both to all
 contract items that are associated with SM work orders (via jobs/phases). Since work completed entries are handled
 on a T&M basis in SM Work Orders, you can only generate T&M billings for
 them in Job Billing.

1. In JC Jobs, assign a T&M template to each job
 that will be associated with SM work orders.When you initialize billings in JB
 T&M Bill Initialization, the system looks to the job to determine the
 template to use when creating billings for that job.

Use SM Work Orders to enter work completed for job work
 orders. Once you update work completed costs to Job Cost, use JB Bill Initialize to
 generate T&M billings based on the cost detail from the JC Cost Detail table (JCCD).
 To ensure you pull all eligible work completed costs, you will need to select one of the
 following initialize options (from the Initialize Option drop-down):

- T-T&M (T) Items only — Select this option to pull costs for contract items
 with a Bill Type of T&M.

- B-Progress (P) and Both (B) Items – Initialize (B) Items as T&M — Select
 this option to pull costs for contract items with a Bill
 Type of Both.
