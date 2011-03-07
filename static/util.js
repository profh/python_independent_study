function make_req() {
		var req = false;
      if (window.XMLHttpRequest) {
        try {
          req = new XMLHttpRequest();
        } catch (e) {
          req = false;
        }
      } else if (window.ActiveXObject) {
        try {
          req = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
          try {
            req = new ActiveXObject("Microsoft.XMLHTTP");
          } catch (e) {
            req = false;
          }
        }
      }
	  return req;
}

// Perform an ajax request. 
// Pass a url and it returns the contents of the page.
function request(url) {
	req = make_req();
    if (req) {
        req.open('GET', url, false);
        req.send(null);
        response = req.responseText;
        if (response.length > 0)
        	return response;
        else
        	return "No Results Found";
    } 
	else {
      	return "No Results Found";
    }
}
function CopyToClipboard(data) {
      var copyText = data;
      if (window.clipboardData) { // IE send-to-clipboard method.
            window.clipboardData.setData('Text', copyText);
      } else if (window.netscape) {
            // You have to sign the code to enable this or allow the action in about:config by changing user_pref("signed.applets.codebase_principal_support", true);
            netscape.security.PrivilegeManager.enablePrivilege('UniversalXPConnect');
            
            // Store support string in an object.
            var str = Components.classes["@mozilla.org/supports-string;1"].createInstance(Components.interfaces.nsISupportsString);
            if (!str) return false;
            str.data=copyText;
            
            // Make transferable.
            var trans = Components.classes["@mozilla.org/widget/transferable;1"].createInstance(Components.interfaces.nsITransferable);
            if (!trans) return false;
            
            // Specify what datatypes we want to obtain, which is text in this case.
            trans.addDataFlavor("text/unicode");
            trans.setTransferData("text/unicode",str,copyText.length*2);
            
            var clipid=Components.interfaces.nsIClipboard;
            var clip = Components.classes["@mozilla.org/widget/clipboard;1"].getService(clipid);
            if (!clip) return false;
            
            clip.setData(trans,null,clipid.kGlobalClipboard);
      }
}
function CopyTemplateToClipboard(chapter, exercise){
	
	var chapter = prompt("What Chapter Number");
	var exercise = prompt("What Exercise Number");
	
	var templateString = "";
	
	templateString += "# Chapter:\t\t"+chapter+"\r\n";
	templateString += "# Exercise:\t\t"+exercise+"\r\n";
	templateString += "# Start:\t\t"+request("CurTimestamp")+"\r\n";
	templateString += "# End:\t\t\t___________" + "\r\n";
	templateString += "# Rating:\t\t___________" + "\r\n";
	templateString += "# Note:\t\t\t___________" + "\r\n";

	CopyToClipboard(templateString);
	alert("Template Copied to Clipboard");
}
function CopyTimeToClipboard(){
	CopyToClipboard(request('CurTimestamp'));
	alert("Time Copied to Clipboard");
}

function createNewTemplate(){
	chapter = prompt("What Chapter Number");
	exercise = prompt("What Exercise Number");
	if (chapter == null || exercise == null){
		alert("You must specify a chapter and exercise");
		return;
	}
	alert(request("/python/index/newTemplate?chap="+chapter+"&exer="+exercise));
	

}