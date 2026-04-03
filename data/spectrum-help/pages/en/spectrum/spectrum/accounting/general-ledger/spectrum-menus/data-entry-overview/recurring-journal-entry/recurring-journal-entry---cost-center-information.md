---
title: "Recurring Journal Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/recurring-journal-entry/recurring-journal-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/data-entry-overview/recurring-journal-entry/recurring-journal-entry---cost-center-information"
---

# Recurring Journal Entry - Cost Center Information

Spectrum verifies the cost center assigned to the G/L account code by comparing the entry to the list of allowed cost centers for that G/L account. Spectrum compares the G/L account's list of shared cost centers with cost centers in the operator's assigned scheme, and if there are no common cost centers, then that G/L account code is not allowed. Validation is also performed if the operator attempts to change or delete an existing distribution line. Below is a chart that outlines the impact of cost centers on different types of distribution lines.
This screen excludes journal entries from the list box if you do not have security authorization to the cost center specified in the journal entry header.
Line Type
Cost Center Verification

Direct Job Cost
For direct job cost journal entries, the cost center is assigned based on the cost center associated with the job or phase. The cost center specified in the phase file will display if valid (and active), and your operator has permission for the specified cost center. Entry of the phase will not be permitted of the cost center in the phase file is not allowed. If the cost center is not specified in the phase file, the cost center assigned to the job will be shown (if valid and active), provided your operator has permission for the cost center. Spectrum also assures that the cost center assigned to the line based on the job or phase is valid for the G/L account code specified on that line. Entry of that job will not be permitted of the cost centers in both the job and phase files are not allowed.
When your operator's scheme includes override settings for Job entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to direct job cost journal entry detail lines based on these overrides. The override cost centers supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with Job override cost centers in your operator's assigned scheme and if the cost center is not included, then the journal entry line is not allowed.

Direct Equipment Cost
For direct equipment journal entries, the cost center is assigned based on the cost center associated with the equipment or cost category. The cost centers specified in the cost category file will display if valid (and active), and the operator has permission for that cost center. Entry of that cost category will not be permitted if the cost center in the cost category file is disallowed. If the cost center is not specified in the cost category file, the cost center assigned to the piece of equipment will be shown (if valid and active), provided the operator has permission for that cost center. Spectrum also assures that the cost center assigned to the line based on the equipment or cost category is valid for the G/L account code specified on that line. Entry of that equipment will not be permitted of the cost centers in both the equipment and cost category files are disallowed.
When your operator's scheme includes override settings for Equipment entries in Cost Center Scheme Maintenance, this screen will validate the cost center assigned to direct equipment cost journal entry detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum will compare the cost center assigned in the entry screen detail with Equipment override cost centers in your operator's assigned scheme, and if the cost center is not included, then the journal entry line will not be allowed.

Non-Job
When your operator's cost center scheme includes override settings for non-job entries in Cost Center Scheme Maintenance, this screen validates the cost center assigned to non-direct journal entry detail lines based on these overrides. The override cost center(s) supersede the cost center list defined for the scheme in general. Spectrum compares the cost center assigned in the entry screen detail with non-job override cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then that cost center will not be allowed on the detail line.
