punctuations = "!()–[]{};:'\",<>.?/@#$%^&*_~"

text = "Hello!!!, Python -- is great: isn't it?"

no_punct = ""
for char in text:
    if char not in punctuations:
        no_punct += char

print("Original String:", text)
print("String without Punctuations:", no_punct)
