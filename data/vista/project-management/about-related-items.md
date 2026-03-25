---
title: "About Related Items | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/about-related-items"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/about-related-items"
---

# About Related Items

The Related Items feature allows you to link related project records and then view and
 access those items from the Project Management Work Center and most forms in the PM module.
Related Items are linked in several ways:

- Automatically - The system
 automatically relates two records when one record is used to generate another. For
 example if you create an issue log from a subcontract (by selecting CreateIssue Log from PM Subcontracts),
 the system automatically relates the created Issue Log with the subcontract used to
 create it.
The Create drop down in the PM Work Center also automatically
 links related records.

- Manually - You can manually
 create and remove item relations using the PM Relate Items form. This form is
 launched by clicking the drop down next to the Related Items icon and selecting Add
 Related Items. PM Relate Items has search functions that allow you to quickly locate
 records and then manually add or remove the relations.

- From the PM Work Center -
 You can also manually relate items using the drag and drop feature on the Related
 Items panel on the PM Work Center. For example if you receive an MS Outlook email
 about a Subcontract, you can open that Subcontract in the PM Work Center and then
 drag and drop the email from MS Outlook to the Related Items panel. This will add the
 email as an attachment and as a related item on the Subcontract.

- Creating a Related
 Document - You can create related items using the Create Related
 option (). When you create a related item, the system creates a
 new record using the information on the currently selected record. The new record is
 associated with the current record using the Related Item feature, and to reduce data
 entry, some of the fields on the new record will default based on the currently
 selected record.
For example if you are viewing a meeting in the PM Meeting Minutes
 form and want to create a subcontract, click on the Create Related option and select
 Subcontract from the menu that displays. This will open the PM Subcontracts form, and
 populate the Project field so that you can create a new subcontract.

Once items are linked, you can view them using the Related Items panel
 on the applicable form (accessed by selecting Related Items > View Related Items from the form's toolbar) or using the Related Items panel on the PM Work
 Center.
For example, if you highlight an RFI in the
 Work Center, the following will display in the Related Items panel:

- All project issues, transmittals,
 pending change orders, or other records related to the RFI will be grouped into
 folders - for example project issues will display in a folder titled Issues

-  Any emails related to the RFI will
 display in a folder titled Email - the emails must be attached to the RFI record, not
 just indexed to the project and RFI, and they must have an .msg file extension

-  Attachments on the RFI will display in
 a folder titled Attachments

- RFI documents generated using the Create
 and Send feature will also display in the Attachments folder, but the RFI document
 category must be set up to save generated documents as attachments using PM Create
 & Send Settings.

## Setup

There are two things to set up before using
 the Related Items feature:

- Make sure you select the Allow multiple
 instances of a form checkbox in VA User Profile or in the User
 Options form (accessed from the main menu by selecting Options > User Options). If this checkbox is not selected, you will be unable to open
 records of the same document category from a form when using the Related Items
 panel. For example, you will not be able to open related project issues from PM
 Project Issue because you will not be able to open multiple instance of PM Project
 Issue.

- You may also want to select the
 Default
 Create and Send Attach to Parent Form as checked checkbox on the
 Info tab of PM Create and Send Settings for each document category. When this box
 is checked, documents generated using the Create and Send feature will be saved as
 attachments on the parent form, which means you will be able to view and open them
 using the Related Items panel on the Work Center. For example when you highlight
 an RFI in the Work Center grid, the Related Items panel will not only display all
 of the related records but also all of the generated RFI documents.

Note: This does not apply to the Related Items panel that
 displays on forms, which does not display attachments

Related concepts

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)

- [PM Create & Send Settings Form](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [About the User Options Form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-user-options-form)

- [About the Project Management Work Center](/en/vista/vista/system-tools/work-centers/about-the-project-management-work-center)

- [PM Relate Items Form](/en/vista/vista/project-management/about-related-items/pm-relate-items-form)

Related information

- [About Creating Queries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries)
