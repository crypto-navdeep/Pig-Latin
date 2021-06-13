const paragraph = `Pig Latin is a language game or argot in which English words are altered, usually by adding a fabricated suffix or by moving the onset or initial consonant or consonant cluster of a word to the end of the word and adding a vocalic syllable to create such
a suffix. For example, "Wikipedia" would become "Ikipediaway" (the "W" is moved from the beginning and has "ay" appended to create a suffix). The objective is to conceal the words from others not familiar with the rules. The reference
to Latin is a deliberate misnomer; Pig Latin is simply a form of argotor jargon unrelated to Latin, and the name is used for its English connotations as a strange and foreign-sounding language. It is most often used by young children
as a fun way to confuse people unfamiliar with Pig Latin.`;
/*
const list = `<li>- Let's take the word pig which would get translated into <code>igpay</code>. - And let's take the word <code>enlarge</code> which would get translated into <code>enlargeyay</code> Did you notice what happens ? You would think
that some bizarre word is spitted out, but no, here is how it works... Here are the rules...
</li>
<li>
- When there is a vowel at the starting the word, then the suffix <code>yay</code> would be added.
</li>
<li>
- but when there is a constant at the starting of the word, then it would cut the entire consonant cluster till it gets the vowel and stops. now the cut word is going to be attached to the last of the word and the suffix <code>yay</code>                            would be added.
</li>`; */

let pigLatinExp = document.getElementById('pig-latin-explanation');
pigLatinExp.innerText = paragraph;