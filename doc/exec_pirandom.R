pdf("pirandom.pdf")   # define graphical output file
source("pirandom.R")  # execute the script, making any function defined in it available
pirandom(1000)        # execute the function
dev.off()             # close the graphical output file
