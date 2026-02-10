
#task1
import numpy as np
scores=np.random.randint(50,101 , size=(5,3))
subject_means=scores.mean(axis=0)
centered_scores = scores - subject_means
print("Original Scores (Students x Subjects):")
print(scores)

print("\nMean of Each Subject:")
print(subject_means)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)



#task 2
data=np.arange(24)
reshape_data=data.reshape(4,3,2)
final_data=reshape_data.transpose(0, 2, 1)
print("Final shape:",final_data.shape)
print("Final Array:")
print(final_data)