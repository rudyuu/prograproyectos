s=input('Insert a word: ', 's');
Number_of_vowels = vowelcounts(s)  %function calling
function w = vowelcounts(s)        %function definition
w=0;
l=length(s);
for i=1:l
if s(i)=='a' || s(i)=='e' || s(i)=='i' || s(i)=='o' || s(i)=='u'
    w=w+1;
else 
    continue
end
endfor
endfunction