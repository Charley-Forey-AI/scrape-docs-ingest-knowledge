---
title: "Hard Dollar File Transfer - Other Issues | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-hard-dollar/hard-dollar-file-layout-overview/hard-dollar-file-transfer---other-issues"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-hard-dollar/hard-dollar-file-layout-overview/hard-dollar-file-transfer---other-issues"
---

# Hard Dollar File Transfer - Other Issues

The following information should be noted prior to completing any Hard Dollar file transfers.

- If you have multiple levels in your WBS for the direct bid costs,
 the budget.txt file will only store the lowest level of detail with your costs,
 quantities, and hours. The higher levels will have the activity code and description.
 This ensures that the count doesn't double the lowest level items with higher level
 totals.

- If several of the direct bid costs have the same account numbers,
 then these will be transferred into Project Setup with the same phase codes. However,
 when they are transferred to the Job Cost module, these will be summarized. The hours,
 costs, AND quantities will be summarized into the phase code and cost type. The
 description, unit of measure and quantities assigned to each phase are based on the
 information in the "Account Codes" record. Each cost activity in the "Direct Bid Cost by
 Bid Item" contains an account number. This same account number is defined in the
 "Account Codes" section and contains the specific description, unit of measure and
 quantity for that cost activity that will be used during the Esti-link Job Import and
 setup.

- Phases are imported from Hard Dollar using the account number in
 Hard Dollar. In Hard Dollar, you have control of what the phase code is by entering this
 number under the account number in the budget. Remember, you can specify the same
 account number for different budget items, but the quantity will also be accumulated
 along with the hours and dollars. Therefore, you may want to only assign the same phase
 number to budget items with the same unit of measure. The length of the phase is
 determined by the phase mask in Job File Maintenance. If there is a difference between
 the number of characters in the account code and the phase mask in the job, the phase
 line item will be created starting with the leftmost character of the account code and
 reading right until the account code contains sufficient characters. Zeros will be added
 to the end if necessary to meet the phase mask requirements.

- The billing items are imported from Hard Dollar using the bid
 (pay). If the Import job with bid group checkbox is not selected, the billing item in
 the phase is set to the number of characters defined by the billing item mask and will
 read the designated number of characters of the pay ID (beginning with the rightmost
 digit and counting left) in the "Direct Bid Costs by Bid Item" record. The billing item
 created in the contract detail will be determined in a similar manner, reading the "Item
 Code" field in the "Bid Items" record. If the "Import job with bid group" checkbox is
 checked the user is prompted for a bid group; this 2 character field can be used as a
 prefix for all billing items. If left blank the billing item is created in both the
 phase file and the contract file using the same logic as "Import job with bid group =
 not checked" as defined above. When transferred to job cost, this code will be setup in
 the phase file as the billing item. This billing item number created in both the phase
 file and the contract detail should be the same number; this cross reference allows you
 to see the revenue versus cost on the billing item analysis inquiries and reports in Job
 Cost.

- The alternate phase in Spectrum is set to the Hard Dollar cost
 account (account number). The alternate phase code can be used when transferring
 historical costs back to Hard Dollar for analysis. You are allowed to transfer the
 actual costs from Job Cost into a cost code field that can either be your phase code or
 this alternate phase code. If you have some standard codes for the company and those
 aren't always used for setting up jobs (for example, you put the bid item + cost account
 as the phase), then this allows you to use that standard code for creating historical
 analysis.
