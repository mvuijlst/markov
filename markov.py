import markovify
import codecs

# Get raw text as string.
#with open("source/vb2014.txt", encoding="latin-1") as f:
#    textA = f.read()
with open("source/huizinga.txt", encoding="latin-1") as f:
    textB = f.read()
with open("source/johannes.txt", encoding="latin-1") as f:
    textC = f.read()

# Build the model.
#textA_model = markovify.Text(textA)
textB_model = markovify.Text(textB)
textC_model = markovify.Text(textC)

model_combo = markovify.combine([ textB_model, textC_model ], [ 1, 1 ])

out = codecs.open("output.txt", "w+", "utf8")

for i in range(300):
    # print(text_model.make_short_sentence(140))
    candidate = model_combo.make_sentence(max_overlap_total=8)

    if (candidate!='None'):
        #print(candidate)
        out.write(candidate+"\r\n")