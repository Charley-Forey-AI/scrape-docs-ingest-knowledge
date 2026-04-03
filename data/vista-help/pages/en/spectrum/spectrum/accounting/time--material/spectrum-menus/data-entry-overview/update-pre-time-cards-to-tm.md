---
title: "Update Pre-Time Cards To T+M | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-pre-time-cards-to-tm"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/update-pre-time-cards-to-tm"
---

# Update Pre-Time Cards To T+M

This feature allows Time + Material billings to include
 labor hours before the payroll cycle is updated. Labor hours entered through Payroll > Pre-Time Card Entry can be updated into Time + Material at this point. When the check cycle is run,
 these hours will not be duplicated.
Hours for both Time + Materials and Cost Plus jobs will update. This is
 indicated by specifying Time + Material or Cost Plus, as appropriate, in the "price" method
 field of Jobs. A listing will print, detailing the information which will update. If the
 Time + Material Installation option for 'Include burden when
 adding Payroll cost-plus billings?' is selected, cost plus jobs will be updated to the Time
 + Material module by including the 'pre-time card burden' amount specified in Jobs. If this
 option is not selected, the time card extension will still be to Time + Material module,
 but the 'pre-time card burden' will not be included in this amount.
If this is a sub-job billed from a master job, the software will read
 for job-specific setup rates for the master job, and if none are found use standard
 settings. If this is a sub-job billed at the sub-job level, the software will read for
 job-specific setup rates for the sub-job first, and if billing rates are not found then the
 master job, and if none are found there use standard settings.
If the 'Post to Job Cost using standard labor rates' option is selected
 on the Payroll Installation screen, standard costs will update to
 T+M for cost-plus jobs and display on the Detail Billing Selection
 screen.
Time cards currently being routed for Workflow approval will be omitted
 from the update.
Important: Once these Pre-Time Card Entry hours are updated
 to Time + Material, no payroll changes will be allowed; additional time card lines will be
 required to make modifications.

Related information

- [Calculate Markups Based on Pay Type](/en/spectrum/spectrum/accounting/time--material/procedures-overview/in-depth-overview/calculate-markups-based-on-pay-type)
