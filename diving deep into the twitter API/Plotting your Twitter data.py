#Now  you have the number of tweets that each candidate was mentioned in, 
#you can plot a bar chart of this data.  use the statistical data visualization library seaborn
# You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot,
#passing it two arguments:

#a list of labels and
#a list containing the variables you wish to plot (clinton, trump and so on.).

#Import both matplotlib.pyplot and seaborn using the aliases plt and sns, respectively.
#Complete the arguments of sns.barplot: the first argument should be the labels to appear on the x-axis;
#the second argument should be the list of the variables you wish to plot, as produced in the previous exercise.

# Import packages
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz)
ax.set(ylabel="count")
plt.show()



