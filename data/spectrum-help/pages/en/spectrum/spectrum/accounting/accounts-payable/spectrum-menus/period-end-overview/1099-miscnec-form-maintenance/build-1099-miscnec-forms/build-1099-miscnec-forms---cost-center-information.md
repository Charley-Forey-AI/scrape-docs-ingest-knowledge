---
title: "Build 1099-MISC/NEC Forms - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/1099-miscnec-form-maintenance/build-1099-miscnec-forms/build-1099-miscnec-forms---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/1099-miscnec-form-maintenance/build-1099-miscnec-forms/build-1099-miscnec-forms---cost-center-information"
---

# Build 1099-MISC/NEC Forms - Cost Center Information

If cost centers are being used, the Build 1099-MISC/NEC Forms process operates in a specific way.
When performing the Build 1099-MISC/NEC Forms process, Spectrum will complete the vendor 1099 update only if you have permission to access all vendors included in the starting screen selection. Spectrum compares each vendor's list of shared cost centers with cost centers in your assigned cost center scheme, and if there are no common cost centers, then the 1099 form update is not performed.
If cost center entities are being used, this update will allocate vendor payments onto separate 1099-MISC/NEC Forms based on 'Entity code' stored for the 'check cost center' assigned to the vendor payment. Specifically, the software will read the assigned cost center of each vendor payment in the A/P Payment History Table, and then determine whether that cost center has an assigned entity with an Accounts Payable 'Tax ID number' in order to build the 1099-MISC/NEC Forms by Entity. The software will apply the 'minimum amount' separately when determining whether to generate a 1099 to the vendor for the particular entity.
