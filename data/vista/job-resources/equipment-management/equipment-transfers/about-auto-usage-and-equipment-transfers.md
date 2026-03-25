---
title: "About Auto Usage and Equipment Transfers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-auto-usage-and-equipment-transfers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-auto-usage-and-equipment-transfers"
---

# About Auto Usage and Equipment Transfers

If you are using the EM Automatic Usage program, equipment
 transfers must be handled using the EM Location Transfers or EM Mass Location Transfer v11
 forms.
The system automatically charges equipment usage to
 jobs based on the length of time the equipment is on the job. When you transfer a
 piece of equipment, the system automatically updates the current job and location
 fields in the Equipment Master. The update of this information is especially
 important if you have selected the Restrict Usage to Current Job
 checkbox for the equipment category in EM Categories.
Important: If you are using both ‘auto usage’ and ‘manual usage’ functionality on the same piece of equipment, you should use the EM Location Transfers form.
If you transfer equipment using the EM Mass Location
 Transfer v11 form, upon clicking the Equipment Refresh button, the system adds
 equipment to the Equipment selection box based on values in the EM Equipment (EMEM)
 table, rather than the EM Location History (EMLH) table. If you update the job and
 location in EM Equipment when posting equipment usage (option in EM Company
 Parameters, Updates tab), this may cause the job/location assignments for equipment
 to differ from the "transfer to job" records in the EM Location History table. If
 you plan to use this form to transfer equipment, you should set the Job
 Location option in EM Company Parameters (Updates tab) to Do not update Job
 or Location.

Related information

- [About the EM Mass Location Transfer v11 Form](/en/vista/vista/job-resources/equipment-management/equipment-transfers/about-the-em-mass-location-transfer-v11-form)
