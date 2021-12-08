---
title: "Configure Parallels"
url: /howto/general/using-mendix-studio-pro-on-a-mac
category: "General Info"
menu_order: 2
description: "This how-to will allow you to start making Mendix apps on your Mac device."
tags: ["Native", "Parallels", "Mac", "Mobile"]
---

## 1 Introduction

Using Parallels, you can run Mendix Studio Pro on your Mac device using a Windows virtual machine.

{{% alert color="warning" %}}
Studio Pro does not run under Parallels on Apple Silicon Macs, such as the M1.
{{% /alert %}}

To start making Mendix apps on your Mac, follow this how-to.

**This how-to will teach you how to do the following:**

* Configure your Windows virtual machine for Mendix Studio Pro
* Run a Mendix app on a test device using your Windows virtual machine
* Make changes to your app, then view those changes on your test device

For a deep-dive look into installing Studio Pro on a Mac, check out this video:

<img
  style="width: 100%; margin: auto; display: block;"
  class="vidyard-player-embed"
  src="https://play.vidyard.com/nJ9Tz8VnHPPKPrtSBgHv3U.jpg"
  data-uuid="nJ9Tz8VnHPPKPrtSBgHv3U"
  data-v="4"
  data-type="inline"
/>

## 2 Prerequisites

Before starting this how-to, make sure you have completed the following prerequisites:

* Install [Parallels Desktop Pro Edition](https://www.parallels.com/products/desktop/pro/), install Windows when prompted by Parallels, and create a Windows virtual machine (Parallels Desktop Pro Edition is necessary for Mendix's network features to work)
* Install Mendix Studio Pro on your Windows virtual machine

## 3 Configuring Your Windows Virtual Machine for Mendix Studio Pro

To configure your Windows virtual machine to work with Mendix Studio Pro, follow these steps:

1.  Open your Parallels **Control Center**:

	{{/* % image_container width="450" % */}}![parallels control center](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/windows-control-center.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
2. Click the **gear** symbol to open the **Configuration Panel**.
3.  Navigate to the **Hardware** tab, and select **Network** from the left panel:

	{{/* % image_container width="450" % */}}![network in configuration](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/windows-configuration.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
4. Make sure **Source** is set to **Shared Network**.
5. Make sure that both the **Inbound** bandwidth and **Outbound** bandwidth show **unlimited**.

	If this is not the case, either enable **Network Conditioner** and set it to a profile that does not limit bandwidth, or click the **Options** tab then the **Optimization** pane and set **Resource usage** to **No limit**.
6.  In the Parallels drop-down menu, select **Preferences**:

	{{/* % image_container width="400" % */}}![preferences in parallels](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/preferences-dropdown.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
7.  Navigate to the **Network** tab, and select **Shared** from the left panel:

	{{/* % image_container width="450" % */}}![network tab](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/parallels-preferences-no-ports.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
8.  Click the **+** button and add two ports: one for 8080 and one for 8083, both forwarded to your Windows virtual machine (the 8083 port is only necessary for developing native mobile apps):

	{{/* % image_container width="450" % */}}![plus button](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/port-setup.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
	After adding those two ports, your **Port forwarding rules** should look like this:

	{{/* % image_container width="450" % */}}![finished ports](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/parallels-preferences-ports.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
Congratulations! You have successfully configured port forwarding to enable testing Mendix apps with your Mac. 

## 4 Viewing Your App on Your Testing Device

{{% alert color="warning" %}}
Whenever you create or open a Mendix app in Mendix Studio Pro, be sure to do so from a mapped drive instead of a network drive.
{{% /alert %}}

{{% alert color="info" %}}
If you experience issues connecting with the Make It Native app, make sure your firewall is not preventing a connection. For information resolving Windows Defender and other firewall-related issues, see the [Error: Unable to Load Script](/howto/mobile/common-issues#unable-load-script) section of *Troubleshoot Common Native Mobile Issues*
{{% /alert %}}

Read the tips and steps below to view your app on your testing device:

* Correct mapped drives will always have a letter at the start of their file location:

	{{/* % image_container width="450" % */}}![mapped drive](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/mapped-drive.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
* Incorrect network drives will always have **\\** at the start of their file location:

	{{/* % image_container width="450" % */}}![network drive](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/network-drive.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
When running your app on your test device, you cannot use the QR code within Mendix Studio Pro's **View Mobile App** dialog box:

{{/* % image_container width="400" % */}}![view mobile app](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/view-mobile-app.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
Instead, you must enter your Mac's IP address into your Make It Native app. To run your app on your test device, follow the steps below:

1. Make sure your test device and Mac are on the same Wi-Fi network.
2. Place your cursor over your Wi-Fi symbol in your system tray, then and click while holding <kbd>Option</kbd> to see your Mac's advanced network information. You will see your **IP Address** in this drop-down menu.
3.  In your Make It Native app's **Host** field, type *{your IP address}:8080*:

	{{/* % image_container width="400" % */}}![ip in dev app](/attachments/howto/general/using-mendix-studio-pro-on-a-mac/ip-in-dev-app.png){{/* % /image_container % */}}
{{/* % /image_container % */}}
4. Tap **Launch** to view your app.

Congratulations! You have successfully viewed your app on a test device.

## 5 Viewing Changes to Your App on Your Testing Device

For information on how to change to your app and then see that change on your device, see the [Viewing Changes to Your App on Your Testing Device](/howto/mobile/getting-started-with-native-mobile#viewingchanges) section in *Get Started with Native Mobile*.

## 6 Read More

* [Get Started with Native Mobile](/howto/mobile/getting-started-with-native-mobile)
* [Style Your Mendix Native Mobile App](/howto/mobile/how-to-use-native-styling)