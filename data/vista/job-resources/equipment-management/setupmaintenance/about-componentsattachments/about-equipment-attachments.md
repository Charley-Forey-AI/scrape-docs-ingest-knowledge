---
title: "About Equipment Attachments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-componentsattachments/about-equipment-attachments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-componentsattachments/about-equipment-attachments"
---

# About Equipment Attachments

Attachments are pieces of equipment that are 'attached' to other pieces of equipment (for example, a bucket attached to a backhoe or a trailer attached to a dump truck).
Each attachment is set up individually as a piece of equipment, and then assigned to a primary piece of equipment as an attachment. Although an attachment can be assigned to only one primary piece of equipment, a primary piece of equipment can have multiple attachments. And since attachments typically remain with the primary piece of equipment, each time the primary piece of equipment is transferred from one location or job to another, all of the attachments are automatically transferred as well.
When setting up an attachment (in EM Equipment), it is assigned as an Equipment type. Then, on the Comp/Attach tab, you identify the piece of equipment to which it is attached.
Revenue can be posted to the attachment by checking the Post Revenue to Attachment, indicating that usage should be posted to the attachment whenever usage is posted to the primary piece of equipment. Because attachments are set up as individual pieces of equipment, you can designate the revenue rate you want used whenever usage is posted to the attachment. Usage will be posted using the same revenue code specified for the primary piece of equipment, therefore, you must make sure to set up the same revenue codes (in EM Revenue Rates by Category) for the attachment as you have set up for the primary piece of equipment. If you have set up an override to the standard rate by equipment for the primary piece of equipment, you do not have to set up override rates by equipment for the attachment(s). Usage will be posted to the standard rate defined for the attachment.
Note: If usage is entered for a revenue code, and the revenue code has not been set up for the attachment, a warning is displayed, and the record will not be inserted.
Be aware that if multiple attachments exist for a primary piece of equipment, usage will be posted to each attachment when posted for the primary piece of equipment. If you will not be using an attachment for a particular job, you must remove the attachment from the primary equipment to prevent usage from being posted to it. You can remove the attachment manually in EM Equipment; however, if you are tracking the location of your equipment, you should use the EM Location Transfer program to transfer the attachment to the appropriate location (such as a yard or storage facility).
You can view the attachments assigned to a primary piece of equipment by selecting the equipment (in EM Equipment) and clicking on the Attachments tab. All attachments assigned to the equipment will be listed by equipment code.

Related information

- [About the EM Equipment Form](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)
