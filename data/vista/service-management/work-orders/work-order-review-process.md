---
title: "Work Order Review Process | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/work-order-review-process"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/work-order-review-process"
---

# Work Order Review Process

The work order review process enforces a mandatory review and approval process for all work orders before they can proceed to the billing stage.

You can enable this process by selecting the Use Review Process checkbox in SM Company Parameters. Once selected, assigned reviewers must review work orders and flag them as 'ready to bill' before you can bill them.
Note: If you do not select the Use Review Process checkbox, the review and approval process becomes optional. This means that you can review/approve work orders as needed, but review/approval is not required to bill work orders.

## Assigning Reviewers

In order for work order reviews to occur, you must assign at least one reviewer to the work order or one of the following places related to the work order:

- Service Site

- Customer

- Division

- Service Center

Reviewers assigned at the work order level are primary reviewers. Reviewers assigned at the other levels are alternate reviewers. However, if you do not assign a reviewer at the work order level, the system searches for a reviewer at the other levels (in the order shown above). The first reviewer found becomes the primary reviewer, and any others become alternate reviewers.

## Review and Approval

When the review process is active, work orders must be reviewed and approved (that is, flagged as 'ready to bill') before you can bill them. Only the primary or alternate reviewer can select the Ready to Bill checkbox for the work order and its scopes. For more information, see [About the Ready To Bill Flag](/en/vista/vista/service-management/work-orders/work-order-review-process/about-the-ready-to-bill-flag).
Note: There is no automatic notification process to alert reviewers of work orders needing review. However, reviewers can search for work orders awaiting their review in SM Work Orders using the Ready to Review and Reviewer filters in the Search panel. For more information, see [Search Work Orders](/en/vista/vista/service-management/work-orders/search-work-orders).

If the Ready to Bill checkbox is not selected for a work order or work order scope, the Bill WO button is disabled in SM Work Orders (for all users except the reviewer). If you bill work orders using the SM Work Order Billing form, the work order will not display in the Work Orders grid.
Note: If you add billable lines to a work order scope already marked as 'ready to bill', the system deselects the Ready to Bill checkbox, requiring the work order to go through the review/approval process again. However, adding non-billable costs to a scope does not affect the Ready To Bill checkbox.
.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
