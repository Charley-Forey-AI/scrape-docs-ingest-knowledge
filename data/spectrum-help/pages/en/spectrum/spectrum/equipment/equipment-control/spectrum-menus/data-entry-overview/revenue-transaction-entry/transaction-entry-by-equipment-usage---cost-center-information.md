---
title: "Transaction Entry by Equipment Usage - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/transaction-entry-by-equipment-usage---cost-center-information"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/revenue-transaction-entry/transaction-entry-by-equipment-usage---cost-center-information"
---

# Transaction Entry by Equipment Usage - Cost Center Information

If cost centers are being used in this company, for revenue transaction types Equipment Usage (EU), Spectrum verifies that you have authorization to the equipment before transactions are displayed or added.

- Revenue transaction types entered by job will validate the job for your operator.

- For Equipment Usage (and all other transaction types) by equipment, Spectrum verifies that the equipment is valid for your operator. If it is, then you will see all transactions for the equipment; however, you can only add or modify records if they have security for the debit cost center.

- For Equipment Usage by equipment, Spectrum also verifies that your operator has authorization to the job before transactions are added. Spectrum compares the cost center assigned to the job with cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then activity for that job is displayed, but may not be changed. The system also verifies authorization for the assigned phase. Entry of that phase will not be permitted if the cost center in the phase file is not allowed.

- For Equipment Usage transaction type entries, the debit cost center will be available for lookup only, and set from the job (or phase) cost center. For rental lines the debit cost center may be entered, but it can't be blank; it will default from the equipment cost center. The credit cost center will be display only from the equipment.

Job Entries

- For Equipment Usage job transaction type entries, when your
 operator's scheme includes override settings for job entries in Cost Center Scheme
 Maintenance, this screen validates the cost center assigned to job transaction detail
 lines based on these overrides. The override cost center(s) supersede the cost center
 list defined for the scheme. The system will compare the cost center assigned in the
 entry screen detail with job override cost centers in your operator's assigned cost
 center scheme, and if the cost center is not included, then the transaction entry line
 will not be allowed.

Non-Job Entries

- For Equipment Usage rental transaction type entries, when your
 operator's scheme includes override settings for non-job entries in Cost Center Scheme
 Maintenance, this screen validates the cost center assigned to rental transaction detail
 lines based on these overrides. The override cost center(s) supersede the cost center
 list defined for the scheme in general. The system will compare the cost center assigned
 in the entry screen detail with non-job override cost centers in your operator's
 assigned cost center scheme, and if the cost center is not included, then the
 transaction entry line will not be allowed.

Equipment Entries

- For cost transaction types (EC, AP and PR), when your operator's
 scheme includes override settings for equipment entries in Cost Center Scheme
 Maintenance, this screen validates the cost center assigned to transaction detail lines
 based on these overrides. The override cost center(s) supersede the cost center list
 defined for the scheme. Spectrum compares the cost center assigned in the entry screen
 detail with equipment override cost centers in your operator's assigned cost center
 scheme, and if the cost center is not included, then the transaction entry line will not
 be allowed.

G/L Account Validation

- The system will verify the cost center assigned to each G/L account
 code by comparing the entry to the list of allowed cost centers for that G/L account.
 The validation is performed for all transaction types.

Multi-company Transaction Types

- For multi-company cost transaction types (EU, ES, AP and PR), cost center validation is performed based on settings in the destination company. Spectrum also verifies that the cost center is valid for the G/L account and operator in that other company.

- For revenue transactions (EU and ES) where the equipment code is set up in a different company than the job, rental, vendor, or employee assigned to the transaction, the software assigns the inter-company account for the balancing entry in both companies. When the Enterprise Installation option for cost centers is set to No in the destination company, then the applicable cost center field will not appear on that transaction line.

- For revenue entries, the software reads the company code of the equipment code of the transaction line, and then determine if that company code has been assigned a particular inter-company G/L account. For G/L entries in the equipment company, the Equipment Control Installation setup of the equipment company is used, and for the entries to the company of the job or rental activity, the Equipment Control Installation setup of that other company is applied. Inter-post entries are not applicable for these transaction lines.
