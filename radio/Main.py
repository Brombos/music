from git import Repo

repo = Repo('/media/dandan/Lakkaa/github/music/Music')
tree = repo.head.commit.tree
repo.index.commit("Song Change")
#origin = repo.create_remote("origin", repo.remotes.origin.url)
#origin.push()
 