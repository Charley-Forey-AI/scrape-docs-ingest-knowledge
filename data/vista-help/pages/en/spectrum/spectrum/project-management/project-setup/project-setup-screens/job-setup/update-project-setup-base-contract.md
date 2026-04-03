---
title: "Update Project Setup (Base Contract) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/update-project-setup-base-contract"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/update-project-setup-base-contract"
---

# Update Project Setup (Base Contract)

Once the job setup reports have been printed and proofed for accuracy, the Update Project Setup actually sets up the imported job in the Spectrum Job and Phase files in Job Cost.

- If the imported job type is Time + Material or Cost plus, as
 specified on the import starting screen, then the job will also be set up in the Time +
 Materials module.

- Additionally, the Accounts Receivable contract can be automatically
 set up. Billing detail for the contract will be set up as well if specified in the
 Project Setup file.

- An estimate may be updated more than once if changes have been
 made. Each time an estimate is updated, all original and current estimate figures are
 reset, based on the estimate. Therefore, if changes have been made to the estimates in
 Job Cost, for example, due to change orders, caution is advised when re-running this
 update.

- The system does not add new phases to the Job Cost phase file if
 the estimated hours, cost and quantity are all zero in the import file unless the
 Include phases with no estimated costs,
 hours or quantity? checkbox is selected in this screen. This way,
 superfluous phases are not automatically created in the phase file. Important: If a phase has a current estimate/projection
 that is not included on the latest Project Setup update, the update will set the
 estimate on that phase to zero (0). Performing this update for phases that already
 have change requests or change orders applied is not recommended. It is possible to
 automatically set the projected cost and projected hours when phases are transferred
 to Job Cost. Based on the Set projected costs, quantity and hours to
 current estimate when adding a phase? checkbox on the Site Map > System Administration > Installation > Job Cost > Properties tab, the Spectrum will set projected cost and hours equal to the
 current estimates as the phase is updated. This eliminates the projected cost
 processing procedure some companies routinely perform each time a new estimate is
 added to Job Cost via Project Setup.
Note: If the
 Set projected costs, quantity and hours to current estimate when adding
 a phase? checkbox is selected on the Site Map > System Administration > Installation > Job Cost > Properties tab, then the amount in this field is automatically set to equal the
 amount in the Current Estimate > Quantity field on the Phase File
 Maintenance screen.
