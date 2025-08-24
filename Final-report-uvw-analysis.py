#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Jupyter magic command to enable the inline plotting mode
get_ipython().run_line_magic('matplotlib', 'inline')

# specify the filenames for US Census Bureau data (expects to find them locally in same dir as code)
names_filename = 'adult.names.txt'
data_filename = 'adult.data.txt'

# Initialize an empty list to store attribute names
attribute_names = []

# Read the attribute names from 'adult.names.txt'
with open(names_filename, 'r') as file:
    for line in file:
        if ':' in line and '|' not in line and '>' not in line:
            attribute_name = line.split(':')[0].strip()
            attribute_names.append(attribute_name)

# Add the 'income' column to the attribute names to hold <=50K and >50K
attribute_names.append('income')

# Read the data from 'adult.data.txt' and populate the DataFrame
df_data = pd.read_csv(data_filename, header=None, names=attribute_names, skipinitialspace=True)

# Drop the entire 'fnlwgt' column from the DataFrame (axis=1 means column)
df_data = df_data.drop('fnlwgt', axis=1)

# List of columns containing '?'
columns_with_question_mark = ['workclass', 'occupation', 'native-country']

# Apply the cleaning operation to specified columns: replace '?' with None for the entire DataFrame
for column in columns_with_question_mark:
    df_data[column] = df_data[column].apply(lambda x : x.strip() if x.strip() != '?' else None)

# set 'income' column as a categorical variable for proper ordering
df_data['income'] = pd.Categorical(df_data['income'], categories=['<=50K', '>50K'], ordered=True)


### DEBUG
#
#print('attribute_names: ', attribute_names)
#print('attribute_names len: ', len(attribute_names))

#print(df_data)
#print(df_data.head(60))
#
### 


# In[2]:


## break data down into smaller categories to be used to simplify visualizations
# define the education mapping to group into qualitative data into smaller categories
education_mapping = {
    'Preschool': 'Preschool',
    '1st-4th': '1st-8th Grade',
    '5th-6th': '1st-8th Grade',
    '7th-8th': '1st-8th Grade',
    '9th': '9th-12th Grade',
    '10th': '9th-12th Grade',
    '11th': '9th-12th Grade',
    '12th': '9th-12th Grade',
    'HS-grad': 'HS Graduate',
    'Some-college': 'Some College',
    'Assoc-acdm': 'Associate',
    'Assoc-voc': 'Associate',
    'Bachelors': 'Bachelors',
    'Masters': 'Masters',
    'Prof-school': 'Prof. School',
    'Doctorate': 'Doctorate'
}

# create a new column 'education_grouped' based on the mapping
df_data['education_grouped'] = df_data['education'].map(education_mapping)

# Specify the order of categories for the x-axis
order = [
    'Preschool',
    '1st-8th Grade',
    '9th-12th Grade',
    'HS Graduate',
    'Some College',
    'Associate',
    'Bachelors',
    'Masters',
    'Prof. School',
    'Doctorate'
]

# Define age categories
age_bins = [17, 20, 30, 40, 50, 60, 70, 80, 90]

# Define labels for the age categories
age_labels = ['17-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '81-90']

# Create a new column 'age_grouped' based on the age categories
df_data['age_grouped'] = pd.cut(df_data['age'], bins=age_bins, labels=age_labels, right=False)

### DEBUG
#
#print(df_data['age_grouped'].value_counts())


# In[3]:


## Education vs income bar chart

# Set the figure size
plt.figure(figsize=(10, 6))

# Create the countplot with seaborn with specified order
#sns.countplot(x='education_grouped', hue='income', data=df_data, palette='pastel', order=order)
#sns.countplot(x='education_grouped', hue='income', data=df_data, palette='viridis', order=order)
#sns.countplot(x='education_grouped', hue='income', data=df_data, order=order)
sns.countplot(x='education_grouped', hue='income', data=df_data, palette=['#528bd9', '#f08b18'], order=order)   # 528bd9 = blue, f08b18 = orange


# set x-axis labels by 45 degrees and font size
plt.xticks(rotation=45, ha='right', fontsize=10)

# add labels and title to plot
plt.title('Impact of Education Level on Income')
plt.xlabel('Education Level')
plt.ylabel('Number of Adults')

# add annotations (labels) for each bar using get current axes method
for p in plt.gca().patches:
    plt.gca().annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)

# set Seaborn style and context
#sns.set(style="whitegrid")

# enable gridlines
#plt.grid(True)

# show the plot
plt.show()

## DEBUG
#print(df_data.head(60))
#print('Total Records: ', len(df_data))


# In[4]:


# Stacked bar chart for Income vs Education


# Reshape the DataFrame to have separate columns for '<=50K' and '>50K'
df_stacked = df_data.groupby(['education_grouped', 'income']).size().unstack().fillna(0)

# Reorder the index according to the specified order
#df_stacked = df_stacked.reindex(order)

# Set the figure size
#plt.figure(figsize=(12, 8))

