---
title: "Update Labor Billing Rates - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/utilities-overview/update-labor-billing-rates/update-labor-billing-rates---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/utilities-overview/update-labor-billing-rates/update-labor-billing-rates---cost-center-information"
---

# Update Labor Billing Rates - Cost Center Information

If the cost center feature is enabled in the Enterprise
 Installation screen for this company, a Cost
 group field displays beneath the Contract field.
This field filters records in the customer-specific, site specific, and
 contract-specific billing rates tables when cost centers are enabled for the current
 company.
If cost centers are set to Yes in the current company, the software will only adjust rates for records that the operator is authorized to access in the Maintenance menu. There are no cost center restrictions for standard rates.

- For customer-specific rates, the operator must have security
 access to the customer. Spectrum compares the customer's list of shared cost centers
 with the cost centers in the operator's assigned scheme; if there are no common cost
 centers, then that customer-specific labor billing record is not updated.

- For site-specific rates, the operator must have security access
 to the site. Spectrum compares the site's assigned cost center with the cost centers
 in the operator's assigned scheme; if the cost center is not included, then that
 site-specific labor billing record is not updated.

- For contract-specific rates, the operator must have security
 access to the contract. Spectrum compares the cost center assigned to the contract
 with the operator's assigned cost center scheme; if the cost center is not included,
 then that contract is not updated.
