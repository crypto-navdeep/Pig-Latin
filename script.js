"use strict"

function convert(original) {

    let originalArray = original.split(' ');
    let convertedArray = [];

    for (let originalWord of originalArray) {
        if ('aeiou'.includes(originalWord[0])) convertedArray.push(originalWord + "yay");
        else {
            let vowelIndex = 0;
            for (let letter of originalWord) {
                // Loop through until the first vowel is found
                if ('aeiou'.includes(letter)) {
                    vowelIndex = originalWord.indexOf(letter);
                    break
                }
            }
            // Compose final wording
            // let convertedCons = originalWord.slice(vowelIndex + originalWord.slice(0, vowelIndex)) + "ay";
            let convertedCons = originalWord.slice(0, vowelIndex) + "ay";
            convertedArray.push(convertedCons);
        }
    }
    let convertedSentence = convertedArray.join(" ");
    return convertedSentence;
};

// Example
// console.log(convert('the quick brown fox jumps over the lazy dog'));

// Get it from DOM

let inputButton = document.getElementById('input-btn');

function iExecuteWhatIamProgrammedFor() {
    let originalText = document.getElementById('input-text');
    let pigLatinPara = document.getElementById('output-text');
    console.log(originalText.value);
    pigLatinPara.innerHtml = convert(originalText.value);
};

inputButton.addEventListener('click', iExecuteWhatIamProgrammedFor());