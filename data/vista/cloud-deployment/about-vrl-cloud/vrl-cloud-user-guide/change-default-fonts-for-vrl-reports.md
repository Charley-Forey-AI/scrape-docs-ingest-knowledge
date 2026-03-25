---
title: "Change Default Fonts for VRL Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/change-default-fonts-for-vrl-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-vrl-cloud/vrl-cloud-user-guide/change-default-fonts-for-vrl-reports"
---

# Change Default Fonts for VRL Reports

If your deployment method is either VRL on-premises or VRL Cloud, you may need to replace an unsupported font with a supported one so that you your custom reports render properly.
Take the steps below only if all the following apply to you:

- your deployment method is either or VRL on-premises or VRL Cloud

- your Vista version is 2020 R1 or greater; to confirm your version, go to Help > About Vista

- you use any custom report that uses the Arial Narrow font and the report is rendering poorly (looks distorted)

Note: In order to proceed, your computer must have .NET 4.7.2 or higher. If it does not, the utility will fail to run and you will receive an error message. If needed, download the latest version of the .NET framework from Microsoft at [https://dotnet.microsoft.com/download/dotnet-framework](https://dotnet.microsoft.com/download/dotnet-framework).

To replace the Arial Narrow font, you need to do the following:

- Download, extract, and open the font replacement utility.

- Select the report files you want altered.

- Run the utility to exchange the fonts on the report files you've selected.

1. Download, extract, and open the font replacement utility.

1. Go to this location to locate the zip file: [https://support.viewpoint.com/s/product-more-resources?product=Vista&type=Downloads&links=true&title=Downloads%20for%20Vista](https://support.viewpoint.com/s/product-more-resources?product=Vista&type=Downloads&links=true&title=Downloads%20for%20Vista)

1. Select FontExchange_20200110.zip to begin downloading it.Once it finishes downloading, your downloads folder displays a zip folder named FontExchange_20200110.

1. Navigate to your Downloads folder, right-click the file, and select Extract All.A new screen appears prompting you to select a location.

1. Select a location and then select Extract.The location you chose to save the files to opens automatically.

1. Double-click the FontExchange item whose Type is Application.

1. If you receive a Windows Defender alert, locate and select More Info, then Run anyway.The Viewpoint Crystal Reports Utility opens.

1. Select the report files you want altered.

1. To add one or more files to the File List section, select the Add File icon in the top left corner.

1. To add all files in a directory to the File List section, select the Add Folder icon in the top left corner.The reports you have selected appear in the File List section.

1. If you want to remove a single file from the list, select the file to remove and press the delete key.

1. If you want to remove all files from the list, select the Clear Files icon in the top left corner.

1. Run the utility.

1. In the Original Font field, select Arial Narrow.

1. In the Replacement Font field, select VP Narrow.

1. In the Backup File Directory field, select the blue ellipsis button and use the search dialog to select the directory to store the original, non-modified files.

1. Select Run.The Status column displays the result for each report file.

The system makes the font changes to the report files you selected.Tip: There is no harm if you happen to run the utility multiple times for one or more reports.

Related concepts

- [About VRL Cloud](/en/vista/vista/cloud-deployment/about-vrl-cloud#concept-7178--en__concept-7178)
