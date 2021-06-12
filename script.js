function convert(original) {

    let originalArray = original.split(" ");
    let convertedArray = []

    for (let originalWord of originalArray) {
        if ('aeiou'.includes(originalWord[0])) convertedArray.push(originalWord + "yay");
        else {
            for (let letter of originalWord) {
                // Loop through until the first vowel is found
                if ('aeiou'.includes(letter)) {
                    vowelIndex = originalWord.indexOf(letter);
                    break
                }
            }
            // Compose final wording
            let convertedCons = originalWord.slice(vowelIndex) + originalWord.slice(0, vowelIndex) + "ay";
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

inputButton.addEventListener('click', function() {
    let originalText = document.getElementById('input-text');
    console.log(originalText.value);
})