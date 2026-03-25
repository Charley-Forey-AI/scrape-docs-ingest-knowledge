---
title: "About Service Timecards | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-service-timecards"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/about-service-timecards"
---

# About Service Timecards

Service timecards allow you to capture the labor hours for technicians performing service work and update the costs to the service work order (in SM).
You can [enter timecards for SM work orders](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/entering-sm-work-order-timecards) directly in the PR
 Timecard Entry form. Once you save a timecard line, the system generates a corresponding
 work completed labor entry in SM Work Orders (Work Completed tab). If you enter
 equipment usage with a service timecard line (customer work orders only), the system
 will also generate a work completed equipment line for the work order. Any changes made
 to an existing timecard will update the corresponding work completed record(s) in
 SM.
Note: Work completed equipment lines generated from a timecard
 cannot be edited in SM; all edits must be handled via PR Timecard Entry. The system will
 update the work completed equipment line accordingly.
Labor hours entered for work orders in SM Work
 Orders will not add or update timecard records; instead, they will add or update
 timesheet records (in PR My Timesheet), which you must then approve and send to a
 timecard batch. However, this functionality is only available if you selected the
 PR interface checkbox in SM Company Parameters. Otherwise, you will
 need to manually enter and update timecards or timesheets in PR to capture labor hours
 for SM work orders.
Equipment usage entered for work orders in SM Work Orders will not add or update timecard (or timesheet) records. Revenue updates to EM will be handled for these entries directly in SM.
Note: For Australian and Canadian companies: Entry of time to a
 non-job SM work order will automatically set the Tax
 Type to 3-VAT for the work completed labor line in SM Work Orders.
 The tax code for the work completed line will default from the Service Center or
 Service Site (depending on the Tax Source specified for the work order) and must be
 a VAT-type code. For this function to work, the SM company's AR company (defined in
 SM Company Parameters) must be set up with a Default Country of AU or CA in HQ
 Company Setup.
