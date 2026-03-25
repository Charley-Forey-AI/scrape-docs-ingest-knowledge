---
title: "Create a Document Location | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/create-and-send/create-a-document-location"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/create-and-send/create-a-document-location"
---

# Create a Document Location

Create a document location using the PM Create & Send Locations form.
Note: Your company's Vista deployment method affects which actions you should take on this page. Your deployment method is shown at the bottom of the Main Menu in the status bar.

Template locations are where document templates are
 stored. To create a document location in the PM Create & Send Locations
 form:

1. Click the New Record icon.

1. In the
 Location field, enter a name for the new
 location.

1. The Document Path field identifies where the document templates will be stored.
 Your deployment method dictates what action you should take in this field:Deployment
 methodRequired Action
VRL cloudDo not make a selection or
 enter anything. Skip this step.
LAN, RDP, or legacy cloudUse the Browse button to
 navigate to and select the directory location on the network.
LAN *and* VRL on-premisesThe directory you enter must be
 subdirectory of the directory defined in the API Settings tab of the
 Viewpoint Configuration form located on your app server. If you don't
 know what's been defined, ask your system administrator.
VRL on-premises
 onlyDo not make a selection or
 enter anything. Skip this step.

Important: Do not use the standard Viewpoint
 document templates directory (Viewpoint Repository\Document
 Templates\Standard). If you do, each time you install a new release, the update will overwrite
 this directory, thereby removing your custom templates.Instead, save
 your custom templates to the Viewpoint Repository\Document
 Templates\Custom\<your_custom_name> directory.

1. Click Save.

Once the document location is saved:

- if you want to copy a standard document template and paste it into the new
 location, use the PM Copy Document Template form.

- if you want to move existing customized templates to the new location, use the PM Transfer form.

Related concepts

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
