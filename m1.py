import markovify
import codecs

# Get raw text as string.
with open("source/nyt.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

out = codecs.open("output.txt", "w")

for i in range(300):
    candidate = text_model.make_sentence(max_overlap_total=8)

    if (candidate!='None'):
        print(candidate)
        #out.write(candidate+"\r\n")