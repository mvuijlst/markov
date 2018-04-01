import markovify

# Get raw text as string.
with open("source/vb2014.txt") as f:
    textA = f.read()
with open("source/spagroen2012.txt") as f:
    textB = f.read()
with open("source/nvagent2012.txt") as f:
    textC = f.read()

# Build the model.
textA_model = markovify.Text(textA)
textB_model = markovify.Text(textB)
textC_model = markovify.Text(textC)

model_combo = markovify.combine([ textA_model, textB_model, textC_model ], [ 1, 1, 1 ])


for i in range(30):
    # print(text_model.make_short_sentence(140))
    candidate = model_combo.make_sentence(max_overlap_total=8)

    if (candidate!='None'):
        print(candidate)