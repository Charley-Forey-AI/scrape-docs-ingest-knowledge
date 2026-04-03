---
title: "Equipment Tracking Requisition | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/equipment-tracking-requisition"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-tracking/spectrum-menus/data-entry-overview/equipment-tracking-requisition"
---

# Equipment Tracking Requisition

This screen is used to enter tracking information about
 equipment and inventory items, and allows multi-company processing. If the multi-company
 option is being used in either the Inventory Control or Equipment Control modules, then a
 company ID may be entered for the job during equipment tracking data entry. Multi-company
 processing is available for requisitions with direct cost transaction codes. The system will
 post G/L expense and Job Cost to the company ID entered. The intercompany G/L code entered on
 the Inventory Control Installation or Equipment Control
 Installation screens will be used as the G/L credit account code.
The system will validate Equipment Tracking requisitions against the history file in this screen. On billing for requisitions, the billing rate is defined as the number of days an item has been issued to a job. If the requisition has already been recorded, a warning message appears and further entry is disallowed.

- For non-job issues, the Issue to job field is skipped and the division field is available. If the G/L Direct cost flag is set to Job cost or Equipment cost, then the division is a must input and it must correspond to the G/L department file; if the flag is No direct cost, this field is optional and is only used for reports and inquiries. For non-job entries, the phase and ct fields are skipped and no entry is allowed. Also, when division is entered and validated, then it should also validate that the G/L department and the account code in the transaction code file together make a valid full G/L code. Otherwise, it should display error and not let you continue.

- For non-job issues of equipment, these will create rental billing transactions with the same logic as we use for job billings. For non-job inventory issues, these will be sent to the inventory system as adjustment sales to inventory. The requisition # will be the same as the adjustments reference # and the remarks will be transferred over from the requisition to the message line in adjustments.

- Equipment and inventory can be issued to a job with a simple click of the Continue button.

- Equipment is returned automatically from the 'old' job when an issued piece of equipment is 'Issued' to a 'new' job

- Requisition 'returns' are handled automatically by the software, simply by highlighting the piece of equipment to be returned to a yard or deployed to another job in a single-step process.
Note: If Document Imaging is being used, any image records saved from this
 screen will be stored in the Document Imaging > EC cabinet.

Related information

- [Equipment Rate Hierarchy](/en/spectrum/spectrum/equipment/equipment-tracking/equipment-tracking-installation/equipment-rate-hierarchy)
