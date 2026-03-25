---
title: "Set up the Create and Send Feature | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature/set-up-the-create-and-send-feature"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature/set-up-the-create-and-send-feature"
---

# Set up the Create and Send Feature

You must set up the Create and Send feature before you can use it in applicable PM forms to generate project documents and email them to applicable contacts.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.

Follow the steps below to set up the enhanced Create and Send feature. These steps are very similar to setting up the legacy Create and Send used on other forms in the PM module

1. (LAN, VFC, and VRL on-premises only) For information on configuring SMTP, refer to the Support Knowledge Base. In the Knowledge Base, search for "How to Configure SMTP for Viewpoint Emails".

1. Review how user accounts are configured in the [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form) form. The From address of the emails sent is the email address set up on your user account (in VA User Profile, Info tab, Email Address field).
If you do not have an email address set up in this field, VP Message cannot be selected in the Notify By field. If you would like Notifier messages to still use VP Messaging, open the Notification Preferences tab on the VA User Profile form and then create a new line item where the Source is Notifier and the Destination is VP Message.

1. Optional: Use [Allow Document Edit](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049e0b--en) to disable the ability for users to edit Word documents prior to sending them via Create & Send.

1. Optional: Use [Select All Attachments](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#ID-00049e16--en) to automatically attach all documents when using Create & Send.

1. Optional: To create any additional document types, see [PM Document Types Form](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form). Document types can be used to assign default document templates and distribution defaults.

1. Optional: To create and maintain the data sources, see [PM Create & Send Data Sources Form](/en/vista/vista/project-management/create-and-send/pm-create--send-data-sources-form). Generally you only need to do this if you want to include the information in a custom table on a project document.

1. To create and maintain the document template locations, see [PM Create & Send Locations Form](/en/vista/vista/project-management/create-and-send/pm-create--send-locations-form). This is where the custom document templates are stored.

1. To set up the document categories, see [PM Create & Send Settings Form](/en/vista/vista/project-management/create-and-send/pm-create--send-settings-form). You can deactivate the Create and Send feature, or set up the subject line on generated emails to have a specific format.

1. To set up your document templates, see [PM Create & Send Templates Form](/en/vista/vista/project-management/create-and-send/pm-create--send-templates-form). Document templates determine the format of the documents generated using the Create and Send feature. For example, the RFI document template defines how RFI documents generated using the Create and Send feature appear.

1. Optional: Define any default document templates. This allows you to define which document templates should by default be used when using the Create and Send feature. [More](/en/vista/vista/project-management/create-and-send/assign-a-project-template)

1. Optional: Assign the distribution defaults. Distribution defaults define what documents a project contact should by default receive. [More](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form)

1. Optional: To create and maintain distribution groups, see [PM Distribution Groups Form](/en/vista/vista/project-management/create-and-send/pm-distribution-groups-form). These can be used to add contacts to an email.

The setup is complete.
