from bleurt import score

checkpoint = "D:/Applications/Programming/Python/Python310/Lib/site-packages/bleurt/test_checkpoint"
references = ["Sun on the ocean at the beach."
 "699pp."
 "With a price like this, you'll be floating on air." 
 "The wings of china." 
 "The dreams of the world."
 "Land your dream." 
 "Air China." 
 "Entire world." 
 "Free with every van." 
 "Forget winter." 
 "Escape to the sun." 
 "Dream bigger." 
 "Virgin holiday Sale." 
 "Boarding pass." 
 "Fly high with Turkey"]
candidates = ["Book now"]
#Score is determined as -1.306936502456665. The score is supposed to be between 0 and 1, where 0 is random and 1 is a perfect match.
#The current score would indicate a random output without context. By the first look, book now could be a fitting text for a picture of a beach in the context of a travel advertisement.
#The exact evaluation of the score by BLEURT needs to be evaluated, if only longer sentences are scored higher than short sentences.
#The script scores.py needed to use int64 input tokens as described in https://github.com/yongchanghao/bleurt/commit/e2a36c2bc9bbaef2d18b04eff105fc65466a55ad

scorer = score.BleurtScorer(checkpoint)
scores = scorer.score(references=references, candidates=candidates)
assert type(scores) == list and len(scores) == 1
print(scores)
