import subprocess
import os


def gh_deploy(config):
    if not os.path.exists('.git'):
        print 'Cannot deploy - this directory does not appear to be a git repository'
        return

    print "Copying '%s' to `gh-pages` branch and pushing to GitHub." % config['site_dir']
    try:
        subprocess.check_call(['ghp-import', '-p', config['site_dir']])
    except:
        return

    url = subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
    url = url.decode('utf-8').strip()
    host, path = url.split(':', 1)
    username, repo = path.split('/', 1)
    if repo.endswith('.git'):
        repo = repo[:-len('.git')]
    print 'Your documentation should shortly be available at: http://%s.github.io/%s' % (username, repo)
