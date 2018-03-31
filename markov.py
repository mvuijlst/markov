import markovify

# Get raw text as string.
with open("source/nvagent2012.txt") as f:
    textA = f.read()
with open("source/comm.txt") as f:
    textB = f.read()

# Build the model.
textA_model = markovify.Text(textA)
textB_model = markovify.Text(textB)

model_combo = markovify.combine([ textA_model, textB_model ], [ 1, 1 ])


for i in range(30):
    # print(text_model.make_short_sentence(140))
    candidate = model_combo.make_sentence(max_overlap_total=8)

    if (candidate!='None'):
        print(candidate)