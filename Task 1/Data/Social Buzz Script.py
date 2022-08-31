#Path for Git is 'C:/Users/bongi/OneDrive/Bongiwe_Documents/Academics/Forage/'

#import libraries
import pandas as pd

#import data
SB_Content = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\Content (1).csv")
SB_Location = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\Location (1).csv")
SB_Profile = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\Profile (1).csv")
SB_Reactions = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\Reactions (1).csv")
SB_ReactionTypes = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\ReactionTypes (1).csv")
SB_Session = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\Session (1).csv")
SB_User = pd.read_csv(r"C:\Users\bongi\OneDrive\Bongiwe_Documents\Academics\Forage\Task 1\Data\User (1).csv")

#inspect data
SB_Location.describe()