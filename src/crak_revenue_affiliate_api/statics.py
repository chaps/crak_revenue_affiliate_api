
CONDITIONAL_FILTERS = {
    "BETWEEN": {
        "description": "Objects which have a field \
        that is in a certain range, inclusive",
        "use": "range"
    },
    "EQUAL_TO": {
        "description": "Finds objects which do have the provided value.",
        "use": "value",
    },
    "NOT_EQUAL_TO": {
        "description": "Finds objects which do not have the provided value.",
        "use": "value",
    },
    "LESS_THAN": {
        "description": "Finds objects which have a value less \
        than the provided value",
        "use": "value"
    },
    "LESS_THAN_OR_EQUAL_TO":  {
        "description": "Finds objects which have a value less \
        than or equal to the provided value.",
        "use": "value"
    },
    "GREATER_THAN": {
        "description": "Finds objects which have a value greater\
         than the provided value.",
        "use": "value",
    },
    "GREATER_THAN_OR_EQUAL": {
        "use": "value",
        "description": "Finds objects which have a value greater than \
        or equal to the provided value.",
    },
    "LIKE": {
        "use": "value",
        "description": "Returns objects which have a value that matches the \
        provided string, using case - insensitive search. The '%' character \
        is a wildcard: use at the beginning of the string \
        to find values ending in that string, at the end of\
         the string to find values beginning with\
        that string, or in the middle to find values \
        bookended by two parts of \
        the string",
    },
    "NOT_LIKE": {
        "use": "value",
        "description": "Returns objects which have a value that does not match\
         the provided s tring. The '%' character is a wildcard, with the same\
          function as in the LIKE operator.",
    },
    "NULL": {
        "use": "flag",
        "description": "Finds objects which have a value that is NULL.\
        This is not the same as an empty string; you should use the EQUAL_TO\
         condition al to find objects whose value is an empty string.\
          Notice no \"values\" are passed for this conditional.",
    },
    "NOT_NULL": {
        "description": "Finds objects which have a value that is NOT NULL.\
         This is not the same as an empty string; \
         you should use the NOT_EQUAL_TO\
          conditional to find objects whose \
          value is an not an empty stri ng.\
           Notice no \"values\" are passed for this conditional.",
        "use": "flag"
    }

}

AFFILIATE_REPORT_GET_STATS_FIELDS = {
    "AdCampaign.name": {
        "description": "",

    },
    "Browser.display_name": {
    },
    "Browser.id": {
    },
    "Category.id": {
    },
    "Category.name": {
    },
    "Country.name": {
    },
    "Offer.name": {
    },
    "OfferFile.display": {},
    "OfferUrl.name": {},
    "OfferUrl.preview_url": {},
    "Stat.ad_campaign_creative_id": {},
    "Stat.ad_campaign_id": {},
    "Stat.affiliate_info": {},
    "Stat.affiliate_info1": {},
    "Stat.affiliate_info2": {},
    "Stat.affiliate_info3": {},
    "Stat.affiliate_info4": {},
    "Stat.affiliate_info5": {},
    "Stat.clicks": {},
    "Stat.conversions": {},
    "Stat.cpa": {},
    "Stat.cpc": {},
    "Stat.cpm": {},
    "Stat.ctr": {},
    "Stat.date": {},
    "Stat.erpc": {},
    "Stat.gross_clicks": {},
    "Stat.hour": {},
    "Stat.impressions": {},
    "Stat.ltr": {},
    "Stat.month": {},
    "Stat.offer_file_id": {},
    "Stat.offer_id": {},
    "Stat.offer_url_id": {},
    "Stat.payout": {},
    "Stat.payout_type": {},
    "Stat.source": {},
    "Stat.unique_clicks": {},
    "Stat.week": {},
    "Stat.year": {},
    "Stat.currency": {},
}


AFFILIATE_OFFER_FIND_ALL_FIELDS = {
    "require_terms_ and_conditions": {
        "description": "Whether or not this Offer requires prior approval\
         before an Affiliate can run it. The text of the terms and\
          conditions is in the \"terms_and_conditions\" field."
    },
    "is_expired": {
        "description": "Whether or not this Offer is expired\
         (i.e. it has a past \"expiration_date\")."
    },
    "use_target_rules": {
        "description": "Whether or not this Offer has Advanced\
         Targeting enabled."
    },
    "show_custom_variables": {
        "description": ""
    },
    "require_approval": "",
    "preview_url": "",
    "terms_and_conditions": "",
    "status": {
        "description": "The status of the Offer. Affiliates can only \
        view active Offers."
    },
    "percent_payout": {

    },
    "name": {
    },
    "dne_list_id": {
    },
    "default_payout": {
    },
    "featured": {},
    "currency": {},
    "payout_type": {},
    "is_pay_per_call": {},
    "monthly_payout_cap": {},
    "payout_cap": {},
    "monthly_conversion_cap": {},
    "conversion_cap": {},
    "has_goals_enabled": {},
    "email_instructions": {},
    "show_mail_list": {},
    "default_goal_name": {},
    "allow_website_links": {},
    "allow_direct_links": {},
    "dne_download_url": {},
    "dne_unsubscribe_url": {},
    "id": {},
    "expiration_date": {},
    "email_instructions_subject": {},
    "email_instructions_from": {},
    "description": {},
}

urls = {
    "Affiliate_Report": {
        "description": "Returns reports on the affiliate.",
        "url": "http://gateway.crakrevenue.com/affiliate",
        "params": {
            "default": {
                "Target": "Affiliate_Report",
                "Method": "getStats"
            },
            "required": {
                "api_key": {
                    "type": str,
                },
                "fields[]": {
                    "description": "List of fields to return",
                    "type": list,
                    "opts": AFFILIATE_REPORT_GET_STATS_FIELDS
                }
            },
            "optional": {
                "filters": {
                    "opts": AFFILIATE_REPORT_GET_STATS_FIELDS
                },
                "groups": {
                    "opts": AFFILIATE_REPORT_GET_STATS_FIELDS,
                    "type": list
                },
                "sort": {
                    "opts": AFFILIATE_REPORT_GET_STATS_FIELDS
                },
                "limit": {
                    "type": int
                },
                "page": {
                    "type": int
                },
                "totals": {
                    # 1 or 0
                    "type": bool
                },
                "data_start": {
                    type: str
                },
                "data_end": {
                    type: str
                },
                "hour_offset": {
                    type: int
                }

            }
        }

    },

    "Affiliate_Offer": {
        "description": "",
        "url": "http://gateway.crakrevenue.com/affiliate",
        "params": {
            "default": {
                "Target": "Affiliate_Offer",
                "Method": "findAll"
            },
            "required": {
                "api_key": {
                    "type": str,
                },
                "fields[]": {
                    "description": "List of fields to return",
                    "type": list,
                    "opts": AFFILIATE_OFFER_FIND_ALL_FIELDS
                }
            },
            "optional": {
                "filters": {
                    "opts": AFFILIATE_OFFER_FIND_ALL_FIELDS
                },
                "sort": {
                    "opts": AFFILIATE_OFFER_FIND_ALL_FIELDS
                },
                "limit": {
                    "type": int
                },
                "page": {
                    "type": int
                },
            }
        }
    }
}
