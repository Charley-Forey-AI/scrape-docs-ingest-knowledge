---
title: "Initial Setup for Compliance Tracking | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/initial-setup-for-compliance-tracking"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/initial-setup-for-compliance-tracking"
---

# Initial Setup for Compliance Tracking

An overview of the initial setup required for tracking vendor compliance.
During the course of setting up Compliance tracking, you will take action across several modules: Headquarters, Project Management, Subcontract Ledger, Purchase Orders, and Accounts Payable.
There are several setup options required for tracking compliance:

- HQ Compliance Codes form - You must set up the compliance codes that you are interested in tracking. If you want warnings or prevention from payment in invoicing and payments, select the Verify checkbox.

- HQ Compliance Groups form - Set up groups that may relate to different types of jobs and the compliance codes that would apply to those jobs. For example, compliance codes on federal projects might be different than those on commercial projects. The same code may be used in multiple groups.

In AP Company Parameters, there are four checkboxes that determine how verification works:
Subcontracts

- Check compliance on transaction entry, warning only. This option provides warnings in the SL Worksheet and AP Transaction Entry forms if a subcontract has any codes that are not in compliance.

- Don’t add to Payments batch if “out of compliance”. If you select this option, any invoices posted to subcontracts that have codes out of compliance are not initialized into an AP payment batch. However, out-of-compliance transactions may be added to a batch manually in the AP Payments Posting form.

Purchase Orders

- Check compliance on transaction entry, warning only. This option provides warnings in the AP Transaction Entry form if a purchase order has any codes that are not in compliance.

- Don’t add to Payments batch if “out of compliance”. If you select this option, any invoices posted to purchase orders that have codes out of compliance are not initialized into an AP payment batch. However, out-of-compliance transactions may be added to a batch manually in the AP Payments Posting form.

If you are using the Project Management module, you can also initialize compliance by assigning compliance groups to projects (in the PM Projects form). When you initialize a subcontract or purchase order, the system assigns the compliance group to the SL or PO header, and sets up the associated compliance codes in the SL Compliance Tracking form. You may also manually assign compliance groups to subcontract and purchase order headers.
If you are not using the Project Management module, you can enter the compliance group in the header when adding subcontracts in the SL Entry form or purchase orders in the PO Entry form. As the batch is posted, the codes associated with the group are added to compliance tracking in both modules. Codes may be individually added or deleted in either the SL Compliance or PO Compliance form.
Note: Changing a subcontract or purchase order's compliance group automatically updates its compliance codes. The system retains all original codes and adds any unique codes from the new group. If you manually deleted codes prior to changing the compliance group and they exist for the new compliance group, they will be re-added. You can manually delete them again if needed..

Related concepts

- [About Compliance Tracking Setup for Non PO/SL Invoices](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking/about-vendor-compliance-for-non-posl-invoices/about-compliance-tracking-setup-for-non-posl-invoices)

- [Vendor Compliance Tracking](/en/vista/vista/accounting/accounts-payable/vendors/vendor-compliance-tracking)
