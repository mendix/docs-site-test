---
title: "IMAP/POP3 Incoming Email"
url: /appstore/modules/imap/
category: "Modules"
description: "Describes the configuration and usage of the IMAP/POP3 Incoming Email module, which is available in the Mendix Marketplace."
tags: ["marketplace", "marketplace component", "imap", "pop3", "incoming email", "encryption", "platform support"]
#If moving or renaming this doc file, implement a temporary redirect and let the respective team know they should update the URL in the product. See Mapping to Products for more details.
---

## 1 Introduction

The [IMAP/POP3 Incoming Email](https://marketplace.mendix.com/link/component/1042/) module enables your app to retrieve emails from POP3, POP3S, IMAP, and IMAPS servers. In order for Mendix to act on incoming email, you can implement this module and model all the actions around it.

### 1.1 Typical Usage Scenario

* Retrieve emails and act like an email client, which is the recommended approach when hosting your application in the Mendix Cloud

### 1.2 Features

* Configuration of multiple accounts
* Supported protocols:
	* POP3 and POP3S
	* IMAP and IMAPS
* Actions to be performed after receiving emails:
	* Delete from server
	* Move to a folder (for example, an archive)

## 2 Configuration

The basic setup and reception of emails can be done using the **EmailAccount_Overview** example page.

To invoke receiving emails from an account, you can call the **RetrieveEmailMessages** Java action.

Set the **EncryptionKey** constant for email account passowrd encryption.
