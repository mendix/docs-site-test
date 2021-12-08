---
title: "Build JavaScript Actions: Part 1 (Basic)"
url: /howto/extensibility/write-javascript-actions
parent: "build-javascript-actions"
menu_order: 10
description: "This how-to will teach you to create a JavaScript action."
tags: ["widget", "TexttoSpeech", "SpeechtoText", "JavaScript", "API", "JavaScript-API"]
---

## 1 Introduction

Nanoflows are more powerful with pluggable nanoflow actions — called JavaScript actions. With JavaScript actions, the standard set of actions can be extended with new functionality. A JavaScript action is a reusable action based on JavaScript that runs in the client just like the nanoflow, and can use capabilities such as HTML5 browser functions, Cordova plugins, and React Native modules. JavaScript actions are similar to [Java actions](/refguide/java-actions), but run on the client instead of the server. To share them inside your organization, JavaScript actions can be distributed and downloaded through the private [Mendix Marketplace](https://marketplace.mendix.com/).

**This how-to will teach you how to do the following:**

* Create a JavaScript action
* Configure input and output parameters
* Implement web text to speech
* Make an asynchronous return
* Expose an action as a nanoflow action
* Use your actions in a demo

## 2 Create a JavaScript action: TextToSpeech

To create a JavaScript action that can synthesize text to speech, follow these steps:

1.  In the **App Explorer**, right-click the module you would like to add a new JavaScript action to and select **Add other** >**JavaScript action**.

2.  Give the JavaScript action a descriptive name:

	![naming dialog](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/descriptivename.png)

	You can now start creating the API for the JavaScript action, which consists of parameters and a return type.

3.  Your **TextToSpeech** action only requires a single parameter. Create it by clicking the **Add** button in the top left corner. Give the parameter a name and add an extended description if desired:

	![javascript action description field](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/jsactiondescription.png)

	You can leave the **Return type** at the default Boolean value. That means that the action will return `false` if no text is provided, and return `true` after it has successfully spoken the provided text.
  
4.  Next, click the **Code** tab to begin editing the JavaScript action. Now you can start writing the actual action. Mendix Studio Pro already created a default template for you, using the parameters and return type we provided:

	![text to speech code](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/code.png)

	You can only add code between `// BEGIN USER CODE` and `// END USER CODE`. Any code outside this block will be lost. The source code is stored in your app folder under **javascriptsource** > **(module name)** > **actions** > **(action name).js**. This JavaScript action will be asynchronous, so you will be using promises to return values (for details about using promises, see Mozilla's [Using promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) guide). 

5. Now add a check to verify if the required parameter has been set correctly. The action will return `false` if no text was provided:

	```javascript
	export async function TextToSpeech(text) {
		// BEGIN USER CODE
		if (!text) {
			return false;
		}
		throw new Error("JavaScript action was not implemented");
		// END USER CODE
	}
	```

6. To enable spoken text, you will need the [Web SpeechSynthesis API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis). However, not all browsers support this experimental API. Add a check to verify if the API is available, and include an error if it is not. For future reference, add a comment with references to documentation about our API and its compatibility.

	```javascript
	export async function TextToSpeech(text) {
		// BEGIN USER CODE
		// Documentation: https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis
		// Compatibility: https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis#Browser_compatibility
		if (!text) {
			return false;
		}
		if ("speechSynthesis" in window === false) {
			throw new Error("Browser does not support text to speech");
		}
		throw new Error("JavaScript action was not implemented");
		// END USER CODE
	}
	```

7. Next up is the fun part: making the application speak. Create a new `SpeechSynthesisUtterance` object and call the `speak` function. You will write this new code by overwriting the last `Return` from the previous code.

	```javascript
	export async function TextToSpeech(text) {
		// BEGIN USER CODE
		if (!text) {
			return false;
		}
		if ("speechSynthesis" in window === false) {
			throw new Error("Browser does not support text to speech");
		}
		const utterance = new SpeechSynthesisUtterance(text);
		window.speechSynthesis.speak(utterance);
		return true;
		// END USER CODE
	}
	```

8. The function will already return even when the browser is not finished speaking. To prevent this we can attach `onend` and `onerror` handlers to it. The `onend` handler runs when the application finishes speaking the text, so the promise resolves with a value of `true`. In case an error occurs, the promise is rejected and a descriptive error message is shown. After attaching these handlers, it can start speaking:

	```javascript
	export async function TextToSpeech(text) {
		// BEGIN USER CODE
		if (!text) {
			return false;
		}
		if ("speechSynthesis" in window === false) {
			throw new Error("Browser does not support text to speech");
		}
		// const utterance = new SpeechSynthesisUtterance(text);
		// window.speechSynthesis.speak(utterance);
		// return true;
		return new Promise(function(resolve, reject) {
			const utterance = new SpeechSynthesisUtterance(text);
			utterance.onend = function() {
				resolve(true);
			};
			utterance.onerror = function(event) {
				reject("An error occured during playback: " + event.error);
			};
			window.speechSynthesis.speak(utterance);
		});
		// END USER CODE
	}
	```

9. You have just implemented your first JavaScript action! You can start using the action in your nanoflows by adding a **JavaScript action call** and selecting the newly created **SpeechToText** action: 

	![select text to speech action](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/selectjsactioncalldetail.png)
	
	Optionally, you can expose the JavaScript action as a nanoflow action. When you do, you can choose a **Caption**, **Category**, and **Icon**. Note that to choose an icon your image will need to be included in an existing [image collection](/refguide/image-collection). 
	
	![add caption category and icon](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/exposeasnanoflow.png)
	
	It will then appear in the **Toolbox** window when editing a nanoflow: 
	
	![text to speech in nanoflow](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/iconintoolbox.png)

10. Now for a JavaScript action test run! First, make a nanoflow which features your new JavaScript action. Right-click your folder in the **App Explorer** and click **Add nanoflow**. Then, add an action to your nanoflow, select **call a nanoflow action**, and select your JavaScript action. You will see a window which will let you edit the JavaScript action. Click the **Edit** button of the **Input Text** and type *‘Hello world'*. Then, set **Use return value** to *No* radio button.

	![edit text in call javascript action dialog](/attachments/howto/extensibility/build-javascript-actions/write-javascript-actions/calljsactionnanoflow.png)

11. Now you are going to put your new nanoflow to work. On a page of your app, make an action button by clicking **Add widget** in the top center toolbar. Then, under **Buttons**, select **Call nanoflow button**. Select your new nanoflow when prompted. 

12. Click a place on your page to drop your new button where you want it. With the button now on your page, you can test your work. Run your model, click your new button, and if your sound is on you should be greeted by the voice you programmed! 

## 3 Read More{#read-more}

* [Build JavaScript Actions: Part 2 (Advanced)](write-javascript-github)
* [Implement Best Practices for JavaScript Actions](best-practices-javascript-actions)
* [JavaScript Actions](/refguide/javascript-actions)
* [Mendix Client API](https://apidocs.rnd.mendix.com/8/client/index.html) 
* JavaScript Resources:
	* [JavaScript basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
	* [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
	* [Async functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Async_await)