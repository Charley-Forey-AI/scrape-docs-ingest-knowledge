---
title: "Cost Transaction Entry by Payroll - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry-by-payroll---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/cost-transaction-entry/cost-transaction-entry-by-payroll---cost-center-information"
---

# Cost Transaction Entry by Payroll - Cost Center Information

For Payroll transaction type entries, Spectrum allows you
 to add a transaction for an employee only if your operator has permission to access that
 employee.
The system then validates entry of the equipment code and cost category to assure that your
 operator has authorization for the transaction. The cost center assigned to the credit
 portion of the entry will automatically be assigned the cost center of the employee.
When your operator's scheme includes override settings for employee entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to payroll transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general.
For cost transaction types, Spectrum displays cost centers for the debit and credit portions of the transaction entry. The cost center assigned to the debit portion of the entry will automatically be assigned the cost center of the equipment or cost category. If the cost center is not specified in the cost category file, the cost center assigned to the equipment will be assigned, provided your operator has permission for that cost center. Cost centers are required for equipment. Validation for the credit cost center varies, depending on the transaction type.
Equipment Overrides
For cost transaction types (EC, AP and PR), when your operator's scheme includes override settings for equipment entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to transaction detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme. The system applies the equipment override validation to the cost center of the cost category when determining permission for the debit cost center.
G/L Account Validation
The system will verify the cost center assigned to each G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. The system compares the G/L account's list of shared cost centers with cost centers in your operator's assigned cost center scheme. The validation is performed for all transaction types.
Multi-company Transaction Types
For multi-company cost transaction types (EU, ES, AP and PR), cost center validation is performed based on settings in the destination company. When cost centers are being used in the destination company, then the cost center designated on the transaction line applicable to the other company must be valid in that other company. Spectrum also verifies that the cost center is valid for the G/L account and operator in that other company.
For multi-company Cost entries (AP and PR), the software will read the company code of the equipment code of the transaction line, and then determine if that company code has been assigned a particular inter-company G/L account. For the Debit entry, the Equipment Control Installation setup of the current company is used, and for the Credit entry to the equipment company (referenced in the transaction line), the Equipment Control Installation setup of that other company is applied. Inter-post entries are not applicable for these transaction lines.
