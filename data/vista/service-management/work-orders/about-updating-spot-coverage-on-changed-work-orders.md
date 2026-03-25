---
title: "About Updating Spot Coverage on Changed Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/about-updating-spot-coverage-on-changed-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/about-updating-spot-coverage-on-changed-work-orders"
---

# About Updating Spot Coverage on Changed Work Orders

You can make certain changes to an SM work order and have the
 spot coverage updated for existing work completed lines.
When you make changes to a work order, the system updates spot coverage for work completed as follows:

- Agreement / Call Type - If you change the agreement or call type on a
 work order scope, the system updates existing work completed lines based on the
 coverage defined for the new agreement or call type. If a work completed line was
 previously covered, but is no longer covered for the new agreement or call type, the
 Non-Billable checkbox is deselected and the billable amounts
 populated based on the scope's rate template or the agreement's rate template (if
 Agreement Rates checkbox is selected). If the work completed line
 is now covered that was not previously, the Non-Billable checkbox is selected and
 all billable amounts cleared.If you remove the agreement on a work order
 scope, any applicable work completed lines flagged as non-billable will be left as is.
 You can manually adjust those lines as needed..

- Service Site - If you are not using the auto posting feature for work
 completed (that is, you did not select the Auto Post New Work Completed
 checkbox in SM Company Parameters), you can change the service site on a work order
 and the system will update the spot coverage for existing work completed lines, as
 long as you have not yet posted them. The system will update each work completed
 line based on the coverage defined for the new service site. If standard charges
 were added to the work order for the old service site, they are removed. If standard
 charges are defined for the new service site, they will be added to the work
 order.

If you have posted any of the work completed
 lines, you will be unable to change the service site unless you delete the posted work
 completed lines.
Note: Changes made to the work order do not affect any
 work completed lines that you have already billed.
