---
title: "Printing Crystal Reports With Custom Fonts (Cloud) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/crystal-reports-overview/printing-crystal-reports-with-custom-fonts-cloud"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/crystal-reports-overview/printing-crystal-reports-with-custom-fonts-cloud"
---

# Printing Crystal Reports With Custom Fonts (Cloud)

If you use custom fonts on your Crystal Reports, you must render those reports locally in order for your custom fonts to be used when printing.
When printing Crystal reports in the cloud, the system automatically uses the standard Vista fonts, even if you have applied custom fonts to the report. To use your custom fonts when printing reports requires that you render them locally.The following details how to set up your reports to render locally.

1. Format your Crystal Report with the custom font. See [Formatting Crystal Reports](/en/vista/vista/system-tools/reports/crystal-reports-overview/formatting-crystal-reports) for more information.

1. Select Reports > Programs > RP Report Titles.

1. Select the customized report from the Grid tab.

1. On the Info tab, select the Force Local Render checkbox.

When you print this report, the system renders the report locally using your custom fonts.
