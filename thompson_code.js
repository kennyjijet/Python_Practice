
aaaaabbbcccc
a5b3c4

function countChars(input) { 
    var strResult = "", count = 1, tempStr = "";
    input.split("").forEach(element => {
        console.log(element);
        console.log(tempStr);
        if (tempStr != element) {
            if (tempStr != "") { 
                strResult += tempStr;
                strResult += count;
            }
            tempStr = element;
            count = 1;
        } else if (tempStr == element) { 
            count++;
        }
    });
    strResult += tempStr;
    strResult += count;
    
    console.log(strResult);
}

countChars("aaabbccdd");