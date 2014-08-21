releaseConfig = {}

# Release Notification
#  not used yet
# Basic product configuration
#  Names for the product/files
releaseConfig['productName']                = 'seamonkey'
releaseConfig['brandName']                  = 'SeaMonkey'
releaseConfig['appName']                    = 'suite'
#  Current version info
releaseConfig['version']                    = '2.29b1'
releaseConfig['appVersion']                 = '2.29'
releaseConfig['milestone']                  = '32.0'
releaseConfig['buildNumber']                = 1
releaseConfig['baseTag']                    = 'SEAMONKEY_2_29b1'
#  Old version info
releaseConfig['oldVersion']                 = '2.26b2'
releaseConfig['oldAppVersion']              = '2.26'
releaseConfig['oldBuildNumber']             = 2
releaseConfig['oldBaseTag']                 = 'SEAMONKEY_2_26b1'
releaseConfig['oldRepoPath']                = 'releases/comm-beta'
#  Next (nightly) version info
#     not yet available
#  Repository configuration, for tagging
releaseConfig['skip_tag']                   = False
releaseConfig['relbranchPrefix']            = 'SEA_COMM'
releaseConfig['sourceRepoName']             = 'comm-beta' # buildbot branch name
releaseConfig['sourceRepoPath']             = 'releases/comm-beta'
releaseConfig['sourceRepoRevision']         = 'ca5ec1a2966f'
releaseConfig['relbranchOverride']          = ''
#releaseConfig['productVersionFile']        = 'suite/config/version-20.txt'
releaseConfig['productVersionFile']         = ''
#   Mozilla
releaseConfig['mozillaRepoPath']            = 'releases/mozilla-beta'
releaseConfig['mozillaRepoRevision']        = 'FIREFOX_32_0b8_BUILD1'
releaseConfig['mozillaRelbranchOverride']   = 'GECKO320b8_2014081821_RELBRANCH' # put Gecko relbranch here that we base upon
#   Inspector
releaseConfig['inspectorRepoPath']          = 'dom-inspector' # leave empty if inspector is not to be tagged
releaseConfig['inspectorRepoRevision']      = 'SEA2_26_RELBRANCH'
releaseConfig['inspectorRelbranchOverride'] = ''
#   Venkman
releaseConfig['venkmanRepoPath']            = 'venkman' # leave empty if venkman is not to be tagged
releaseConfig['venkmanRepoRevision']        = 'SEA2_26_RELBRANCH'
releaseConfig['venkmanRelbranchOverride']   = ''
#   Chatzilla
releaseConfig['chatzillaRepoPath']          = 'chatzilla' # leave empty if chatzilla is not to be tagged
releaseConfig['chatzillaRepoRevision']      = 'SEA2_26_RELBRANCH'
releaseConfig['chatzillaRelbranchOverride'] = ''
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

# Mock
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux', 'linux64')
