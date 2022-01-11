import logging
import argparse

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class GitRepo(object):
    def __init__(self, path='', component='', id=''):
        self.path = path
        self.component = component
        self.id = id

    def __repr__(self):
        return 'GitRepo(%r, %r, %r)' % (self.path, self.component, self.id)


mapping = [
    ('GLOSS/gloss_repo', 'IPE', 712),
    ('GLOSS/BPS', 'BPS', 1279),
    ('GLOSS/CREST', 'CREST', 1298),
    ('GLOSS/SWIFT', 'SWIFT', 1299),
    ('GLOSS/PRINT', 'PRINT', 1292),
    ('GLOSS/dds', 'ACDDM', 2654),
    ('GLOSS/TRAX', 'TRAX', 1293),
    ('GLOSS/esb', 'EAI', 1534),
    ('GLOSS/EB_283', 'EB_283', 1288),
    ('GLOSS/EURO', 'EURO', 1297),
    ('GLOSS/Gloss-FIFO', 'FIFO', 1280),
    ('GLOSS/CC_169', 'CC_169', 1285),
    ('GLOSS/CTM', 'CTM', 1538),
    ('GLOSS/CCASS', 'CCASS', 1294),
    ('GLOSS/tmi', 'TMI', 4217),
    ('GLOSS/gloss-te', 'TE', 941),
    ('GLOSS/te-core', 'TE', 2528),
    ('GLOSSjava/gpm', 'PP', 2637),
    ('GLOSSjava/gpl', 'PP', 2640),
    ('GLOSSjava/integrity-check', 'PP', 2649),
    ('GLOSSjava/master-build', 'PP', 2646),
    ('GLOSSjava/gsl', 'PP', 2639),
    ('GLOSSjava/jec', 'PP', 2641),
    ('GLOSSjava/framework', 'PP', 2636),
    ('GLOSSjava/mob', 'PP', 2644),
    ('GLOSSjava/mor', 'PP', 2645),
    ('GLOSSjava/rebuilder', 'PP', 2647),
    ('GLOSSjava/cfs', 'PP', 2643),
    ('GLOSSjava/product-installer', 'Product_Installer', 2546),
    ('GLOSSjava/ccpne', 'CCPNE', 2652),
]

repo_list = [GitRepo(*r) for r in mapping]


def find_repo(attribute, value):
    """Lookup Git Repo by attribute"""

    def first(iterable, default=None):
        """Helper function that returns first item in an iterable"""
        for item in iterable:
            return item
        return default

    g = GitRepo()
    valid_attributes = list(g.__dict__.keys())
    if attribute in valid_attributes:
        return first(repo for repo in repo_list if getattr(repo, attribute) == value)
    else:
        raise AttributeError('%r is not an attribute of the %r class' % (attribute, g.__class__.__name__))


def list_components():
    """Return list of Jira Components valid for builds"""
    components = list(set([repo.component for repo in repo_list]))
    components.sort()
    return components


_build_components = list_components()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Return project id for selected component')
    parser.add_argument('-c', '--component', help='Component', type=str, required=True)
    args = parser.parse_args()

    repo = find_repo('component', args.component)
    if repo:
        print(repo.id)
    else:
        exit(1)
