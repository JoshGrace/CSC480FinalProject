# CSC480

# setup instructions
make sure you have a healthcare-provider-fraud-detection-analysis with all the csv files
run ./setupFacts.sh this will generate all the _facts.clp files

# running clips
run ./startClipsFacts.sh this will start clips and pipe all the commands in startClipsCommands.txt to clips

# developing
create new rules files and add a line in startClipsCommands.txt to load the rules file.
Make sure to run findIdealLevel.py after ./starClipsFacst.sh

# Key Project Files
Sorry about the mess! Make sure that you're on the *insights* branch for the most up to date project files.
* *_template.clp - Template files generated from annotated data.
* *_facts.clp - Fact files of annotated data.
* rule2.clp - All the rules used to find fraudulent providers.
* startClipsCommands.txt - Used to load all the facts, templates, and rules into clips.
* outputfraudfound.txt - A list of all the providers who have been flagged as fraudulent.
* findIdealLevel.py - Used to find the optimal number of flags for the given data set.
