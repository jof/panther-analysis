"""
Here, default values for `panther_config.config` are defined
"""

# A list of public DNS domain names that fall under the administrative domain of
# the Panther installation
ORGANIZATION_DOMAINS = ["example.com"]

DROPBOX_ALLOWED_SHARE_DOMAINS = ORGANIZATION_DOMAINS
DROPBOX_TRUSTED_OWNERSHIP_DOMAINS = ORGANIZATION_DOMAINS
GSUITE_TRUSTED_FORWARDING_DESTINATION_DOMAINS = ORGANIZATION_DOMAINS
GSUITE_TRUSTED_OWNERSHIP_DOMAINS = ORGANIZATION_DOMAINS
MS_EXCHANGE_ALLOWED_FORWARDING_DESTINATION_DOMAINS = ORGANIZATION_DOMAINS
MS_EXCHANGE_ALLOWED_FORWARDING_DESTINATION_EMAILS = ["postmaster@" + ORGANIZATION_DOMAINS[0]]
TELEPORT_ORGANIZATION_DOMAINS = ORGANIZATION_DOMAINS

# Key/value pairs of tags used to denote resources that are intentionally exposed
DMZ_TAGS = set(
    [
        ("environment", "dmz"),
    ]
)
