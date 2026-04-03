---
title: "Transaction Entry by Accounts Payable - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/transaction-entry-by-accounts-payable---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/transaction-entry-by-accounts-payable---cost-center-information"
---

# Transaction Entry by Accounts Payable - Cost Center Information

For Accounts Payable transaction type entries, Spectrum
 allows you to add a transaction for a vendor only if your operator has permission to access
 that vendor.
The system compares the vendor's list of shared cost centers with cost centers in your
 operator's assigned cost center scheme, and if there are no common cost centers, then
 transaction entry for that vendor will be disallowed. The system then validates entry of
 the equipment code and cost category to assure that your operator has authorization for the
 transaction. The cost center assigned to the credit portion of the entry may be entered,
 but must be a cost center that is valid for that vendor.
For cost transaction types, Spectrum displays cost centers for the debit and credit portions of the transaction entry. The cost center assigned to the debit portion of the entry will automatically be assigned the cost center of the equipment or cost category, and no changes will be allowed. The system will first assure that you have permission for cost center specified in the cost category file, if any. Entry of that cost category will not be permitted if the cost center in the cost category file is disallowed. If the cost center is not specified in the cost category file, the cost center assigned to the equipment will be assigned, provided your operator has permission for that cost center. Spectrum will not allow entry of equipment codes with no cost center since the cost centers are required for equipment. The system also assures that the cost center assigned to the line based on the equipment or cost category is valid for the G/L account code specified on that line. Validation for the credit cost center varies, depending on the transaction type.
Equipment Overrides
For cost transaction types (EC, AP and PR), when your operator's scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with equipment override cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then the transaction entry line will not be allowed. The system applies the equipment override validation to the cost center of the cost category when determining permission for the debit cost center.
G/L Account Validation
The system will verify the cost center assigned to each G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. The system compares the G/L account's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that G/L account code is not allowed. The validation is performed for all transaction types.
Multi-company Transaction Types
For multi-company cost transaction types (EU, ES, AP and PR), cost center validation is performed based on settings in the destination company. When the Enterprise Installation option for cost centers is set to Yes in the destination company, then the cost center designated on the transaction line applicable to the other company must be valid in that other company. Spectrum also verifies that the cost center is valid for the G/L account and operator in that other company. When the Enterprise Installation option for cost centers is set to No in the destination company, then the applicable cost center field will not appear on that transaction line.
For multi-company Cost entries (AP and PR), the software will read the company code of the equipment code of the transaction line, and then determine if that company code has been assigned a particular inter-company G/L account. For the Debit entry, the Equipment Control Installation setup of the current company is used, and for the Credit entry to the equipment company (referenced in the transaction line), the Equipment Control Installation setup of that other company is applied. Inter-post entries are not applicable for these transaction lines.
