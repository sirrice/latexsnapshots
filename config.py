###########################################
#
#    Required
#
##########################################


# absolute path to the git_repo
git_repo = "/tmp/animated"

# what name for the paper?
paper_name = "infovis16_approx"

# the latex document directory (within the git repo)
latex_dir = "docs/infovis16_approx"

def make_cmds(dstpath):
  """
  @param dstpath Where the generated latex file should be moved to
  @return a list of commands to run to generate the latex file and move it to dstpath
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

# where to store the data, no need to change this
dburi = "sqlite:///latex2.db"

