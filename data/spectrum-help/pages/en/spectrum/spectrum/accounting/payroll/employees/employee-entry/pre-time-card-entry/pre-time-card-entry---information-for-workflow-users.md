---
title: "Pre-Time Card Entry - Information for Workflow users | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/pre-time-card-entry/pre-time-card-entry---information-for-workflow-users"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-entry/pre-time-card-entry/pre-time-card-entry---information-for-workflow-users"
---

# Pre-Time Card Entry - Information for Workflow users

The Pre-Time Card Entry screen can be used to enter
 detailed time cards outside of the defined payroll cycle.

- If you have the Workflow module serialized and the Time Card Approval Workflow
 is 'Active', when you add a new pre-time card, the corresponding Workflow (job or
 employee) will begin automatically. Exception: void checks are never routed for
 approval.

- If you have no assigned supervisor or job contact, the Workflow will still exist but will not show up in the Dashboard App or 'Time Card Approval' for any standard 'Reviewer'. Instead, these Workflows will need to be handled by an Override Operator.

- When editing records, any changes made to the Job or Phase or Work date will result in the time card moving to another Workflow.

- You will not be allowed to make changes to records that have already been approved. Editing a time card line is not allowed once any one of the reviewers has signed off. In order to correct an error once approval has been granted, it will be necessary to 'delete-and-add' a time card to make the correction. Deletions are allowed while any Workflow is 'In Review' or 'Rejected'. However, if the 'Allow override operator to modify approved time cards' option was selected in the Time Card Approval Workflow, approved time cards can be edited or deleted if the current user is an override operator.

- The Pre-Time Card import and error correction, the Work Order labor transfer, and the reverse pre-time card update also automatically place all new pre-time cards into Workflows.

- The update to transfer pre-time cards to the pay cycle will SKIP all pre-time cards that are still in open Workflows (that is, 'unapproved'), unless performed by an Override Operator.
