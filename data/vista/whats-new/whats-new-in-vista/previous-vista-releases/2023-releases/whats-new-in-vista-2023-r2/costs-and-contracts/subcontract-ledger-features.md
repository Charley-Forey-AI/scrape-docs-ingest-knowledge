---
title: "Subcontract Ledger Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/costs-and-contracts/subcontract-ledger-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r2/costs-and-contracts/subcontract-ledger-features"
---

# Subcontract Ledger Features

Vista 2023 R2 delivers on user-requested Subcontract Ledger enhancements, fixes, and other improvements.

## Update to Max Retention Calculations on Subcontract Claims

When entering claims in SL Subcontract Claims, the system now correctly calculates 0.00 retention for subcontract items when the WC Maximum Retention is set to 0.00% or 0.00 amount for a subcontract (in SL Subcontract Entry).
Additional changes made in SL Subcontract Claims include the following:

- A new Distribute Item Retainage button was added to the Subcontract Details section of the form. The button label differs by country as follows:

- Distribute Item Retainage (U.S.)

- Distribute Item Retention (AU)

- Distribute Item HoldBack (CA)

 When you select this button, the system calculates and distributes the retention on the claim based on the work complete retention percentage entered for each subcontract item included on the claim. If item retention exceeds the maximum (which causes a 'Max Retention Limit has been exceeded' message to display), selecting the Distribute Item Retainage button causes the retention to be recalculated and the message to be cleared.
If the WC Maximum Retention is set to 0.00% or 0.00 amount for a subcontract and item retention amounts are greater than 0.00, selecting the Distribute Item Retainage button sets the item retention amounts to 0.00.
Additionally, once you select this button, if you have selected the Show Retention button, the screen automatically refreshes with the calculated amounts. Previously, you would need to select the Refresh button to show the new calculations.
Note: If user security prohibits update permission for the SL Subcontract Claim form, the new Distribute Item Retainage button is disabled.

- Removed the Calculate and Distribute Claim Retention to Claim Items option from the File menu, as it is no longer needed.

## Access Vista Web's Pending PO / Subcontract Review from SL

You can now access the Pending PO / Subcontract Review approval page in Viewpoint Field Management™ from the Subcontract Ledger module. The Programs menu in SL now includes an SL Subcontract Review link that when selected, opens the Pending PO / Subcontract Review page in a web browser.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
