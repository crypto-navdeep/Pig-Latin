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
}


function convert_1() {
    originalValue = document.getElementById("original_sentence").value;
    document.getElementById("pig_latined").value = convert(originalValue);
}