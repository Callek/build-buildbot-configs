releaseConfig = {}

# Release Notification
#  not used yet
# Basic product configuration
#  Names for the product/files
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
#  Current version info
releaseConfig['version']                    = '2.12b5'
releaseConfig['appVersion']                 = '2.12'
releaseConfig['milestone']                  = '15.0'
releaseConfig['buildNumber']                = 1
releaseConfig['baseTag']                    = 'SEAMONKEY_2_12b5'
#  Old version info
releaseConfig['oldVersion']                 = '2.12b4'
releaseConfig['oldAppVersion']              = '2.12'
releaseConfig['oldBuildNumber']             = 1
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_12b4'
releaseConfig['oldRepoPath']                = 'releases/comm-beta'
#  Next (nightly) version info
#     not yet available
#  Repository configuration, for tagging
releaseConfig['skip_tag']                   = False 
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-beta' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-beta'
releaseConfig['sourceRepoRevision']         = '36e2012538ac'
releaseConfig['relbranchOverride']          = ''
#releaseConfig['productVersionFile']        = 'suite/config/version-20.txt'
releaseConfig['productVersionFile']         = ''
#   Mozilla
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-beta'
releaseConfig['mozillaRepoRevision']        = 'FIREFOX_15_0b5_BUILD1'
releaseConfig['mozillaRelbranchOverride']   = 'GECKO150_2012081422_RELBRANCH' # put Gecko relbranch here that we base upon
#   Inspector
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = '869a1de4fc3f'
releaseConfig['inspectorRelbranchOverride'] = 'DOMI_2_0_13'
#   Venkman
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = '6fcfa71a2039'
releaseConfig['venkmanRelbranchOverride']   = 'SEA2_12_RELBRANCH'
#   Chatzilla
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'e25c0b12b768'
releaseConfig['chatzillaRelbranchOverride'] = 'SEA2_12_RELBRANCH'
#  L10n repositories
releaseConfig['l10nRepoPath']               = 'releases/l10n/mozilla-beta'
releaseConfig['l10nRelbranchOverride']      = ''
releaseConfig['l10nRevisionFile']           = 'l10n-changesets-comm-beta'
#  Support repositories
#   not used yet

# Platform configuration
releaseConfig['enUSPlatforms']              = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']         = ()

# Unittests
releaseConfig['unittestPlatforms']          = ()

# L10n configuration
releaseConfig['l10nPlatforms']              = ('linux', 'win32', 'macosx64')
releaseConfig['mergeLocales']               = True

# Mercurial account
releaseConfig['hgUsername']                 = 'seabld'
releaseConfig['hgSshKey']                   = '~seabld/.ssh/seabld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']                    = ':ext:seabld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
releaseConfig['patcherConfig']              = 'mozBeta-seamonkey-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']            = 'UPDATE_PACKAGING_R14'
releaseConfig['binaryName']                 = releaseConfig['brandName']
releaseConfig['oldBinaryName']              = releaseConfig['binaryName']
releaseConfig['ftpServer']                  = 'ftp.mozilla.org'
releaseConfig['stagingServer']              = 'stage.mozilla.org'
releaseConfig['bouncerServer']              = 'download.mozilla.org'
releaseConfig['ausServerUrl']               = 'https://aus2-community.mozilla.org'
releaseConfig['testOlderPartials']          = False
releaseConfig['releaseNotesUrl']            = None
releaseConfig['releaseChannel']             = 'beta'
releaseConfig['verifyConfigs']              = {
    'linux':  'mozBeta-seamonkey-linux.cfg',
    'macosx64': 'mozBeta-seamonkey-mac64.cfg',
    'win32':  'mozBeta-seamonkey-win32.cfg'
}
releaseConfig['mozconfigs']                 = {
    'linux': 'suite/config/mozconfigs/linux32/release',
    'linux64': 'suite/config/mozconfigs/linux64/release',
    'macosx64': 'suite/config/mozconfigs/macosx-universal/release',
    'win32': 'suite/config/mozconfigs/win32/release',
}

# Major update configuration
releaseConfig['majorUpdateRepoPath']        = None

# Tuxedo/Bouncer related - XXX: atm not allowed for SeaMonkey
#releaseConfig['tuxedoConfig']              = 'seamonkey-tuxedo.ini'
#releaseConfig['tuxedoServerUrl']           = 'https://bounceradmin.mozilla.com/api/'
