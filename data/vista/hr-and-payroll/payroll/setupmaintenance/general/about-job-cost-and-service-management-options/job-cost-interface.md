---
title: "Job Cost Interface | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-job-cost-and-service-management-options/job-cost-interface"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-job-cost-and-service-management-options/job-cost-interface"
---

# Job Cost Interface

You can control Job Cost interfacing and define certain settings
 for timecards and liability distributions using the Job Cost/Service Mgmt tab in PR Company Parameters.
If you want to interface PR to JC, select the
 Interface
 Labor/Equipment/SM Work Order Costs to JC and Revenue to EM checkbox. You can
 decide what detail you want interfaced to JC using the Include in JC Detail section at
 the bottom of the form. These detail options control how much and what type of timecard
 detail is interfaced to JC. These options are generally determined by a company's Job Billing requirements.
 Three types costs are updated to Job Cost: Labor (representing
 all posted and add-on earnings and hours), Burden (representing the liabilities
 associated with those earnings), and Usage (representing the costs to a job related to
 equipment use).
The Craft/Class, Crew, Employee, and Use Posting
 Date options apply to all three types of job costs. However, there are options specific
 to each of the job cost types:

- Labor – Options provided allow you to break out earnings by Earnings
 Type, Earnings Factor, and Shift, depending on how you bill out costs.

- Burden – Options are provided to allow breaking down the liability costs
 associated with earnings (e.g. taxes, insurance, etc.) by Liability Type, Earnings
 Factor, and Shift.

Note: Earnings Factor and Shift options are only
 available if breaking down by Liability Type.

- Usage – Options are providing for breaking out equipment costs by
 Equipment and Revenue Code.

All payroll information updated to JoC is
 distributed by pay period, month, JC company, job, phase, and cost type, but if one of
 the above options is checked, then the entries created in the JC Cost Detail file will
 also include the corresponding detail information. For example, if you check the
 Use Timecard
 Date Instead of Pay Period Ending Date box, then entries will be created
 in JC Cost Detail for each day worked instead of a single entry for the pay period. If
 the Employee box is checked, then separate entries will be added to JC Cost
 Detail for each employee instead of a summarized entry for all employees. Burden will be
 included with labor costs unless the Liability Type box is checked. If you
 post equipment usage, you typically will want to check the Equipment
 and Revenue
 Code boxes to interface detail to JC.
