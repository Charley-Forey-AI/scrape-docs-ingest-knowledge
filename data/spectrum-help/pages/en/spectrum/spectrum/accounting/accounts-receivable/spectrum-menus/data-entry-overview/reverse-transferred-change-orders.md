---
title: "Reverse Transferred Change Orders | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/reverse-transferred-change-orders"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/reverse-transferred-change-orders"
---

# Reverse Transferred Change Orders

Use this screen to reverse change orders and change requests for the selected contract. Enter Job and Customer codes in the header portion of the screen, and Spectrum will display the change orders and change requests that can currently be reversed. Specifically, the following change requests and change orders will appear in the grid portion of the screen for reversal:

- Any change orders that were originally transferred to the open draw request application

- Any change orders that were transferred to later applications not currently on the software (this could include an application that was previously open on the software, but was removed during the Reverse Last Draw Request update)

- Any change requests that have not been assigned to a change order for reversal if they were transferred to the open application (or a later one that was removed)

- Any change requests that have been assigned to a change order

- Any pertinent change requests assigned to a change order that has not yet been transferred
If a change request that has been transferred to the current application and was later attached to a change order, it can be reversed only if the change order has not yet been transferred. In addition, change request that were originally transferred to an application that has already been posted are not available for reversal and will not display for the selected contract. Likewise, any change requests that have been transferred to the open application but were later attached to a change order that is not currently available for reversal will not appear.

Once you select lines for reversal and click Continue, the update will remove the transferred revenue from the current draw request for the specified changes and will also reset the change order or change request status to unposted, removing the application number from the item. If a change order that includes a change request that has already been transferred to an earlier application is reversed, the revenue on the draw request associated with the change request will not be reversed and that change request will not be deselected; the rest of the change order revenue will be removed from the draw request and the change order (and any other attached change requests) status will be changed to unposted.
