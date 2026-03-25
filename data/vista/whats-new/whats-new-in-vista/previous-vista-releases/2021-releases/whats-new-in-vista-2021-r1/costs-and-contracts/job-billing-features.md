---
title: "Job Billing Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-billing-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-billing-features"
---

# Job Billing Features

Vista 2021 R1 delivers on user-requested Job Billing enhancements, fixes, and other improvements.

## Ability to Refresh Job Cost Detail for an Entire Billing

You can now refresh Job Cost detail for an entire T&M billing to add cost detail that was previously deleted or posted after a billing was created.
 From the JB T&M Bill All JCDetail Lines form (accessed from JB T&M Bill Edit by selecting File > Job Cost Detail), you can now access the JB T&M JC Detail Fill Grid form (added in a previous release) by clicking Refresh Cost Detail. You can then enter criteria (date range, cutoff month, labor cutoff date, etc.) to filter the cost detail you want to add.
 Once you click Fill Grid, the system adds the JC Detail for all lines and sequences (not already on the billing) that meet the specified criteria. Clicking Refresh at the bill header updates all applicable totals to include the additional lines.
For more information, see [Add JC Cost Detail to a T&M Billing](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/add-jc-cost-detail-to-a-tm-billing).

## Support Separate T&M Bills for Customer POs with Approved Ticketed Costs

In conjunction with the new Separate Inv checkbox added to the Customer POs tab on the JC Contract Master form, the bill initialization process (in JB Bill Initialization) will now create a separate billing for each customer PO flagged for separate invoicing.
During the initialization process, if a customer PO is flagged for separate invoicing, the system creates a separate billing for that customer PO and groups all approved field ticket costs associated with the customer PO on the same billing.
For customer POs not flagged for separate invoicing, the system adds all approved field ticket costs associated with the customer PO to the same billing created for other non-ticketed costs on the contract.
For information about the new checkbox, see the [Job Cost](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/costs-and-contracts/job-cost-features) release notes

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
