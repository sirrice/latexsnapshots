###########################################
#
#    Required
#
##########################################


# absolute path to the git_repo
# Make sure things are committed!  
# We will need to checkout many commit points as part of the rollback procedure.
git_repo = "/tmp/animated"

# what name for the paper?
paper_name = "infovis16_approx"

# the latex document directory (within the git repo)
latex_dir = "docs/infovis16_approx"

# A function that returns shell commands for compiling the latex doc and 
# copying it to the destination location
def make_cmds(dstpath):
  """
  @param dstpath Where the generated latex file should be moved to
  @return a list of shell commands to run to generate the latex file and move it to dstpath
  """
  cmds = [
    "cd /tmp/animated/docs/infovis16_approx",
    "latexrun main",
    "cp latex.out/main.pdf %s" % dstpath
  ]
  return cmds


###########################################
#
#    Optional
#
##########################################

# minimum edit distance of tex files to take a snapshot
min_edit_distance = 4000

# Don't create a snapshot if the previous one was within X hours of this commit
min_hours_gap = 12

# where to store the data, no need to change this
dburi = "sqlite:///latex2.db"