# Create the stacked bar chart with seaborn
#df_stacked.plot(kind='bar', stacked=True, color=['#acc2e3', '#e6ad8e'], width=0.8)  # pastel colors
df_stacked.plot(kind='bar', stacked=True, color=['#799ac7', '#eda95a'], width=0.8)

# Rotate x-axis labels by 45 degrees for better readability
plt.xticks(rotation=45, ha='right')

# add annotations (labels) for each bar using get current axes method
#for p in plt.gca().patches:
#    plt.gca().annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
#                       ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize=8)


# Add labels and title
plt.title('Impact of Education on Income')
plt.xlabel('Education Level')
plt.ylabel('Number of Adults')

# Show the plot
plt.show()


# In[5]:


from statsmodels.graphics.mosaicplot import mosaic

# Assuming you already have the 'df_data' DataFrame and 'attribute_names' list

# Set the figure size
#plt.figure(figsize=(12, 8))


# Set the figure size
#plt.figure(figsize=(12, 8))
plt.figure(figsize=(16, 12))

# Create the mosaic plot
#mosaic_data = df_data.groupby(['marital-status', 'sex', 'income']).size().unstack().fillna(0)
#mosaic_data = df_data.groupby(['marital-status', 'sex', 'income']).size().unstack().fillna(0)
#mosaic(mosaic_data.stack(), title='Mosaic Plot of Marital Status and Sex vs Income', gap=0.01)

# Create the mosaic plot
#mosaic_data = df_data.groupby(['marital-status', 'sex', 'income']).size().unstack().fillna(0)
#labelizer_func = lambda k: f"{k} ({mosaic_data.stack()[k]})"
#mosaic(mosaic_data.stack(), title='Mosaic Plot of Marital Status and Sex vs Income', gap=0.01, axes_label=True, labelizer=labelizer_func)


# Add labels and title
plt.xlabel('Marital Status and Sex')
plt.ylabel('Income')
plt.show()


# In[6]:


# Assuming you already have the 'df_data' DataFrame and 'attribute_names' list
'''
# Set the figure size
plt.figure(figsize=(12, 8))

# Specify the columns for the parallel coordinate plot
columns_to_plot = ['age', 'workclass', 'race']

# Create the parallel coordinate plot
pd.plotting.parallel_coordinates(df_data.sample(1000), class_column='income', color=['#66c2ff', '#ffb266'])

# Add legend
plt.legend(title='Income', loc='upper right')

# Add labels and title
plt.title('Parallel Coordinate Plot of Selected Attributes vs Income')
plt.xlabel('Attributes')
plt.ylabel('Values')

# Show the plot
plt.show()
'''


# In[7]:


print("Minimum Age:", df_data['age'].min())
print("Maximum Age:", df_data['age'].max())


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming you already have the 'df_data' DataFrame, 'order' list, and 'education_mapping' dictionary

# Create a new DataFrame with counts for 'income' and 'total data count' for each 'occupation' and 'age_grouped'
df_stacked = df_data.groupby(['occupation', 'age_grouped', 'income']).size().unstack().fillna(0)

# Reorder the index according to the specified order
#df_stacked = df_stacked.reindex(order)

# Reset the index to make 'occupation' a regular column
#df_stacked = df_stacked.reset_index()

# Set the figure size
plt.figure(figsize=(12, 8))

# Create the stacked bar chart with Pandas plotting
#df_stacked.plot(kind='bar', x='occupation', y=['<=50K', '>50K'], stacked=True, color=['#799ac7', '#eda95a'], width=0)
df_stacked.plot(kind='bar', y=['<=50K', '>50K'], stacked=True, color=['#799ac7', '#eda95a'], width=0)

# Rotate x-axis labels by 45 degrees for better readability
plt.xticks(rotation=45, ha='right')

# Add labels and title
plt.title('Stacked Bar Chart of Income and Total Data Count by Occupation and Age Group')
plt.xlabel('Occupation')
plt.ylabel('Count')

# Show the plot
plt.show()


# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named df_data with columns 'age', 'occupation', and 'income'

# Filter the data for individuals earning >$50,000 USD
df_high_income = df_data[df_data['income'] == '>50K']

# Set the figure size
plt.figure(figsize=(16, 8))

# Create a stacked bar chart using Seaborn with 'age' as hue
sns.countplot(x='occupation', hue='age_grouped', data=df_high_income, palette='viridis', order=df_high_income['occupation'].unique())

# Add labels and title
plt.title('Distribution of Income >$50,000 USD Across Occupation and Age')
plt.xlabel('Occupation')
plt.ylabel('Count')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Move the legend inside the plot area
#plt.legend(title='Age', loc='upper left', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()


# In[10]:


# Assuming df_data is your DataFrame
unique_age_counts = df_data['age'].value_counts()

# Print or display the result
print(unique_age_counts)


# In[11]:


import pandas as pd

# Assuming df_data is your DataFrame
distinct_native_countries = df_data['native-country'].nunique()

# Print or display the result
print("Number of distinct native countries:", distinct_native_countries)


# In[12]:


import pandas as pd

# Assuming df_data is your DataFrame
distinct_education_levels = df_data['education'].nunique()

# Print or display the result
print("Number of unique education levels:", distinct_education_levels)

