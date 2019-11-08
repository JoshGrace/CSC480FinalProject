# CSC480

# setup instructions
make sure you have a healthcare-provider-fraud-detection-analysis with all the csv files
run ./setupFacts.sh this will generate all the _facts.clp files

# running clips
run ./startClipsFacts.sh this will start clips and pipe all the commands in startClipsCommands.txt to clips

# developing
create new rules files and add a line in startClipsCommands.txt to load the rules file
